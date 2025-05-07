

#step 1
import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT c.customer_name, o.order_id, p.product_name FROM customers c JOIN orders o ON c.customer_id = o.customer_id 
    JOIN line_items li ON o.order_id = li.order_id JOIN products p ON li.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(df)

    cursor = conn.cursor()


SELECT 
line_items.line_item_id, 
line_items.quantity, 
line_items.product_id,
products.product_name, 
products.price
FROM 
line_items
JOIN 
book
ON 
line_items = book_id = books.book_id


#  Step 2

df = pd.read_sql_query(query, conn)


print("Sales DataFrame:")
print(df.head(5))

# Step 3: Add a 'total' column (quantity * price)

df['total'] = df['quantity'] * df['price']

#Print again after adding 'total'
print("\nDataFrame with 'total' column:")
print(df.head(5))

# Step 4: Group by product_id


sales_summary = df.groupby('product_id').agg(
line_item_count=('line_item_id', 'count'),
total_sales=('total', 'sum'),
product_name=('product_name', 'first')
).reset_index()

#Step 5: Sort by product_name
grouped = grouped.sort_values('product_name')

#Step 6: Print first 5 lines 
print("\nGrouped and Sorted DataFrame:")
print(grouped.head(5))

# Step 7: Write to order_summary.csv


grouped.to_csv('order_summary.csv', index=False)

conn.close()

if __name__ == "__main__":
    main()