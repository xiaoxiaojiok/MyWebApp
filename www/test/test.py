#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'XiaoJian'

from threading import local, Thread, currentThread
import sys
import logging

from mysql import connector

threadeddict = local()
threadeddict.name = "main"

ctx = {"username": "abc"}

class LocalThread(Thread):
    def run(self):
        print "-----local-------"
        print currentThread()
        print threadeddict.__dict__  # 可以访问到主线程中的变量，但是访问不了它的内容
        print ctx  # 变量和内容都可以访问
        print ctx
        threadeddict.name = self.getName()  # 改变值不会影响主线程
        print threadeddict.__dict__

config={
    'host':'125.216.243.42',
    'user': 'admin',
    'password': '123456',
    'database': 'mywebapp'
}

class DBTest(object):

    def testconnect(self):
        try:
            self.cnn = connector.connect(**config)
            print 'connect successfully!'
        except connector.Error as e:
            print('connect failed.'+format(e))
            sys.exit(0)

    def testcreate(self):
        sql_create='create table user(' \
                   'id int primary key,' \
                    'name varchar(20),' \
                    'age int);'
        self.cursor = self.cnn.cursor()
        self.cursor.execute(sql_create)
        self.cursor.close()

    def testinsert(self):
        sql_insert = "insert into user(id,name,age) values(1,'xiaojain',23)"
        self.cursor = self.cnn.cursor()
        self.cursor.execute(sql_insert)
        self.cursor.close()

    def testupdate(self):
        sql_update = "update user u set u.age = 18 where u.name = 'xiaojain'"
        self.cursor = self.cnn.cursor()
        self.cursor.execute(sql_update)
        self.cursor.close()

    def testdelete(self):
        sql_delete = "delete from user where user.id = 2"
        self.cursor = self.cnn.cursor()
        self.cursor.execute(sql_delete)
        self.cursor.close()

    def testselect(self):
        sql_select = "select * from user"
        self.cursor = self.cnn.cursor()
        self.cursor.execute(sql_select)
        print(self.cursor.fetchall())
        self.cursor.close()


def test(*tup,**mydic):
    if tup is not None:
        print 'tup '
        print tup
    if mydic is not None:
        print 'dic '
        print mydic

if __name__ == '__main__':
    # print "-----main-------"
    # print currentThread()
    # print threadeddict.__dict__
    #
    # A = LocalThread()
    # A.start()
    # A.join()
    #
    # print "-----main-------"
    # print currentThread()
    # print threadeddict.__dict__
    # print '%015d' % time.time()
    # db = DBTest()
    # db.testconnect()
    # db.testcreate()
    # db.testinsert()
    # db.testselect()
    # doctest.testmod()
    # test(usr='c')
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('debug')
    logging.info('info')
    logging.warning('warnning')
    logging.error('error')
