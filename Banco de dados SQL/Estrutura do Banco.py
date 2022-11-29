import os

os.remove("jogodia20.db") if os.path.exists("jogodia20.db") else None

import sqlite3

con = sqlite3.connect("C:jogodia20")

type (con)

cur = con.cursor()

type(cur)

sql_create = 'create table deve''(nome varchar(100), ''veio varchar(10), ''bebeu varchar(11), ''comeu varchar(12), ''valor integer)'

cur.execute(sql_create)

sql_insert = 'insert into deve values (?, ?, ?, ?, ?)'

recset = [('Gomes', 'SIM', 'SIM', 'SIM', 30), 
         ('Marcelo', 'SIM', 'SIM', 'SIM', 30),
         ('Ricardo', 'SIM', 'SIM', 'SIM', 30),
         ('Torugo', 'SIM', 'NAO', 'SIM', 10),
         ('Vinicius', 'SIM', 'SIM', 'SIM', 30),
         ('Josue', 'SIM', 'NAO', 'SIM', 10)]

for rec in recset:
    cur.execute(sql_insert, rec)

con.commit()

sql_select = 'select * from deve'

cur.execute(sql_select)
dados = cur.fetchall()

for linha in dados:
    print('Nome: %s, Veio: %s, Bebeu: %s, Comeu: %s, Pagar: %d \n' % linha)

con.commit()

con.close()
