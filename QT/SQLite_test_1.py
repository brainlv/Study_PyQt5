from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import random

x = random.randint(0, 9)
y = random.randint(0, 9)
z = random.randint(0, 9)
a = random.randint(0, 9)


def creatDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./db/database.db')
    if not db.open():
        print("无法建立与数据库的链接")
        return False
    global query
    query = QSqlQuery()
    query.exec_('create table test(temperature REAL,distance REAL,num integer,heart int)')
    query.exec_('insert into test values(%s,%s,%s,%s)' % (x, y, z, a))
    db.close()
    return True


if __name__ == '__main__':
    creatDB()
