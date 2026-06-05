# import csv

# with open("order.csv" , "r") as file:
#     reader = csv.reader(file)
#     # header = next(reader)

#     for row in reader:
#         print(row)



# convert strings to numbers
# import csv

# with open("order.csv" , "r") as file:
#     reader = csv.reader(file)
#     header = next(reader)

#     for row in reader:
#         product = row[1]
#         price = row[2]
#         quantity = row[3]

#         print(product, price, quantity)




# only quantity gretter than 2
# import csv

# with open("order.csv" , "r") as file:
#     reader = csv.reader(file)
#     header = next(reader)

#     for row in reader:
#         product = row[1]
#         price = row[2]
#         quantity = row[3]

#         if  quantity != 0 and int(quantity) > 2:
        
#          print(product)

# practice tasks


# import csv

# total_revenue = 0
# count = 0
# total = 0
# with open("order.csv" , "r") as file:
#     reader = csv.reader(file)
#     header = next(reader)
   
# total orders
    # for row in reader:
    #     count += 1
    # print("total orders:",count)

# missing price
#     for row in reader:
#         product = row[1]
#         price = row[2]
#         quantity = row[3]
#         if row[2] == "":
#             count += 1
#     print("total missing price:",count)  
# #

# totral revenue
    # for row in reader:
    #      product = row[1]
    #      price = row[2]
    #      quantity = row[3]
    #      if price != "":
    #       total = float(price) * int(quantity)
    #       total_revenue += total
    # print("total_revenue:", total_revenue)

     
        

