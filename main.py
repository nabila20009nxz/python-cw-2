name = input("what is your name?") 
age = input ("what is your age?")
print (f"My name is {name} and I am {age} years old")
first_number  = int(input ("pick number"))
secound_number = int(input ("pick number") )
operation = input("enter operation ")

if operation == '+' :
    print (first_number + secound_number) 
elif operation == "-":
    print(first_number - secound_number)
elif operation == "*":
    print(first_number*secound_number)
elif operation == "/" : 
    print(first_number/ secound_number) 
else:
    print('operation is invalid')

bus_capacity=50 
inside_bus= int(input("how many people inside the bus" ))
outside_bus = int(input ("how many people out side the bus" ))
empty_seats = bus_capacity- inside_bus
 
if empty_seats>=outside_bus:
    print(f"there are {empty_seats}")
else: 
    print(f"there are no {empty_seats}")
