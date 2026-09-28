## amtplotlib
import numpy as np
import matplotlib.pyplot as plt

## line chart

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 130, 200]

plt.plot(months, sales)
plt.show()


days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [120, 150, 140, 180, 200]

plt.plot(days,sales)
plt.title("growth chart")
plt.xlabel("week Days")
plt.ylabel("Sales number")
plt.show()




## bar chart

products = ["A", "B", "C", "D"]
sales = [450, 300, 600, 400]

plt.bar(products,sales)
plt.title("category wise chart")
plt.xlabel("products")
plt.ylabel("sales")
plt.show()



## histogram

ages = np.array([18,20,21,22,22,23,24,25,25,26,27,30,32,35])

plt.hist(ages, bins=5)
plt.show()


heights = np.random.normal(170,8,1000)

plt.hist(heights, bins=20)
plt.title("Most heights frequency")
plt.xlabel("height in cm")
plt.ylabel("no. of people")
plt.show()




## scatter plot


hours = [1,2,3,4,5,6]
marks = [40,45,55,60,70,80]

plt.scatter(hours, marks)
plt.show()


advertising = [10,20,30,40,50]
sales = [100,150,180,250,300]


plt.scatter(advertising,sales)
plt.title("sales and ad ratio")
plt.xlabel("no. of ads")
plt.ylabel("no. of sales")
plt.show()




months = ["Jan","Feb","Mar","Apr"]
sales = [100,150,130,200]

plt.plot(months, sales)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()


## multiple lines


months = ["Jan","Feb","Mar","Apr"]

sales_2024 = [100,150,130,200]
sales_2025 = [120,170,160,230]

plt.plot(months, sales_2024, label="2024")
plt.plot(months, sales_2025, label="2025")

plt.title("Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()
plt.show()






