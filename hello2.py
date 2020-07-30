import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


star = db.movies2.find_one({'title':'월-E'})['star']
stars = list(db.movies2.find({'star':star}))
db.movies2.update_many({'star': star},{'$set': {'star': '0'}})
print(stars)