inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]
total=0
revenue=0
#low_stock=[]
for items in inventory:
    name,category,unit_price,units_sold,unit_left = items
    total += units_sold*unit_price
    if(unit_left<5):
        print(name)
print(total)
for items in inventory:
    name,category,unit_price,units_sold,unit_left = items
    revenue=unit_price*units_sold
    print(f"category : {category}  totalrevenue : {revenue}")

