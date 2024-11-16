import sqlite3
from database import (initialize_database,add_seasonal_flavor, display_all_flavors, add_ingredient, display_ingredients, add_customer_suggestion, display_customer_suggestions)
    
def main_menu():
    
        while True:
            print("Welcome to the Chocolate House!")
            print("1. Add Seasonal Flavor")
            print("2. Display All Seasonal Flavors")
            print("3. Add Ingredient")
            print("4. Print All Ingredients")
            print("5. Append Customer Suggestion")
            print("6. Print All Customer Suggestions")
            print("7. Quit")
        
            choice = input("Choose an option: ")
            if choice == '1':
                    add_seasonal_flavor()
            elif choice == '2':
                    display_all_flavors()
            elif choice == '3':
                    add_ingredient()
            elif choice == '4':
                display_ingredients()
            elif choice == '5':
                add_customer_suggestion()
            elif choice == '6':
                    display_customer_suggestions()
            elif choice == '7':
                    print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a valid one.")
 
def update_seasonal_flavor():
    try:
        display_all_flavors()  # Show existing flavors to the user
        flavour_id = int(input("Enter the ID of the flavor you wish to update: "))
        conn = sqlite3.connect("chocolate_house.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM seasonal_flavors WHERE id = ?", (flavor_id,))
        flavor = cursor.fetchone()

        if not flavor:
            print("Flavor not found.")
        return

        name = input(f"Enter the new name (current: {flavor[1]}): ")
        description = input(f"Enter the new description (current: {flavor[2]}): ")
        start_date = input(f"Enter the new start date (current: {flavor[3]}): ")
        end_date = input(f"Enter the new end date (current: {flavor[4]}): ")
        price = float(input(f"Enter the new price (current: ${flavor[5]:.2f}): "))

        cursor.execute("""
            UPDATE seasonal_flavors
            SET name = ?, description = ?, start_date = ?, end_date = ?, price = ?
            WHERE id = ?
        """, (name, description, start_date, end_date, price, flavor_id))
        conn.commit()
        conn.close()
        print("Seasonal flavor updated successfully!")
    
    except sqlite3.Error as e:
        print(f"Error updating seasonal flavor: {e}")

                           
    try:
            print(display_all_flavors())   # Display existing flavors to the user
            flavor_id = int(input("Enter the ID of the flavor to delete: "))
            #
            conn = sqlite3.connect("chocolate_house.db")
            cursor = conn.cursor()

            cursor.execute("DELETE FROM seasonal_flavors WHERE id = ?", (flavor_id,))
            conn.commit()
            conn.close()

            print("Seasonal flavor deleted successfully!")
    
    except sqlite3.Error as e:
            print(f"Error deleting seasonal flavor: {e}")

if __name__ == "__main__":
 
            print("Welcome to the Chocolate House Management System!")
while True:
        print("Chocolate House Menu:")
        print("1. Initialize Database (Only needed for the first run)")
        print("2. Add Seasonal Flavor")
        print("3. Display All Flavors")
        print("4. Add Ingredient")
        print("5. Display Ingredients")
        print("6. Add Customer Suggestion")
        print("7. Display Customer Suggestions")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            initialize_database()
        elif choice == "2":
            add_seasonal_flavor()
        elif choice == "3":
            display_all_flavors()
        elif choice == "4":
         add_ingredient()
        elif choice == "5":
            display_ingredients()
        elif choice == "6":
            add_customer_suggestion()
        elif choice == "7":
            display_customer_suggestions()
        elif choice == "8":
            print("Exiting the system. Goodbye!")
        break
else:
        print("Invalid choice. Please try again.")

