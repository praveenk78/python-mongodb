from pymongo import MongoClient
client = MongoClient()
db = client.mydatabase
collection = db.mycollection
doc = {"name": "John", "age": 30, "city": "New York"}
# result = collection.insert_one(doc)
# print(result.inserted_id)

# docs = [
#     {"name": "kabil", "age":35, "city": "Bangalore"},
#     {"name": "bala", "age":33, "city": "australia"}
# ]
# result = collection.insert_many(docs)
# print(result.inserted_ids)

# db = [
#     {"holder name": "barath", "Acc no": 123456, "Balance": 50000, "Mobile no": 2345678936},
#     {"holder name": "arun", "Acc no": 135791, "Balance": 65000, "Mobile no": 2468104680},
#     {"holder name": "santhosh", "Acc no": 234567, "Balance": 32000, "Mobile no": 1324657980},
# ]

# result = collection.insert_many(db)
# print(result.inserted_ids)

result = collection.find_one()
print(result)

result = collection.find_one({"holder name": "barath"})
print(result)

res = collection.find({"Balance": {"$gt" : 40000}})
for r in res:
    print(r)

result = collection.find({"Acc no":{"$exists":"true"}})
for i in result:
    print(i)

res = collection.find().sort({"Balance": 1}).skip(12)
for i in res:
    print(i)

criteria = {"name": "barath"}
new_values = {"$set": {"Balance":72000}}
collection.update_one(criteria, new_values)

result = collection.find(criteria)
for i in result:
    print(i)



criteria = {"holder name": "barath"}
new_values = {"$set": {"Balance":72000}}
collection.update_many(criteria, new_values)

result = collection.find(criteria)
for i in result:
    print(i)

collection.delete_many({"name":"bala"})