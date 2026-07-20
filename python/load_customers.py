import pandas as pd
import psycopg2


# Read CSV
customers = pd.read_csv("data/raw/customers.csv")

print(customers)


# Connect to PostgreSQL
connection = psycopg2.connect(
    host="localhost",
    database="ecommerce_analytics",
    user="anuja",
    password=""
)

cursor = connection.cursor()


# Insert data
for _, row in customers.iterrows():
    cursor.execute(
        """
        INSERT INTO customers
        (customer_id, first_name, last_name, email, country)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (customer_id) DO NOTHING;
        """,
        (
            row.customer_id,
            row.first_name,
            row.last_name,
            row.email,
            row.country
        )
    )


connection.commit()

cursor.close()
connection.close()

print("Customers loaded successfully!")