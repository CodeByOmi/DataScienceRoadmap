# import csv

# new_cleaned = []

# with open("order.csv", "r") as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     new_cleaned.append(header)

#     empty_price = 0 
#     invalid_price = 0
#     invalid_quantity = 0

#     for row in reader:
#         price = row[2]
#         quantity = row[3]

#         if price.strip() == "":
#             empty_price += 1
#             continue

#         try:
#             price_val = float(price)
#         except ValueError:
#             invalid_price += 1
#             continue

#         try:
#             quantity_val = int(quantity)
#         except ValueError:
#             invalid_quantity += 1
#             continue

#         new_cleaned.append(row)

        
#     print(empty_price)
#     print(invalid_price)
#     print(invalid_quantity)

    
# # new csv make
#     with open("new_cleaned", "w", newline ="") as file:
#         writer = csv.writer(file)
#         writer.writerows(new_cleaned)