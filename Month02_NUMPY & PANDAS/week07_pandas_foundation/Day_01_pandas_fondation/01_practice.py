import pandas as pd

# Series

marks = pd.Series([99,87,60,50,92])
print(marks)


names = pd.Series(["Omkar", "Rahul", "Priya", "Amit"])
print("first name:", names[0])
print("last name:", names[3])


temp = pd.Series([30,32,27,45,21,52,18])
print("max:", temp.max())
print("min:", temp.min())
print("average:", temp.mean())




#dataframe

people = pd.DataFrame({   "Names" : ["omkar", "padmaj", "babu", "pranav"],
                          "Age" : [21,16,17,19],
                          "City" : ["pune", "gujrat", "mumbai", "bihar"]
                          },
                          index =["s1", "s2", "s3", "s4"])

print(people)


employess = pd.DataFrame({
    "name" : ["govind", "himanshu", "jayesh", "kunal", "rounit", "auyush"],
    "age" : [21,32,23,26,33,24],
    "salary(lpa)" : [6,4,7,8,4,5],
    "department" : ["account", "frontend","mangerial","backend","computer","budget"],
    "experince(years)" : [1,6,2,1,9,3]
})



#incpecting dataset
print(employess)
print(employess.head(3))
print(employess.tail(2))
print(employess.shape)




