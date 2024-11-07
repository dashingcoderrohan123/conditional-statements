#Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?

y=float(input("Enter your selling price"))
f=float(input("Enter your cost price"))
profit=y-f
if y>f:
    
    print("you got a profit of ", profit)

else:
    print("you're in a loss")