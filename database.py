import sqlite3
import sql_helpers
import os
import csv

if not os.path.exists("data"):
    os.mkdir("data")


def initialise(cursor):
    cursor.execute(sql_helpers.drop_table("fighters"))
    cursor.execute(
        sql_helpers.create_table(
            "fighters",
            {
                "fighter_id": "INTEGER PRIMARY KEY",
                "name": "TEXT",
                "nationality": "TEXT",
                "club_id": "INTEGER",
            },
        )
    )

    cursor.execute(sql_helpers.drop_table("clubs"))
    cursor.execute(
        sql_helpers.create_table(
            "clubs",
            {
                "club_id": "INTEGER PRIMARY KEY",
                "club_name": "TEXT",
                "club_short_name": "TEXT",
                "country": "TEXT",
                "state": "TEXT",
                "city": "TEXT",
                "parent_club_id": "INTEGER",
            },
        )
    )

    cursor.execute(sql_helpers.drop_table("categories"))
    cursor.execute(
        sql_helpers.create_table(
            "categories",
            {
                "category_id": "TEXT PRIMARY KEY",
                "category_name": "TEXT",
                "year": "INT",
                "event": "TEXT",
            },
        )
    )

    cursor.execute(sql_helpers.drop_table("participations"))
    cursor.execute(
        sql_helpers.create_table(
            "participations",
            {
                "category_id": "TEXT",
                "fighter_id": "INTEGER",
            },
        )
    )

    cursor.execute(sql_helpers.drop_table("ratings"))
    cursor.execute(
        sql_helpers.create_table(
            "ratings",
            {
                "fighter_id": "INTEGER",
                "event_id": "INTEGER",
                "category_name": "TEXT",
                "rank": "INT",
                "rank_before_event": "INT",
                "weighted_rating": "REAL",
                "weighted_rating_before_event": "REAL",
                "date": "TEXT",
            },
        )
    )

    return cursor

def table_to_csv(table):
    db_name = "data/hlo.db"
    conn = sqlite3.connect(database=db_name)
    cursor = conn.cursor()
    cursor.execute(f"select * from {table}")
    with open(f"data/{table}.csv", "w") as csv_file:
      csv_writer = csv.writer(csv_file, delimiter=",")
      csv_writer.writerow([i[0] for i in cursor.description])
      csv_writer.writerows(cursor)

    conn.commit()
    conn.close()
