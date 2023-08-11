operation = int (input("please select one operation  _1 =  +_  _2 =  -_  _3 = *_  _4 = /_  _5 = change celsius to fahrenheit_  "))
first_number = float(input("please enter first number"))

second_number = float(input("please enter second number"))
if operation == 1:
    print(first_number , "+" , second_number , "is equal to:" ,(first_number+second_number) )
elif operation == 2:
    print(first_number , "-" , second_number , "is equal to:" ,(first_number-second_number) )
elif operation == 3:
    print(first_number , "*" , second_number , "is equal to:" ,(first_number*second_number) )
elif operation == 4:
    print(first_number , "/" , second_number , "is equal to:" ,(first_number/second_number) )
if operation == 5:
    print(first_number , "celsius" , "is equal to:" ,((first_number*9/5)+32), "fahrenheit" )    
else:
    print("wrong operation")