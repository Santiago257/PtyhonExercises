#Ask to the user the number of hours worked and the cost per hour
#We need to cast the result to make the operation
hours =float(input("Hours worked "))
cost = float(input("Cost per hour "))

pay = hours * cost

print(pay)