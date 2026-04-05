import random
import csv
from datetime import datetime

card_types = ["Visa", "MasterCard", "Amex", "Rupay"]
categories = ["Shopping", "Food", "Travel", "Electronics", "Healthcare", "Entertainment"]
countries = ["India", "USA", "UAE", "UK", "Canada", "Australia"]

def generate_transaction(id):
    amount = random.randint(100, 20000)
    country = random.choice(countries)
    card_type = random.choice(card_types)
    category = random.choice(categories)
    
    if (
       (amount > 15000 and country != "India") or 
       (category == "Electronics" and amount > 12000) or
       (card_type == "Amex" and amount > 18000)
       ):
        fraud = "Yes"
    else:
        fraud = "No"

    return [
        id,
        datetime.now().strftime("%d-%m-%Y %H:%M"),
        card_type,
        category,
        amount,
        country,
        fraud
    ]

with open("../data/transactions.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Transaction_ID",
        "Date",
        "Card_Type",
        "Category",
        "Amount",
        "Country",
        "Fraud"
    ])

    for i in range(1, 1001):
        writer.writerow(generate_transaction(i))

print("Transaction dataset created successfully!")
print("Rows generated:",i)