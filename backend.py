import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, genre text, status text, UNIQUE(title, author))")
    conn.commit()
    conn.close()
    
def insert(title,author,genre,status):
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book(title,author,genre,status) VALUES (?,?,?,?)", (title,author,genre,status))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()    
    return rows
    
def search(title="",author="",genre="",status=""):
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title =? OR author=? OR genre=? OR status=?", (title,author,genre,status))
    rows = cur.fetchall()
    conn.close()
    return rows     

def delete(id):
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()
 
def delete_all():
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book")
    conn.commit()
    conn.close()
    
def update(id,title,author,genre,status):
    conn=sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, genre=?, status=? WHERE id=?", (title,author,genre,status,id))
    conn.commit()
    conn.close()        
    
connect()
