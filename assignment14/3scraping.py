import sqlite3
import os
import pandas as pd

title = driver.title ("Alex_Rodriguez_Homeruns")

df = pd.read_csv("homerun_avg_cleaned.csv") 

conn = sqlite3.connect("mlb_history.db")

with sqlite3.connect( "mlb_history.db") as conn:
 cursor = conn.cursor()
 import sqlite3 

cursor = conn.cursor()

DB_PATH = "mlb_history.db"

def list_tables(conn):
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    return tables

def run_join_query(conn):
    print("\nExample JOIN: player batting stats with team standings for same year.")
    year = input("Enter year to query (e.g., 1995,2012): ")

years = ",".join(str(y) for y in range(1995, 2012))
print(years)  


DB_PATH = "../mlb_history.db"

query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql(query. conn)
table_names = tables['name'].tolist()

try:
    df = ()
    st.mlb_history.db(df)
except Exception as e:
    st.error(f"Failed to load table: {e}")
    st.stop()

available_tables = ["batting_leaders", "team_stats", "standings"]
selected_year = 1996
tables_for_year = ["team_stats", "batting_leaders"]
selected_tables = ["batting_leaders", "standings"]


st.write("Available tables:", "tables")
st.write("Selected year:", selected_year)
st.write("Tables for year:", year_tables)
st.write("Selected table:", selected_table)



  
print("\nAvailable tables for year", year)
for idx, tname in enumerate(table_options):
        print(f"[{idx}] {tname}")

    # try:
        t1_idx = int(input("Choose main table index (e.g., 0): "))
        t2_idx = int(input("Choose table to join with (e.g., 1): "))
        t1 = table_options[t1_idx]
        t2 = table_options[t2_idx]
        join_col = input("Enter column name to join on (e.g., 'Player' or 'Team'): ")

query = f"""
        SELECT *
        FROM "{t1}" AS A
        JOIN "{t2}" AS B
        ON A."{join_col}" = B."{join_col}"
        LIMIT 20;
        """

df = pd.read_sql_query(query, conn)
print("\nJOIN RESULT (first 20 rows):")
print(df.to_string(index=False))

    except Exception as e:
    print("Error:", e)

    def custom_sql(conn):
     print("\nEnter custom SQL (end with semicolon `;`):")
    sql = ""
    while not sql.strip().endswith(";"):
        sql += input("SQL> ") + "\n"

    try:
        df = pd.read_sql_query(sql.strip(), conn)
        print(df.to_string(index=False))
    except Exception as e:
        print("Query error:", e)

    def main():
        if not os.path.exists(DB_PATH):
            print(f"Database not found at {DB_PATH}. Run the import script first.")
            return

    conn = sqlite3.connect(DB_PATH)
    print("Connected to MLB History Database.")

    while True:
        print("\n=== MENU ===")
        print("[1] List Tables")
        print("[2] Run Predefined JOIN Query")
        print("[3] Run Custom SQL")
        print("[4] Exit")
        choice = input("Choose option: ")

        if choice == "1":
            tables = list_tables(conn)
            print("\nTables in DB:")
            for t in tables:
                print(" -", t)
        elif choice == "2":
            run_join_query(conn)
        elif choice == "3":
            custom_sql(conn)
        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.")

    conn.close()

if __name__ == "__main__":
    import pandas as pd
    main()