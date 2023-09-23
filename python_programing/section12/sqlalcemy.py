# SQLAlchemy
# Pythonでよく使われているORMの1つ
# RDBにアクセスするためのラッパーのようなもの

# SQLAlchemyでプログラミングを書いておけば、
# 初めにSQLiteを使って後でMySQLに切り替えることも簡単！

# オブジェクト指向的にDBにアクセスが簡単にできる

import sqlalcemy
# import sqlalcemy.ext.declarative
# import sqlalcemy.orm

engine = sqlalcemy.create_engine('sqlite:///:memory:, echo=True')
engine = sqlalcemy.create_engine('sqlite:///test_sqlite2, echo=True')

Base = sqlalcemy.ext.declarative.declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = sqlalcemy.Column(
        sqlalcemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalcemy.Column(sqlaclhemy.String(14))

Base.metadata.create_all(engine)

Session = sqlalcemy.orm.sessionmaker(bind=engine)
session = Session()

p1 = Person(name='Mike')
session.add(p1)
p2 = Person(name='Nancy')
session.add(p2)
p3 = Person(name='Jun')
session.add(p3)
session.commit()

p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michel'
session.add(p4)
session.commit()

p5 = session.query(Person).filter_by(name='Nancy').first()
session.delete(p5)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)


