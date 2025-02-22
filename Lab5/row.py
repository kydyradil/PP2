import re

def parse_receipt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.readlines()

    items = []
    item_pattern = re.compile(r'^\d+\.\n(.+?)\n(\d+,\d+) x ([\d\s]+,\d+)\n([\d\s]+,\d+)')

    i = 0
    while i < len(data) - 3:
        match = item_pattern.match("".join(data[i:i+4]))
        if match:
            name = match.group(1).strip()
            quantity = match.group(2).replace(',', '.')
            unit_price = match.group(3).replace(' ', '').replace(',', '.')
            total_price = match.group(4).replace(' ', '').replace(',', '.')
            items.append((name, float(quantity), float(unit_price), float(total_price)))
            i += 4  
        else:
            i += 1  

    return items

receipt_items = parse_receipt('/mnt/data/row.txt')

for item in receipt_items:
    print(f"Name: {item[0]}, Quantity: {item[1]}, Unit Price: {item[2]}, Total Price: {item[3]}")
