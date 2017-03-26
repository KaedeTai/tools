# coding=UTF-8
# 記得 conda install pymysql 或 pip install pymysql
import pymysql.cursors
import json

# 設定參數
filename = '會員資料.json'
tablename = 'member'
connection = pymysql.connect(host='localhost', user='workout', password='workout', db='workout', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

# 建立表格
obj = json.load(file(filename))
x = obj['data'][0]
keys = []
for k in x.keys():
    keys += ["`%s` text" % k]
sql = "create table `%s` (%s)"
with connection.cursor() as cursor:
    cursor.execute("drop table if exists `%s`" % tablename)
    cursor.execute(sql % (tablename, ",".join(keys)))

# 匯入資料
keys = []
vars = []
for k in x.keys():
    keys += [k]
    vars += ['%s']
sql = "insert into `%s` (`%s`) values (%s)" % (tablename, "`,`".join(keys), ",".join(vars))
for x in obj['data']:
    vals = []
    for k in x.keys():
        vals += [x[k]]
    with connection.cursor() as cursor:
        cursor.execute(sql, vals)
connection.commit()

