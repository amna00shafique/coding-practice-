# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()
# file = open("data.txt", "w")
# file.write("Hello, this is my first file!")
# file.close()
# file = open("data.txt", "a")
# file.write("\nThis line is added later.")
# file.close()
# file = open("data.txt", "r")
# for line in file:
#     print(line)
# file.close()
# file = open("data.txt", "w")
# file.write("Hello, this is my first file!")
# file.close()
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
choice = int(input("Enter your choice:"))
if(choice>=1 and choice<=4):
   print("Enter two numbers")
num1 = int(input())
num2 = int(input ())
if(choice==1):
   res = num1 + num2
   print("Result=",res)
elif(choice==2):
   res = num1 - num2 
   print("Result=",res)
elif(choice==3):
   res = num1 * num2
   print("Result=",res)
elif(choice==4):
   res = num1 / num2
   print("Result=",res)
elif(choice==5):
   exit()
else:
   print("Wrong input....!")