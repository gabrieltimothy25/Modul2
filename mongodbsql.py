import mysql.connector
import pymongo

# def mongo_to_sql():
    # x = pymongo.MongoClient('mongodb://localhost:27017')
    # db = x['marvel']
    # col = db['avengers']
    # data = list(col.find())
    # dbku = mysql.connector.connect(
    #     host = 'localhost',
    #     port = 3306,
    #     user = 'root',
    #     passwd = 'Th_697203',
    #     auth_plugin = 'mysql_native_password',
    #     database = 'marvel'
    #     )
    # kursor = dbku.cursor()
#     sql_data = []
#     for d in data:
#         temp = []
#         for b in d:
#             temp.append(d[b])
#             temp[0] = str(temp[0])
#         sql_data.append(temp)
#     for s in sql_data:
#         query = ''' Insert into Avengers (_id, title, usia, kota) values (%s, %s, %s, %s)'''
#         kursor.execute(query, tuple(s))
#     dbku.commit()
# mongo_to_sql()

def sql_to_mongo():
    x = pymongo.MongoClient('mongodb://localhost:27017')
    db = x['latihan1']
    col = db['Avengers']
    dbku = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = 'Th_697203',
        auth_plugin = 'mysql_native_password',
        database = 'marvel'
        )
    kursor = dbku.cursor()
    query = '''select * from Avengers'''
    kursor.execute(query)
    data = kursor.fetchall()
    for _id, title, usia, kota in list(data):
        col.insert_one({'_id': _id,
                        'title': title,
                        'usia': usia,
                        'kota': kota})
sql_to_mongo()