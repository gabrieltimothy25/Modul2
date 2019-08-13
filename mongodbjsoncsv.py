import pymongo
import json
import csv

# def mongo_to_json():
#     x = pymongo.MongoClient('mongodb://localhost:27017')
#     db = x['marvel']
#     col = db['avengers']
#     data = list(col.find())
#     new_data = []
#     with open('mongo1.json', 'w') as x:
#         for d in data:
#             d["_id"] = str(d["_id"])
#             new_data.append(d)
#         json.dump(data, x)
# mongo_to_json()


# def json_to_mongo():
#     x = pymongo.MongoClient('mongodb://localhost:27017')
#     db = x['latihan1']
#     col = db['newjson']
#     with open('mongo1.json') as x:
#         data = json.load(x)
#         for d in data:
#             col.insert_one(d)
# json_to_mongo()

# def mongo_to_csv():
#     x = pymongo.MongoClient('mongodb://localhost:27017')
#     db = x['marvel']
#     col = db['avengers']
#     data = list(col.find())
#     csv_data = []
#     for item in data:
#         item["_id"] = str(item["_id"])
#         keys1 = list(item.keys())
#         dicttemp = {}
#         for k in keys1:
#             dicttemp[k] = item[k]
#         csv_data.append(dicttemp)
#     with open('mongo1.csv', 'w', newline = '') as x:
#         tulis = csv.DictWriter(x, fieldnames=keys1)
#         tulis.writeheader()
#         for c in csv_data:
#             tulis.writerow(c)
# mongo_to_csv()

# def csv_to_mongo():
#     x = pymongo.MongoClient('mongodb://localhost:27017')
#     db = x['latihan1']
#     col = db['newcsv']
#     data = []
#     with open('mongo1.csv', 'r') as x:
#         baca = csv.DictReader(x)
#         for b in baca:
#             data.append(dict(b))
#         for d in data:
#             col.insert_one(d)
# csv_to_mongo()