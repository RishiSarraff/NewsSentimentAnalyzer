import sqlite3
import csv

conn = sqlite3.connect("foxArticles.db")

cursor = conn.cursor()

def create_table():
    create_string = """
                    CREATE TABLE FOXArticles(
                        ID INTEGER PRIMARY KEY, 
                        PageTopic TEXT NOT NULL, 
                        Year INTEGER NOT NULL,
                        Month INTEGER NOT NULL,
                        Title TEXT NOT NULL, 
                        Author TEXT NOT NULL, 
                        Content TEXT NOT NULL, 
                        Link TEXT NOT NULL)
                    """
    cursor.execute(create_string)

def insert_into_DB(foxObject):
    check_query = """
            SELECT COUNT(*)
            FROM FOXArticles
            WHERE Title = ? AND Link = ?
        """
    cursor.execute(check_query, (foxObject['Title'], foxObject['Link']))
    result = cursor.fetchone()

    if result[0] == 0:
        insert_string = """
                        INSERT INTO FOXArticles (PageTopic, Year, Month, Title, Author, Content, Link)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """

        cursor.execute(insert_string, (foxObject['PageTopic'], foxObject['Year'], foxObject['Month'], foxObject['Title'],
                                       foxObject['Author'], foxObject['Content'], foxObject['Link'], ))

        conn.commit()


# only create table once
#create_table()

def to_csv(csv_filename):
    cursor.execute("SELECT * FROM FOXArticles")
    rows = cursor.fetchall()

    column_names = [description[0] for description in cursor.description]

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)
        writer.writerows(rows)

    print(f"Exported to {csv_filename}")


to_csv("fox_articles.csv")