balance = 0
inventory = {}
history = []

while True:
    print("\n" + "=" * 40)
    print("AVAILABLE COMMANDS:")
    print("- saldo")
    print("- sprzedaż")
    print("- zakup")
    print("- konto")
    print("- lista")
    print("- magazyn")
    print("- przegląd")
    print("- koniec")
    print("=" * 40)
    
    command = input("Enter command: ").strip().lower()
    
    if command == "koniec":
        print("Closing the program. Goodbye!")
        break
        
    elif command == "saldo":
        try:
            amount = float(input("Enter amount to add (or subtract with a minus sign): "))
            if balance + amount < 0:
                print("Error: Account balance cannot be negative!")
            else:
                balance += amount
                history.append(f"saldo: change by {amount}")
                print(f"Operation completed successfully. Current balance: {balance}")
        except ValueError:
            print("Error: Invalid numeric value provided.")
            
    elif command == "sprzedaż":
        product = input("Enter product name: ").strip()
        
        if product not in inventory:
            print(f"Error: Product '{product}' is not in the warehouse.")
            continue
            
        try:
            price = float(input("Enter selling price per unit: "))
            quantity = int(input("Enter quantity to sell: "))
            
            if price < 0 or quantity <= 0:
                print("Error: Price cannot be negative and quantity must be greater than 0.")
                continue
                
            if inventory[product]["quantity"] < quantity:
                print(f"Error: Not enough items in the warehouse. Available quantity: {inventory[product]['quantity']}")
                continue
                
            total_income = price * quantity
            balance += total_income
            inventory[product]["quantity"] -= quantity
            
            history.append(f"sprzedaż: {product}, price: {price}, quantity: {quantity}")
            print(f"Sale completed! Added {total_income} to the account.")
            
        except ValueError:
            print("Error: Invalid numeric data entered.")
            
    elif command == "zakup":
        product = input("Enter product name: ").strip()
        try:
            price = float(input("Enter purchase price per unit: "))
            quantity = int(input("Enter quantity: "))
            
            if price < 0 or quantity <= 0:
                print("Error: Price and quantity must be greater than zero.")
                continue
                
            total_cost = price * quantity
            
            if balance - total_cost < 0:
                print(f"Error: Insufficient funds on the account! Purchase cost: {total_cost}, current balance: {balance}")
                continue
                
            balance -= total_cost
            
            if product in inventory:
                inventory[product]["quantity"] += quantity
                inventory[product]["price"] = price
            else:
                inventory[product] = {"price": price, "quantity": quantity}
                
            history.append(f"zakup: {product}, price: {price}, quantity: {quantity}")
            print(f"Purchase completed successfully! Deducted {total_cost} from the account.")
            
        except ValueError:
            print("Error: Invalid numeric data entered.")
            
    elif command == "konto":
        print(f"Current account balance: {balance} PLN")
        
    elif command == "lista":
        print("\n--- TOTAL WAREHOUSE STATUS ---")
        if not inventory:
            print("The warehouse is empty.")
        else:
            for prod, data in inventory.items():
                print(f"Product: {prod} | Price: {data['price']} PLN | Quantity: {data['quantity']} pcs.")
        print("-" * 31)
        
    elif command == "magazyn":
        product = input("Enter product name to check: ").strip()
        if product in inventory:
            data = inventory[product]
            print(f"Product: {product} | Price: {data['price']} PLN | Quantity: {data['quantity']} pcs.")
        else:
            print(f"Product '{product}' is not in the warehouse.")
            
    elif command == "przegląd":
        total_actions = len(history)
        print(f"Total number of recorded actions: {total_actions}")
        
        if total_actions == 0:
            print("No recorded actions in history.")
            continue
            
        from_input = input(f"Enter range start (from 0 to {total_actions - 1}, or leave blank): ").strip()
        to_input = input(f"Enter range end (from 0 to {total_actions - 1}, or leave blank): ").strip()
        
        try:
            start = int(from_input) if from_input != "" else 0
            end = int(to_input) if to_input != "" else total_actions
            
            if start < 0 or end > total_actions or start > end:
                print(f"Error: Provided indices are out of range! Available index range: from 0 to {total_actions}")
            else:
                print(f"\n--- ACTIONS REVIEW (from {start} to {end}) ---")
                for i in range(start, end):
                    print(f"[{i}]: {history[i]}")
                print("-" * 40)
                
        except ValueError:
            print("Error: Indices must be integers.")
            
    else:
        print("Unknown command. Please try again from the available options.")