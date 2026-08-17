import numpy as np

#1 brodcasing

marks=np.array([60,70,80])
print(marks + 10)



salary=np.array([30000,45000,60000])
increment = salary * 10/100
print("with bonus:" ,salary + increment)


prices=np.array([100,250,400,550])
gst = prices * 18/100
print("with gst:" ,prices + gst)



#2 VALIDATION
salary= np.array([76000,87000,98000,56000,93000])
print(np.any(salary>=80000))
print(np.all(salary<=90000))

marks=np.array([45,60,70])
print(np.all(marks>=50))


ages = np.random.randint(10,75,50)
print(ages)
print("are any below 18:", np.any(ages<18))
print("are all people adult:", np.all(ages>=18))




#3 DATA CLEANING
arr =np.array([5,20,150])
print(np.clip(arr,10,100))

arr =np.array([10,np.nan,30,np.nan,50])
print(np.isnan(arr))
print(np.nanmean(arr))


temp = np.random.randint(0,50,100)
print(np.clip(temp,15,40))




#4 vectorization
