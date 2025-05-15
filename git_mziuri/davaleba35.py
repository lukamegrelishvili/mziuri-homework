import sqlite3

conn = sqlite3.connect("sports.db")

c = conn.cursor()

c.execute(
    """ 
        CREATE TABLE IF NOT EXISTS footballers (
            ID integer primary key,
            name text,
            lastname text,
            age integer,
            country text
        )
    """
)

c.executemany(
    'insert into footballers (ID, name, lastname, age, country) values (?, ?, ?, ?, ?)',
    [
        (5, 'Luka ', 'Modrić', 39, 'Croatia'),
        (4, 'Kevin ', 'De Bruyne', 33, 'Belgium'),
        (3, 'Erling', 'Haaland', 24, 'Norway'),
        (1, 'Vinícius', 'Júnior', 24, 'Brazil'),
        (2, 'João', 'Félix', 25, 'Portugal')
    ]
)

c.execute(
    """
        update footballers
        set name = 'gandonio'
        where id = 3
    """
)

c.execute(
    """
        insert into footballers (id, name, lastname, age, country) values (12, 'Marcus', 'Rashford', '27', 'England')
    """
)

c.execute(
    """
        delete from footballers where id = 12
    """
)

c.execute('SELECT * FROM footballers')
rows = c.fetchall()
conn.close()

for row in rows:
    print(row)
