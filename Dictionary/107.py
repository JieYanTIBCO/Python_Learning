def inventory_management(inventory: dict, action: str, item: str, quantity: int = 0):  # type: ignore
    match action:
        case "check":
            if item in inventory:
                return inventory[item]
            else:
                return 0

        case "add":
            if item in inventory:
                inventory[item] += quantity
            else:
                inventory[item] = quantity
            return inventory
        case "update":
            if item not in inventory:
                print(f"{item} does not exist in the inventory")
            else:
                inventory[item] = quantity
            return inventory
        case "remove":
            if item in inventory:
                inventory[item] -= quantity
            else:
                print(f"{item} does not exist in the inventory")
            return inventory

        case "delete":
            inventory.pop(item, 0)
            return inventory


inventory = {
    'apple': 10,
    'banana': 5,
    'orange': 8
}

# 检查是否存在 'apple'，应该返回库存数量 10
print(inventory_management(inventory, "check", "apple"))

# 增加 'banana' 的库存数量 3，返回 {'apple': 10, 'banana': 8, 'orange': 8}
print(inventory_management(inventory, "add", "banana", 3))

# 增加 'grape' 的库存数量 15，返回 {'apple': 10, 'banana': 8, 'orange': 8, 'grape': 15}
print(inventory_management(inventory, "add", "grape", 15))

# 减少 'orange' 的库存数量 8（库存会为 0 并删除该物品），返回 {'apple': 10, 'banana': 8, 'grape': 15}
print(inventory_management(inventory, "remove", "orange", 8))

# 从库存中删除 'banana'，返回 {'apple': 10, 'grape': 15}
print(inventory_management(inventory, "delete", "banana"))

# 从库存中删除 'banana'，返回 {'apple': 10, 'grape': 15}
print(inventory_management(inventory, "update", "apple", 199))
