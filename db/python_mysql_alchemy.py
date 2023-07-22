# -*- coding: utf-8 -*-
"""
    :author: allen lv
    sqlalchemy, python orm
"""
from sqlalchemy import Column,  create_engine, INTEGER,String
from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy.ext.declarative import declarative_base


# 创建对象的基类
Base = declarative_base()


# 定义User对象
class Vendor(Base):
    # 表名
    __tablename__ = 'vendors'
    #
    __table_args__ = {'extend_existing': True}
    # 表结构
    vend_id = Column(INTEGER,primary_key=True, autoincrement=True)
    vend_name = Column(String(50))
    vend_address = Column(String(50))

# "auth_plugin":'mysql_native_password'
engine = create_engine('mysql+mysqlconnector://root:lv123@localhost:3306/test?auth_plugin=mysql_native_password')
DBSession = sessionmaker(bind=engine)


# 创建session 对象
session = DBSession()
# 创建新对象用来插入表
new_vendor = Vendor(vend_name='vtest', vend_address='addtest')
session.add(new_vendor)
session.commit()
session.close()


# 查询刚才新插入的new_vendor
session = DBSession()
res = session.query(Vendor).filter(Vendor.vend_name=='vtest').one()
print('type:', type(res))
print('res:', res.vend_id, res.vend_name, res.vend_address)
session.close()