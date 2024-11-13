import sqlite3
import csv

conn = sqlite3.connect("cnnArticles.db")

cursor = conn.cursor()

def create_table():
    create_string = """
                    CREATE TABLE CNNArticles(
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

def insert_into_DB(cnnObject):
    check_query = """
            SELECT COUNT(*)
            FROM CNNArticles
            WHERE Title = ? AND Link = ?
        """
    cursor.execute(check_query, (cnnObject['Title'], cnnObject['Link']))
    result = cursor.fetchone()

    if result[0] == 0:
        insert_string = """
                        INSERT INTO CNNArticles (PageTopic, Year, Month, Title, Author, Content, Link)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """

        cursor.execute(insert_string, (cnnObject['PageTopic'], cnnObject['Year'], cnnObject['Month'], cnnObject['Title'],
                                       cnnObject['Author'], cnnObject['Content'], cnnObject['Link'], ))

        conn.commit()


# only create table once
#create_table()
def to_csv(csv_filename):

    cursor.execute("SELECT * FROM CNNArticles")
    rows = cursor.fetchall()

    column_names = [description[0] for description in cursor.description]

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)
        writer.writerows(rows)

    print(f"Exported to {csv_filename}")


to_csv("cnn_articles.csv")