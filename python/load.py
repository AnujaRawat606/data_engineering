from database import get_connection


def load_customers(df):

    connection = get_connection()
    cursor = connection.cursor()

    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO customers
            (
            customer_id,
            first_name,
            last_name,
            email,
            country
            )
            VALUES (%s,%s,%s,%s,%s)
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

    print("Customers loaded")



    
def load_products(df):

    connection = get_connection()
    cursor = connection.cursor()

    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO products
            (
            product_id,
            product_name,
            category,
            price
            )
            VALUES (%s,%s,%s,%s)
            ON CONFLICT (product_id) DO NOTHING;
            """,
            (
                row.product_id,
                row.product_name,
                row.category,
                row.price
            )
        )

    connection.commit()

    cursor.close()
    connection.close()

    print("Products loaded")

def load_orders(df): 

    connection = get_connection()
    cursor = connection.cursor()

    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO orders
            (
            order_id,
            customer_id,
            product_id,
            quantity,
            order_date
            )
            VALUES (%s,%s,%s,%s,%s)
            ON CONFLICT (order_id) DO NOTHING;
            """,
            (
                row.order_id,
                row.customer_id,
                row.product_id,
                row.quantity,
                row.order_date
            )
        )

    connection.commit()

    cursor.close()
    connection.close()

    print("Orders loaded")