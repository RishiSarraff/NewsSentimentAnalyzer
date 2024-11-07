import sqlite3

conn = sqlite3.connect("cnnArticles.db")

cursor = conn.cursor()

def create_table():
    create_string = """
                    CREATE TABLE CNNArticles(
                        ID INTEGER PRIMARY KEY, 
                        PageTopic TEXT NOT NULL, 
                        Title TEXT NOT NULL, 
                        Author TEXT NOT NULL, 
                        Date TEXT NOT NULL, 
                        Content TEXT NOT NULL, 
                        Link TEXT NOT NULL)
                    """
    cursor.execute(create_string)

# only create table once
create_table()