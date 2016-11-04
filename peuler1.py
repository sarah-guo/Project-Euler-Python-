number=input("Please enter a whole number: \n")
x=0
for i in range(0,number):
    if i%3==0 or i%5==0:
        x=x+i
print(x)
        
