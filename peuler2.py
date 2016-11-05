x=1
y=2
sum=y
z=x
while z<4000000:
    if z<4000000:
        print(z)
        z=y+x
        x=y
        y=z
        if z%2==0:
            sum=sum+z
print("The total of all even fibonacci numbers is: %d " % sum )
        
    
