from collections import defaultdict

# Creating a defaultdict to store data about each customer's purchases
customer_purchases = defaultdict(lambda: defaultdict(int))

# Reading purchase data from stdin
while True:
    try:
        line = input().strip()
        if not line:
            break

        customer, item, quantity = line.split()
        quantity = int(quantity)

        # Filling in the defaultdict with data about each customer's purchases
        customer_purchases[customer][item] += quantity

    except EOFError:
        break

# Sorting the list of all buyers in lexicographical order
sorted_customers = sorted(customer_purchases.keys())

# We display information about each customer's purchases
for customer in sorted_customers:
    print(customer + ":")
    # Sorting the list of products in lexicographic order
    sorted_items = sorted(customer_purchases[customer].items())
    for item, quantity in sorted_items:
        print(item, quantity)
