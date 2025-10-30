groceries = ["milk", "bread", "eggs", "cheese", "butter"]
try:
    item = input("What do you want to buy?   ")
    if item in groceries:
        groceries.remove(item)
        print(f"person bought {item}.")
    else:
        print("Not in the list.")
    print("Updated grocery list:", groceries)
except Exception:
    print("Error")