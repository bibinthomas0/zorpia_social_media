
from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://tbibin001:tbibin1234@cluster0.hehoznw.mongodb.net/?retryWrites=true&w=majority"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# # Create a new client and connect to the server
# # client = pymongo.MongoClient(uri)

# db = client.userside
url = 'mongodb://localhost:27017/'

client = MongoClient(url) 
 
db = client['userside'] 