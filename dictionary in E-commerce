inventory = {
    "Laptop": 15,
    "Phone": 8,
    "Tablet": 12,
    "Headphones": 25,
    "Charger": 5
}
print("Initial Inventory:", inventory)
inventory["Mouse"] = 18
inventory["Phone"] += 5
print("\nUpdated Inventory:", inventory)
def low_stock(inv):
    return [item for item, qty in inv.items() if qty < 10]

print("Products with stock < 10:", low_stock(inventory))
if "Charger" in inventory:
    del inventory["Charger"]
print("After removing Charger:", inventory)
print("\nFinal Inventory:")
for product, qty in inventory.items():
    print(f"{product}: {qty}")