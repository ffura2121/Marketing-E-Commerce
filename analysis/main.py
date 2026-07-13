import pandas as pd

campaigns = pd.read_csv("Data/campaigns.csv")
customers = pd.read_csv("Data/customers.csv")
events = pd.read_csv("Data/events.csv")
products = pd.read_csv("Data/products.csv")
transactions = pd.read_csv("Data/transactions.csv")

def get_info():
    campaigns.info()
    customers.info()
    events.info()
    products.info()
    transactions.info()

def get_head(x):
    print(f"campaigns:\n{campaigns.head(x)}")
    # print(f"customers:\n{customers.head(x)}")
    # print(f"events:\n{events.head(x)}")
    # print(f"products:\n{products.head(x)}")
    # print(f"transactions:\n{transactions.head(x)}")

get_head(10)