import mysql.connector
from mysql.connector import errorcode

print('Conectando...')
connector = None
try:
    connector = mysql.connector.connect(
        host='db',
        user='root',
        password='K21h3fI5X!!'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

# criando o banco para sermos felizes
cursor = connector.cursor()

cursor.execute("DROP DATABASE IF EXISTS calculator;")

cursor.execute("CREATE DATABASE calculator;")

cursor.execute("USE calculator;")

# criando tabelas
TABLES = {}
TABLES['Foods'] = ('''
    CREATE TABLE foods (
    id int NOT NULL AUTO_INCREMENT,
    image varchar(150) NOT NULL,
    name varchar(50) NOT NULL,
    calories float NOT NULL,
    quantity int NOT NULL,
    PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print('Criando tabela {}:'.format(tabela_nome), end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err.msg)
    else:
        print('OK')

# commitando se não nada tem efeito
connector.commit()

cursor.close()
connector.close()
