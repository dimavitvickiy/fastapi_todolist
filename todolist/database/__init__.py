import motor.motor_asyncio

DATABASE_URL = "mongodb://admin:password@db:27017/todo-list"
client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
db = client["todo-list"]
