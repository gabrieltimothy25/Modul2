import json
import csv

#def json_to_csv():
with open('list1.json') as x:
    data = json.load(x)

with open('x.csv', 'w', newline='') as x:
    kolom = list(data[0].keys())
    tulis = csv.DictWriter(x, fieldnames=kolom)
    tulis.writeheader()
    tulis.writerows(data)


#def csv_to_json():
data = []
with open('new.csv', 'r') as x:
    reader = csv.DictReader(x)
    for i in reader:
        print(i)
        data.append(dict(i))
print(data)

with open('x.json', 'w') as x:
    json.dump(data, x)