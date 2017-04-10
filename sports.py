import psycopg2
# from sys import argv


conn = psycopg2.connect("dbname=2003_osu_db user=raleigh host=/tmp/")

cur = conn.cursor()


def add_player(cur, ID, name, rush_atts, rush_yds, rush_tds, pass_comps, pass_yds, pass_tds):
    cur.execute("INSERT INTO data_table (ID, name, rush_attempts, rush_yards, rush_tds, pass_completions, pass_yards, pass_tds) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ID, name, rush_atts, rush_yds, rush_tds, pass_comps, pass_yds, pass_tds))


def find_player(cur, name_input):
    cur.execute("SELECT * FROM data_table WHERE name = %s", (name_input,))
    results = cur.fetchone()
    if not results:
        return None
    print(name_input, '\n')
    print("Rushing attempts:", results[2])
    print("Rushing yards:", results[3])
    print("Rushing touchdowns:", results[4])
    print("Pass completions:", results[5])
    print("Pass yards:", results[6])
    print("Pass touchdowns:", results[7], '\n')


def delete_player(cur, name_input):
    cur.execute("SELECT * FROM data_table WHERE name = %s", (name_input,))
    results = cur.fetchone()
    if not results:
        return None
    cur.execute("DELETE FROM data_table WHERE name = %s", (name_input,))


def main(cur):
    while True:
        action = int(input("What would you like to do?\n\t1. Look up a player\n\t2. Add a player\n\t3. Delete a player\n\t4. Quit\n"))
        if action == 1:
            find_player(cur, input("Enter the player's name: "))
        if action == 2:
            ID = int(input("Enter the player's number: "))
            name = input("Enter the player's name: ")
            rush_atts = int(input("Enter the player's rush attempts: "))
            rush_yds = int(input("Enter the player's total rushing yards: "))
            rush_tds = int(input("Enter the player's total rushing touchdowns: "))
            pass_comps = int(input("Enter the player's total pass completions: "))
            pass_yds = int(input("Enter the player's total pass yards: "))
            pass_tds = int(input("Enter the player's total pass touchdowns: "))
            add_player(cur, ID, name, rush_atts, rush_yds, rush_tds, pass_comps, pass_yds, pass_tds)
            conn.commit()
        if action == 4:
            break
        if action == 3:
            delete_player(cur, input("Enter the player's name: "))
            conn.commit()


def close_connection():
    cur.close()
    conn.close()


main(cur)
close_connection()
