# -*- coding: utf-8 -*-
"""
    :author: allen lv
    python & mysql
"""
import mysql.connector

config = {
    'host': 'localhost',  # default localhost
    'user': 'root',
    'password': 'lv123',
    # 'port': 3306,  # 默认即为3306
    'database':'test', #无默认数据库
    'charset': 'utf8',  # 默认即为utf8
    'buffered': True,   # Unread result found
    "auth_plugin":'mysql_native_password'   # mysql8错误
}
try:
      conn = mysql.connector.connect(**config)
except mysql.connector.Error as e:
      print('connect fail %s' % e)

cursor = conn.cursor()

# show tables
cursor.execute('SHOW TABLES')
# 操作浮标拿到数据
res = cursor.fetchall()
# 执行插入语句
# insert into vendors (vend_name, vend_address) values('test123', 'testad')
cursor.execute('insert into vendors (vend_name, vend_address) values'
               ' (%s, %s)', ['test123', 'testad'])
print(cursor.rowcount)
# 提交事务
conn.commit()
# 关闭浮标
cursor.close()

# 开启查询
cursor = conn.cursor()
cursor.execute('select * from vendors where vend_name = %s', ('test123',))
res = cursor.fetchall()
print(res)