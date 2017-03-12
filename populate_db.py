import csv
import psycopg2

conn = psycopg2.connect("dbname=2003_osu_db user=raleigh host=/tmp/")

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute("CREATE TABLE data_table (id serial PRIMARY KEY, name varchar, rush_attempts integer, rush_yards integer, rush_TDs integer, pass_completions integer, pass_yards integer, pass_TDs integer);")
# creates a table in an existing database


def close_connection():
    conn.commit()
    cur.close()
    conn.close()


with open('sports_data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        cur.execute("INSERT INTO data_table (id, name, rush_attempts, rush_yards, rush_TDs, pass_completions, pass_yards, pass_TDs) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (int(row[0]), row[1], int(row[2]), int(row[3]), int(row[5]), int(row[6]), int(row[7]), int(row[9])))


close_connection()
