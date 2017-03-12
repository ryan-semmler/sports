import psycopg2
from sys import argv


# connect to an existing database
conn = psycopg2.connect("dbname=sql_tour user=raleigh host=/tmp/")


# Open a cursor to perform database operations
cur = conn.cursor()


cur.execute("CREATE TABLE sports_database (id serial PRIMARY KEY, name varchar, rush_atts integer, rush_yds integer, rush_tds integer, pass_recs integer, pass_yds integer, pass_tds integer);")
# creates a table in an existing database


def add_record(cur, id, name, rush_atts, rush_yds, rush_tds, pass_comps, pass_yds, pass_tds):
    cur.execute("INSERT INTO sports_database (id, name, rush attempts, rush yards, rush TDs, pass completions, pass yards, pass touchdowns) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, rush_atts, rush_yds, rush_tds, pass_recs, pass_yds, pass_tds))
