import requests

def idr_to_usd(jumlah, data):
    rate = int(data.json()["jual"])
    final = jumlah/rate
    return (jumlah, final, data)

def usd_to_idr(jumlah, data):
    rate = float(data.json()["beli"])
    final = float(jumlah) * rate
    return(jumlah, final, data)

def bitcoin_to_usd(jumlah, data):
    rate = float(data.json()["USD"]["sell"])
    final = float(jumlah) * rate
    return(jumlah, final, data)

def usd_to_bitcoin(jumlah, data):
    rate = float(data.json()["USD"]["buy"])
    final = jumlah/rate
    return(jumlah, final, data)

def exchange_result(currency, bank):
    url = 'https://kurs.web.id/api/v1/' + bank
    url2 = 'https://blockchain.info/ticker'
    data = requests.get(url)
    data2 = requests.get(url2)
    if currency == "1":
        jumlah = int(input("Silahkan input nominal uang yang akan dikonversi : Rp.  "))
        results = idr_to_usd(jumlah, data)
    elif currency == "2":
        jumlah = float(input("Silahkan input nominal uang yang akan dikonversi : USD  "))
        results = usd_to_idr(jumlah, data)
    elif currency == "3":
        jumlah = int(input("Silahkan input nominal uang yang akan dikonversi : Rp.  "))
        nominal = idr_to_usd(jumlah, data)
        results = usd_to_bitcoin(nominal[1], data2)
    elif currency == "4":
        jumlah = float(input("Silahkan input nominal bitcoin yang akan dikonversi : btc  "))
        nominal = bitcoin_to_usd(jumlah, data2)
        results = usd_to_idr(nominal[1], data)
    elif currency == "5":
        jumlah = float(input("Silahkan input nominal uang yang akan dikonversi : USD  "))
        results = usd_to_bitcoin(jumlah, data2)
    elif currency == "6":
        jumlah = float(input("Silahkan input nominal uang yang akan dikonversi : btc  "))
        results = bitcoin_to_usd(jumlah, data2)
    return results
def menu():
    currency = input("Selamat Datang\nSilahkan pilih konversi yang akan Anda lakukan:\n(1) IDR Indonesia => USD United States\n(2) USD United States => IDR Indonesia\n(3) IDR Indonesia => Bitcoin\n(4) Bitcoin => IDR Indonesia\n(5) USD United States => Bitcoin\n(6) Bitcoin => USD United States\n Pilihan Anda(1/2/3/4/5/6):  ")
    bank = input("Silahkan ketik bank pilihan Anda :  ").lower()
    product = exchange_result(currency, bank)
    if currency == "1":
        kurs_jual = int(product[2].json()["jual"])
        kurs_beli = int(product[2].json()["beli"])
        print("Hasil konversi Rp. " + str(product[0]) + " adalah USD " + str(product[1])+ "\n Dengan kurs jual = " + str(kurs_jual) + " dan kurs beli = "+ str(kurs_beli))
    elif currency == "2":
        kurs_jual = int(product[2].json()["jual"])
        kurs_beli = int(product[2].json()["beli"])
        print("Hasil konversi USD " + str(product[0]) + " adalah Rp. " + str(product[1])+ "\n Dengan kurs jual = " + str(kurs_jual) + " dan kurs beli = "+ str(kurs_beli))
    elif currency == "3":
        bit_jual = int(product[2].json()["USD"]["sell"])
        bit_beli = int(product[2].json()["USD"]["buy"])
        original = round((product[0] * 14276), -6)
        print("Hasil konversi Rp. " + str(original) + " adalah btc " + str(round(product[1], 3))+ "\n Dengan kurs jual = " + str(bit_jual) + " dan kurs beli = "+ str(bit_beli))
    elif currency == "4":
        bit_jual = int(product[2].json()["USD"]["sell"])
        bit_beli = int(product[2].json()["USD"]["buy"])
        print("Hasil konversi btc " + str(product[0]) + " adalah Rp. " + str((product[1]))+ "\n Dengan kurs jual = " + str(bit_jual) + " dan kurs beli = "+ str(bit_beli))
    elif currency == "5":        
        bit_jual = int(product[2].json()["USD"]["sell"])
        bit_beli = int(product[2].json()["USD"]["buy"])
        print("Hasil konversi USD " + str(product[0]) + " adalah btc " + str(round(product[1], 3))+ "\n Dengan kurs jual = " + str(bit_jual) + " dan kurs beli = "+ str(bit_beli))
    elif currency == "6": 
        bit_jual = int(product[2].json()["USD"]["sell"])
        bit_beli = int(product[2].json()["USD"]["buy"])
        print("Hasil konversi btc " + str(product[0]) + " adalah USD " + str(product[1])+ "\n Dengan kurs jual = " + str(bit_jual) + " dan kurs beli = "+ str(bit_beli))
menu()