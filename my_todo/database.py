import sqlite3

def init_db():
     conn = sqlite3.connect("todo.db")
     c = conn.cursor()
     conn.row_factory = sqlite3.Row
     c.execute(
          """
            CREATE TABLE IF NOT EXISTS todo (
               id integer primary key autoincrement,
               title text,
               text text
            )
          """
     )
     conn.close()

def read():
     conn = sqlite3.connect("todo.db")
     c = conn.cursor()
     c.execute("select * from todo")
     results = c.fetchall()
     data = []
     for row in results:
          todo = {
               "id": row[0],
               "title": row[1],
               "text": row[2]
               }
          data.append(todo)
     conn.close()
     return data

def create(title, text):
     conn = sqlite3.connect("todo.db")
     c = conn.cursor()
     c.execute("insert into todo (title, text) values (?, ?)", (title, text))
     conn.commit()
     conn.close()

def update(pk, title, text):
     conn = sqlite3.connect("todo.db")
     c = conn.cursor()
     c.execute("update todo set title = ?, text = ? where id = ?", (title, text,pk))
     conn.commit()
     conn.close()

def delete(pk):
     conn = sqlite3.connect("todo.db")
     c = conn.cursor()
     c.execute("delete from todo where id = ?", (pk,))
     conn.commit()
     conn.close()