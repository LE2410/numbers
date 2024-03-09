three_different_numbers = input("Provide 3 different whole numbers each followed by a space ") #three different numbers is type string
print("Numbers entered: " , three_different_numbers) 

assign_numbers = three_different_numbers.split (" ") #assign_numbers has taken a string and split it into list of string type 

first = assign_numbers [0] #string
second = assign_numbers[1] #string
third = assign_numbers [2] #string

a = int(first)  #convert the above string into integer i.e whole values 
b = int(second)
c = int(third)

sum_numbers=  (a + b + c)
print("Sum of numbers entered:" , sum_numbers)

first_minus_second = (a - b)
print("The first number minus the second number:" , first_minus_second)

third_by_first = (c*a)
print("The third number times the first number:" , third_by_first)

sum_and_divide =  (sum_numbers / c)
print("The sum of numbers dived by the last number entered:" , sum_and_divide)

