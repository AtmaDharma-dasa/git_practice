print("hello world")

def add(num1,num2):
   return num1+num2

x = int(input("Enter num1:  "))
y = int(input("Enter num12:  "))

result = add(x,y)
print_result = input("Do you want to print the result? (Y/N): ")

# Conditionally print the result
if print_result.lower() == "y":
    print(result)
    print("working")

else: print("not working")