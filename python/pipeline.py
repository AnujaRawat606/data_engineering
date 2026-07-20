from extract import extract_csv
from load import load_customers, load_products, load_orders


customers = extract_csv(
    "data/raw/customers.csv"
)

products = extract_csv(
    "data/raw/products.csv"
)

orders = extract_csv(
    "data/raw/orders.csv"
)


load_customers(customers)

load_products(products)

load_orders(orders)


print("Pipeline completed!")