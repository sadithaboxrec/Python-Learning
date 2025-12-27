from menu import Menu
from order import Order

def main():

    print("Welcome to the Saditha's Cafe")
    
    menu = Menu()
    order = Order()

    menu.load_menu()  # to add food items to the menu list
    
    while True:

        menu.display()
        
        user_choice = input("Please enter a food item number or q to quit. ")

        if user_choice.lower() == "q":
            break
        elif user_choice == "":   
            print("Please enter a valid food item number.\n")
            continue

        elif not user_choice.isdigit():
            print("Please enter a valid food item number.\n")
            continue

        food_item = menu.get_item(int(user_choice))

        # user_quantity=input("Please enter the amount you like to order. ")
        # while True:
        #
        #     if user_quantity.isdigit() and int(user_quantity) > 0:
        #         quantity = int(user_quantity)
        #         break
        #     else:
        #         print("Please enter a valid quantity (1 or more).")
        #         continue


        while True:

            user_quantity = input("Please enter the amount you like to order. ")

            if user_quantity.isdigit() and int(user_quantity) > 0:
                user_quantity = int(user_quantity)
                break
            else:
                print("Please enter a valid quantity.")
                continue



        if food_item:
            order.add_item(food_item,user_quantity)
            print(f"{user_quantity} of {food_item.name} added to the cafe.")
        else:
            print("Please enter a valid food item number.\n")
            continue

    order.display_order()
    print(f"\nTotal Bill: Rs.{order.get_total()}")

    print("\nThank you for visiting Saditha's Cafe!")

if __name__ == "__main__":
    main()

