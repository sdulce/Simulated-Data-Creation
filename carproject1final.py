import random
import csv
from datetime import datetime, timedelta

class Car:
    def __init__(self, brand, model, paint_color, price):
        self.brand = brand
        self.model = model
        self.paint_color = paint_color
        self.price = price

    def __str__(self) -> str:
        return f"{self.brand} {self.model} in {self.paint_color} - ${self.price:,.2f}"

class Order:
    def __init__(self, order_id, customer_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self.cars = []
        self.timestamp = self.generate_timestamp()

    def generate_timestamp(self):
        date = datetime(2024, random.randint(1, 12), random.randint(1, 28))
        time = timedelta(hours=random.randint(8, 20), minutes=random.randint(0, 59))
        return date + time

    def add_car(self, car: Car):
        self.cars.append(car)

    def get_total_price(self):
        return sum(car.price for car in self.cars)

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.orders = []

    def create_order(self):
        order_id = random.randint(1000, 9999)
        order = Order(order_id, self.customer_id)
        self.orders.append(order)
        return order

class Store:
    def __init__(self, store_id, corporation_name):
        self.store_id = store_id
        self.corporation_name = corporation_name
        self.customers = []
        self.cars = self.generate_cars()

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def generate_cars(self):
        brands = ["Porsche", "BMW", "Mercedes", "Lexus"]
        models = ["Coupe", "Sedan", "SUV", "Convertible"]
        paint_colors = ["Black", "White", "Red", "Silver", "Grey"]
        
        cars = [Car(brand=random.choice(brands),
                    model=random.choice(models),
                    paint_color=random.choice(paint_colors),
                    price=random.randint(30000, 120000)) for _ in range(10)]
        return cars

    def create_customer_order(self, customer: Customer):
        order = customer.create_order()
        for _ in range(random.randint(1, 3)):  # Each order includes 1-3 cars
            car = random.choice(self.cars)
            order.add_car(car)
        return order

class Corporation:
    def __init__(self, name):
        self.name = name
        self.stores = []
        self.generate_stores()

    def generate_stores(self):
        num_stores = random.randint(1, 2500)
        for _ in range(num_stores):
            store_id = random.randint(1, 2500)
            store = Store(store_id, self.name)
            self.stores.append(store)
            self.generate_customers(store)

    def generate_customers(self, store):
        num_customers = random.randint(1, 1000)
        for _ in range(num_customers):
            customer_id = random.randint(1, 1000)
            customer_name = generate_random_name()
            customer = Customer(customer_id, customer_name)
            store.add_customer(customer)

    def simulate_sales(self):
        sales_data = []  #key list, to store all the xact data, use this below
        for store in self.stores:
            for customer in store.customers:
                order = store.create_customer_order(customer)
                for car in order.cars:  #iterate all products
                    sales_data.append([   #KEY MOMENT - write every transaction data to the list
                        order.timestamp.strftime("%Y-%m-%d"),  #date 
                        order.timestamp.strftime("%H:%M"),     #time
                        store.store_id,                        #store id, unique
                        customer.customer_id,                   # customer id
                        order.order_id,                         #order id, already generated
                        f"{car.brand} {car.model}",                 #formatted brand/model
                        car.paint_color,                                    
                        car.price                               #price
                    ]) #becomes one objects
        self.export_sales_to_csv(sales_data) #sales_data was def prior, ~13 rows ago

    def export_sales_to_csv(self, sales_data):
        filename = "luxury_dealership_sales_data.csv"
        headers = ["Date", "Time", "StoreID", "CustomerID", "OrderID", "Car Brand & Model", "Paint Color", "Price"]
        
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(sales_data)

# Helper function to generate random names
first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Fiona", "George", "Hannah", "Ivy", "Jack", "Liam", "Emma", "Noah", "Olivia", "William", "Sophia", "James", "Isabella", "Lucas", "Mia"]
last_names = ["Smith", "Johnson", "Brown", "Wilson", "Adams", "Garcia", "Martinez", "Lee", "Rodriguez", "Kim", "Anderson", "Thomas", "Taylor", "Clark", "Lewis", "Walker", "Hall", "Allen", "Young", "Hernandez"]

def generate_random_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Testing
corporation = Corporation("Luxury Dealership")
corporation.simulate_sales()  # Simulate sales and export to CSV
