import sqlite3
# Step 1: Database Setup
# Modify the function for initializing the database so it is able to catch errors in database connections
def initialize_database():
    try:
        conn = sqlite3.connect("chocolate_house.db")
        cursor = conn.cursor()
        # Create tables (seasonal flavors, ingredients, customer suggestions)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seasonal_flavors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)


        
        cursor.execute(""" CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT  ,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
            unit TEXT NOT NULL,
                restock_level INTEGER NOT NULL
            )
             """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer_suggestions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                flavor_suggestion TEXT NOT NULL,
                allergy_concern TEXT
            )
        """)

        conn.commit()
        conn.close()
        print("Database initialized successfully!")

    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

#  Muliple of the above function is a method which prompts a user for data on a seasonal flavor of chocolate and adds it to the 'seasonal_flavors' table.


def add_seasonal_flavor():
     # Take info from user
    name = input("Flavor Name: ")
    description = input("Flavor Description: ")
    start_date = input("Start Date (YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")
    price = float(input("Price: "))

# Connect to the database
   
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()

    # Insert the flavor into the database
    cursor.execute("""
        INSERT INTO seasonal_flavors (name, description, start_date, end_date, price)
            VALUES (?, ?, ?, ?, ?)
        """, (name, description, start_date, end_date, price))
    print(f"Flavor '{name}' added successfully!")

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    
    
    print(f"Error adding seasonal flavor: {e}")

# Function to display all the existing flavour 
def display_all_flavors():
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM seasonal_flavors")
    flavors = cursor.fetchall()

    if not flavors:
        print("No seasonal flavors available!")
    else:
        print("Seasonal Flavors Available:")
        print("-" * 50)
        for flavor in flavors:
            print(f"ID: {flavor[0]} - Name: {flavor[1]} | Description: {flavor[2]}")
            print(f"Available from: {flavor[3]} to {flavor[4]}")
            print(f"Price: ${flavor[5]:.2f}")
            print("-" * 50)

    conn.close()

def add_ingredient():
# Take user input for ingredient data
        name = input("Enter the ingredient name: ")
        quantity = int(input("Enter the quantity: "))
        unit = input("Enter the unit of measurement (e.g., kg, liters): ")
        restock_level = int(input("Enter the restock level: "))

# CONNECT TO DB
        conn = sqlite3.connect("chocolate_house.db")
        cursor = conn.cursor()

     # Insert the ingredient into the table
        cursor.execute("""
     INSERT INTO ingredients (name, quantity, unit, restock_level)
     VALUES (?, ?, ?, ?)
     """, (name, quantity, unit, restock_level))
       
        print(f"Ingredient '{name}' added successfully!")
    # Save the changes and close the connection
        conn.commit()
        conn.close()

    
 
def display_ingredients():
        conn = sqlite3.connect("chocolate_house.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM ingredients")
        ingredients = cur.fetchall()

        if not ingredients:
            print("No ingredients found in the inventory!")
        else:
            print("Ingredient Inventory:")
            print("-" * 50)
            for ingredient in ingredients:
                print(f"ID: {ingredient[0]} - Name: {ingredient[1]} | Quantity: {ingredient[2]} {ingredient[3]}")
                print(f"Restock Level: {ingredient[4]}")
                print("-" * 50)
        conn.close()

# Calling the display flavour function to see all the existed flavour


# Add customer flavor suggestions and allergy concerns function
def add_customer_suggestion():
    try:
            customer_name = input("Enter the customer's name: ")
            flavor_suggestion = input("Enter the suggested flavor: ")
            allergy_concern = input("Enter any allergy concern (leave blank if none): ")

            conn = sqlite3.connect("chocolate_house.db")
            cursor = conn.cursor()  
        
            cursor.execute("""
            INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concern)
            VALUES (?, ?, ?)
            """, (customer_name, flavor_suggestion, allergy_concern))

            conn.commit()
            conn.close()
            print(f"Suggestion from '{customer_name}' added successfully!")

    except sqlite3.Error as e:
        print(f"Error adding customer suggestion: {e}")
        conn.close()

# Function to print all customer suggestions and allergy issues
def display_customer_suggestions():
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customer_suggestions")
    suggestions = cursor.fetchall()

    if not suggestions:
        print("No customer suggestions found!")
    else:
        print("Customer Flavor Suggestions:")
        print("-" * 50)
        for suggestion in suggestions:
            print(f"ID: {suggestion[0]}")
            print(f"Customer Name: {suggestion[1]}")
            print(f"Suggested Flavor: {suggestion[2]}")
            print(f"Allergy Concern: {suggestion[3] if suggestion[3] else 'None'}")
            print("-" * 50)
            
    conn.close()




