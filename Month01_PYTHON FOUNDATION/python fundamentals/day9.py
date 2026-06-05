
# import csv

# with open("order.csv", "r") as file:
#     reader = csv.reader(file)
#     # next(reader)
#     for row in reader:
#      print(row)

# fix empty price issue

# cleaned_rows = []
# with open("order.csv", "r") as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     cleaned_rows.append(header)
#     for row in reader:
#         if row[2] == "":
#             row[2] = "0"
#         cleaned_rows.append(row)
#     print(cleaned_rows)

# with open("cleaned_rows.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(cleaned_rows)

# Create CSV with products >= 50 rupee
# expensive_products = []

# with open("order.csv", "r") as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     expensive_products.append(header)

#     for row in reader:
#         if row[2] == "":
#             price = "0"
#         else:
#             price = row[2]

#         if float(price) >= 50:
#             expensive_products.append(row)

# # Write expensive products to new CSV
# with open("expensive_products.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(expensive_products)

# print(len(expensive_products))


