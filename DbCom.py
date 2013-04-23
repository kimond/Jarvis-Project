#!/usr/bin/env python
import psycopg2


class DbCom(object):

    def __init__(self):
        conn = psycopg2.connect("dbname=test user=postgres")
        cur = conn.cursor()
    

