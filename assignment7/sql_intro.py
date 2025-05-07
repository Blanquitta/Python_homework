# #Task 2
# import sqlite3

# # Connect to a new SQLite database
# with  sqlite3.connect("../db/school.db") as conn:  # Create the file here, so that it is not pushed to GitHub!
#     print("Database created and connected successfully.")
#     cursor=conn.cursor()

    
#     cursor.execute("""
#     CREATE TABLE Publisher(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT UNIQUE NOT NULL
#     )
#       """ ),

#     # Creating magazines table
#     cursor.execute("""
#     CREATE TABLE magazines(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT UNIQUE NOT NULL,
#         publisher_id INTEGER NOT NULL,
# #         FOREIGN KEY (publisher_id) REFERENCES publishers(id)
# #     )
# #       """ ),
#     # Creating subscribers table
#     cursor.execute("""
#         CREATE TABLE subscribers (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         address TEXT NOT NULL
#    )
#      """),
    
#        # Task 3 Insert sample data into tables
#     def add_publisher(cursor, name, address):
#         cursor.execute("SELECT * publisher_id FROM publishers WHERE name = ?", (publisher,)) # 
#         results = cursor.fetchall()
#         if len(results) == 0:
#            print("This publihser not excist in the DB")
#            return 
#         publisher_id = results[0][0]
#         try:
#              cursor.execute("INSERT INTO Magazines (magazine_name, publisher_id) VALUES (?, ?)", (name, publisher))
#         except sqlite3.IntegrityError:
#             print(f"{name} is already in the database.")

#     def add_subscriber(cursor, name, address):
#          cursor.execute("SELECT Students id FROM subscribers WHERE name = ?,", (name, address))
#          result = cursor.fetchall()
#          if len(result) > 0:
#                print("This publihser not excist in the DB")
#                return 
#          cursor.execute("INSERT INTO subscribers(subscriber_name, subscriber_address) VALUES (?,?)",(name, address))

#     def add_subscriptions(cursor, magazine, susbscriber, address, espiration_date):
#         cursor.execute("SELECT id FROM Subscribers WHERE subscribers_name = ? AND subscribers_address = ?;",(subscribers))
#         result = cursor.fetchall()
#         if len(result) > 0:
#             subscriber_id=results[0][0]
#         else:
#          print(f"There was no subscriber named{subscribers}.")
#          cursor.execute("SELECT * FROM Magazine WHERE magazine_name = ?", (magazine))
#          results = cursor.fetchall()
#          if len(results) > 0:
#              magazine_id = result[0][0]
#          else:
             
#           print(f"There was no magazine named {magazine}.")

    
   

#     cursor.execute("INSERT INTO publisher (name) VALUES (' Peter')")
#     cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES ('Andrew', 1)")
#     cursor.execute("INSERT INTO subscribers (name, address) VALUES ('Albert', '120 Tarbor Circle' )")


#     conn.commit() 
#     cursor.execute("SELECT name FROM magazines WHERE type.'table'")
#     tables = cursor.fetchall()
#     print("tables in database:")
#     for table in tables:
#         print(f"\t{table[0]}")

#     add_student(cursor, 'Alice', 20, 'Computer Science')  
#     add_student(cursor, 'Bob', 22, 'History')
#     add_student(cursor, 'Charlie', 19, 'Biology')
#     add_course(cursor, 'Math 101', 'Dr. Smith')
#     add_course(cursor, 'English 101', 'Ms. Jones')
#     add_course(cursor, 'Chemistry 101', 'Dr. Lee')

#     print("Sample data inserted successfully.")

#     enroll_student(cursor, "Alice", "Math 101")
#     enroll_student(cursor, "Alice", "Chemistry 101")
#     enroll_student(cursor, "Bob", "Math 101")
#     enroll_student(cursor, "Bob", "English 101")
#     enroll_student(cursor, "Charlie", "English 101")

#     cursor.execute("SELECT * FROM enrollments WHERE name = 'enrollments'")
#     result = cursor.fetchall()
#     for row in result:
#         print(row) 

#     conn.commit() #  to commit to make them final! 
    
    
#     print("Sample data inserted successfully.")
# conn.execute("PRAGMA foreign_keys = 1")


# conn.close()
#  #4  
  

# query_magazines_publisher = """
# SELECT magazines.*
# FROM magazines
# SELECT all magazines sorted by;
# SELECT magazines sorted by name;
# JOIN publishers ON magazines.publisher_id = publishers.id
# WHERE publishers.id = ?;
# """
# cursor.execute("SELECT * FROM magazines WHERE name = 'magazines'")
# result = cursor.fetchall()
# for row in result:
#         print(row)

