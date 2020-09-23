stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    """Display the contents of the inventory."""
    print("\nInventory:")
    item_total = 0

    for k, v in inventory.items():
        item_total += v
        print(v, k)

    print(f"Total number of items: {item_total}\n")

def add_to_inventory(inventory, added_items):
    """Add new loot to inventory."""
    for item in added_items:
        print(f"You got: {item}")
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory


dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

display_inventory(stuff)
add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)