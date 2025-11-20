# Write a program that checks if a number is positive, negative, or zero.
x = 99

if x > 0:
    print("Number is positive")
elif x<0:
    print("Number is negative")
else:
    print("Number is zero")

# Use a for loop to print numbers from 1 to 10.
for x in range( 10 ):
    print( x )
# Use a while loop to print numbers from 10 down to 1.
x =10
while x>=1:
    print(x)
    x-=1
print("Done")
# Write a program that prints all even numbers from 1 to 20 using range().
for num in range(1,21):
    if num %2 ==0:
        print(num)
        
# Ask the user for a number. If it’s greater than 100, print "Big number!", otherwise print "Small number!".
y = 9
if y >100:
    print("Big number!")
else:
    print("Small number!")
