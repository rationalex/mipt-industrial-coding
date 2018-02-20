from pymongo import MongoClient

DB_NAME = 'task1'

db = MongoClient('mongodb://localhost:27017/')[DB_NAME]

res = list(db['messages'].find())
if len(res):
  for i, r in enumerate(res):
    print('Message {}: {}'.format(i, r['message']))
else:
	print('[x] Database is empty')
