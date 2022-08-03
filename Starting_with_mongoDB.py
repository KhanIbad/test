import pymongo

client = pymongo.MongoClient("mongodb+srv://test:mongodb@cluster0.hdren.mongodb.net/?retryWrites=true&w=majority",tls=True,tlsAllowInvalidCertificates=True)



db = client.test
print(db)

d = {"name":"ibad","email":"Ibadkhan@ineuron.ai","number":8800950941}

mydb = client['ibad']

coll = mydb['mongotest']

coll.insert_one(d)

