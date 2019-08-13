import json
import csv
import mysql.connector

# def sql_to_csv():
#     dbku = mysql.connector.connect(
#         host = 'localhost',
#         port = 3306,
#         user = 'root',
#         passwd = 'Th_697203',
#         auth_plugin = 'mysql_native_password',
#         database = 'doraemon'
#     )
#     kursor = dbku.cursor()
#     querydb = '''select * from karakter'''
#     kursor.execute(querydb)
#     # data = kursor.fetchall()
#     with open("new2.csv", "w", newline='') as csv_file:    
#         csv_writer = csv.writer(csv_file)
#         csv_writer.writerow([i[0] for i in kursor.description])
#         csv_writer.writerows(kursor)
# sql_to_csv()

# def csv_to_sql():
#     dbku = mysql.connector.connect(
#         host = 'localhost',
#         port = 3306,
#         user = 'root',
#         passwd = 'Th_697203',
#         auth_plugin = 'mysql_native_password',
#         database = 'doraemon'
#     )
#     kursor = dbku.cursor()
#     with open('new.csv', newline = '') as data:
#         lst = []
#         reader = csv.reader(data)
#         for row in reader:
#             lst.append(tuple(row))
#         lst.pop(0)
#         for l in lst:
#             query = """Insert into newcsv (id, nama, usia) VALUES (%s,%s,%s)"""
#             kursor.execute(query, l)
#     dbku.commit()
# csv_to_sql()

# def sql_to_json():
#     dbku = mysql.connector.connect(
#         host = 'localhost',
#         port = 3306,
#         user = 'root',
#         passwd = 'Th_697203',
#         auth_plugin = 'mysql_native_password',
#         database = 'doraemon'
#     )
#     kursor = dbku.cursor()
#     querydb = '''select * from karakter'''
#     kursor.execute(querydb)
#     data = kursor.fetchall()

#     with open('new2.json', 'w') as x:
#         json.dump(data,x)
# sql_to_json()

# def json_to_sql():
#     dbku = mysql.connector.connect(
#     host = 'localhost',
#     port = 3306,
#     user = 'root',
#     passwd = 'Th_697203',
#     auth_plugin = 'mysql_native_password',
#     database = 'doraemon'
#     )
#     kursor = dbku.cursor()
#     with open('new2.json') as x:
#         data = json.load(x)
#         for d in data:
#             print(d)
#             # query = """ Insert into newjson (id, nama, usia) values (%s,%s,%s)"""
#             # kursor.execute(query, tuple(d))
#             # dbku.commit()
# json_to_sql()
