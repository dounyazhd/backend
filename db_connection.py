from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://dounya:candle2024@ecommerce-candle.syieqkc.mongodb.net/?retryWrites=true&w=majority&appName=ecommerce-candle"
)

db = client['ecommerce-candle']
