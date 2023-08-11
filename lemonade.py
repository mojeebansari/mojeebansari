week_one=[16,15,3,17,12,13,11]
week_two=[16,20,24,28,27,29]
last_day=int(input('enter the amount of lemonade sell today'))
week_two.insert(7,last_day)
week_one.extend(week_two)
sales=week_one
print(min(sales)*1.5,"the worst profit")
print(max(sales)*1.5, "the best profit")
print(sum(sales)*1.5, "total profit")
