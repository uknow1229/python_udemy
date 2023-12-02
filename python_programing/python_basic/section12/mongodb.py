# MongoDB
# ドキュメント思考データベース
# データを挿入するときはJSON形式で記述して保存
# SQLを書かないのでNOSQLとも言われる

import datetime

from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

stack1 = {
  'name': 'customer1',
  'pip': ['python', 'java', 'go'],
  'info': {'os': 'mac'},
  'data': datetime.datetime.utcnow()
}

stack2 = {
  'name': 'customer2',
  'pip': ['python', 'java'],
  'info': {'os': 'windows'},
  'data': datetime.datetime.utcnow()
}

db_stacks = db.stacks
stack_id = db_stacks.insert_one(stack1).inserted_id
print(stack_id, type(stack_id))
print("##########")
print(db_stacks.find_one({'_id': stack_id}))


for stack in db_stacks.find():
    print(stack)

# datetimeで検索
now = datetime.datetime.utcnow()
for stack in db_stacks.find({'data': {'$lt': now}}):
    print(stack)

# mongoDBの使い方としては
# ログや上記情報を大量に入れて、後で読み取りで使うという場合に使うケースが多い！
# MySQLのように複雑な検索に対応していないが、非常にスピードが速い！

# アプリケーションの使い方によってDBを選ぶ

# update
db_stacks.find_one_and_update(
    {'name': 'customer1'}, {'$set': {'name': 'YYY'}})
# setは値を書き換えるとき
print(db_stacks.find_one({'name': 'YYY'}))

# delete
db_stacks.delete_one({'name': 'YYY'})
print(db_stacks.find_one({'name': 'YYY'}))