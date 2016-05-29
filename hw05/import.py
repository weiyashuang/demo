import psycopg2

conn = psycopg2.connect(host="localhost", database="hw04", user="dbo", password="123456")

cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS hw_a;
CREATE TABLE IF NOT EXISTS hw_a (
    sn      INTEGER,
    Name    VARCHAR(10),
    PRIMARY KEY(sn)
);
''')



ins = 'INSERT INTO hw_a(sn,Name) VALUES (%s,%s)'
for i in range(6):
    sn = 10 + i*10
    Name = 'A%d' % sn
    cur.execute(ins,(sn,Name))


cur.execute('''
DROP TABLE IF EXISTS hw_b;
CREATE TABLE IF NOT EXISTS hw_b (
    sn      INTEGER,
    Name    VARCHAR(10),
    PRIMARY KEY(sn)
);
''')


ins = 'INSERT INTO hw_b(sn,Name) VALUES (%s,%s)'
for i in range(5):
    sn = 40 + i*10
    Name = 'B%d' % sn
    cur.execute(ins,(sn,Name))
conn.commit()






