import database

def export_to_csv():
    print("Exporting to csv")
    database.table_to_csv("fighters")
    database.table_to_csv("clubs")
    database.table_to_csv("categories")
    database.table_to_csv("participations")
    database.table_to_csv("ratings")

if __name__ == "__main__":
    export_to_csv()
