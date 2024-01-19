products = ["t-shirt", "mug", "hat", "book", "keychain"]
inventory = {}
customer_orders = set()

def initialize_inventory(products):
    for product in products:
        x = int(input(f"Input the quantity of {product}'s available: "))
        inventory[product]= x

def get_customer_orders():
    for y in range(3):
        while True:
            prdname = input(f"Enter product name #{y+1} from the list {products}")
            if prdname in products:
                if prdname in customer_orders:
                    print("already ordered")
                else:
                    customer_orders.add(prdname)
                    break
            else:
                print("not in products")
    return customer_orders

def update_invetory(customer_orders, inventory): 
    for orderedprd in customer_orders:
        inventory[orderedprd] = inventory[orderedprd] - 1

def calculate_order_statistics(customer_orders,products):
    TPO = len(customer_orders)
    PPO = (TPO/len(products))*100
    order_status = (PPO,TPO)
    print(f"Total Products Ordered: {order_status[1]}")
    print(f"Percentage of Products Ordered: {order_status[0]}%")

def print_inventory(inventory):
    for product, x in inventory.items():
        print(f"{product} : {x}") 

initialize_inventory(products)
get_customer_orders()
update_invetory(customer_orders,inventory)
calculate_order_statistics(customer_orders,products)
print_inventory(inventory)