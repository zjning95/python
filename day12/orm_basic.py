# @Time    : 2018/7/23 17:25
# @Author  : Jennings
# @Email   : zjn@wiwi.ink

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://Jennings:um7cpphy@106.14.3.173/wiwi?charset=utf8", encoding='utf-8')
# echo=True 打印详细信息

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<%s name:%s password:%s>" % (self.id, self.name, self.password)


Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例
# 创建
# user_obj = User(name="jack", password="23333")  # 生成你要创建的数据对象
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建
# Session.commit()  # 现此才统一提交，创建数据

# 查询
# data = Session.query(User).filter_by(name='jack').all()   # all(),first()
# data = Session.query(User).filter_by().all()   # all(),first()
# data = Session.query(User).filter(User.id > 0).filter(User.id < 3).all()
# data = Session.query(User).filter_by().first()
# # print(data[0].name, data[0].password)
# print(data)
# 修改
# data.name = 'sb'
# data.password = 'ooooxxxx'
# Session.commit()

# 回滚
# my_user = Session.query(User).filter_by(id=1).first()
# my_user.name = "Jack"
#
# fake_user = User(name='Rain', password='12345')
# Session.add(fake_user)
#
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 这时看session里有你刚添加和修改的数据
#
# Session.rollback()  # 此时你rollback一下
#
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 再查就发现刚才添加的数据没有了。

# 统计
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).count())

# 分组
print(Session.query(func.count(User.name), User.name).group_by(User.name).all())


