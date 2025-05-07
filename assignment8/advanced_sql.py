
    # 2 Connect to the database
import sqlite3
conn = sqlite3.connect("../db/lesson.db") 
cursor = conn.cursor()

    # SQL query execute
query = """
    SELECT 
        orders.order_id AS order_id,
        SUM(products.price * line_items.quantity) AS total_price
    FROM 
        orders
    JOIN 
        line_items ON orders.order_id = line_items.order_id
    JOIN 
        products ON line_items.product_id = products.id
    GROUP BY 
        orders.id
    ORDER BY 
        orders.id
    LIMIT 5;
    """

    # Execute and fetch results
cursor.execute(query)
rows = cursor.fetchall()

    # Print results
for row in rows:
        print(f"Order ID: {row[0]}, Total Price: {row[1]:.2f}")
    

    # Close connection
conn.close()

if __name__ == "__main__":
    main()

#3
def main():
    conn = sqlite3.connect("../db/lesson.db"), 
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

try:
        # Start transaction
        conn.execute("BEGIN")

        # Get customer_id for 'Perez and Sons'
        cursor.execute("SELECT id FROM customers WHERE name = 'Perez and Sons'")
        customer_id = cursor.fetchone()[0]

        # Get employee_id for 'Miranda Harris'
        cursor.execute("SELECT id FROM employees WHERE name = 'Miranda Harris'")
        employee_id = cursor.fetchone()[0]

        # Get 5 least expensive products
        cursor.execute("SELECT id FROM products ORDER BY price ASC LIMIT 5")
        product_ids = [row[0] for row in cursor.fetchall()]

        # Insert new order, retrieve new order_id
        cursor.execute("""
            INSERT INTO orders (customer_id, employee_id)
            VALUES (?, ?)
            RETURNING id
        """, (customer_id, employee_id))
        order_id = cursor.fetchone()[0]

        # Insert 5 line_items (10 of each product)
        for product_id in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?)
            """, (order_id, product_id, 10))

            #RETURNING order_id 

        # Commit 
        conn.commit()

        #  print order info
        cursor.execute("""
            SELECT line_items.id, line_items.quantity, products.name
            FROM line_items
            JOIN products ON line_items.product_id = products.id
            WHERE line_items.order_id = ?
        """, (order_id,))
        rows = cursor.fetchall()

        # Print the results
        print(f"Order ID: {order_id}")
        for row in rows:
            print(f"Line Item ID: {row[0]}, Quantity: {row[1]}, Product Name: {row[2]}")

except Exception as e:
        print("Transaction failed:", e)
        conn.rollback()

finally:
        conn.close()

if __name__ == "__main__":
    main()
 #4 
    
def find_busy_employees():
    conn = sqlite3.connect("../db/lesson.db") 
    cursor = conn.cursor()

    query = """
    SELECT 
        employees.id AS employee_id,
        employees.first_name,
        employees.last_name,
        COUNT(orders.id) AS order_count
    FROM 
        employees
    JOIN 
        orders ON employees.id = orders.employee_id
    GROUP BY 
        employees.id
    HAVING 
        COUNT(orders.id) > 5;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    print("Employees with more than 5 orders:")
    for row in results:
        print(f"Employee ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Order Count: {row[3]}")

    conn.close()

if __name__ == "__main__":
    main()