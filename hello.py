greating =' world'
print(greating)

print( "I","own", "two", "apples", "and", "one","banana" )
print("I","own","two","apples","and","one","banana")
print( "I", "own",2,"apples", "and",1, "banana" )

x = 8
if x > 10:
    print("Big number")
else:
    print("Try again")
    
# x=5
# print( x )

# x = 7 * 9 + 13 # overwrite the previous value of x
# print( x )

# x = "A nod's as good as a wink to a blind bat."
# print( x )

# x = int( 15 / 4 ) - 27
# print( x ) 
# print( 1000000000 )
# print( "hello"+"world" )
# print( 3* "hello" )
# print( "goodbye" *3 )

# num1= 35
# num2= 5
# print("num 1 is" + " num 2 is ", num2)

#Lists
# fruits= ["Apple", "banana","orange"]
# fruits[1]= "Kiwi"
# fruits.append("mango")
# fruits.insert(0,"blueberry")
# fruits.remove("Apple")
# print(fruits)
# print(fruits[2])

print( 15+4 )
print( float( 15+4 ) )




# =========
# ControlFlow
print( "1.", 2 < 5 )

print( "y" in "Python" )
print( "x" in "Python" )
print( "p" in "Python" )
print( "th" in "Python" )
print( "to" in "Python" ) 
print( "y" not in "Python" ) 
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is in the list")
    
  
fruit = "banana"
for n in fruit:
    print( n )
print( "Done" )
    
# fruit = "banana"
# for letter in fruit:
#     print( letter )
#     if letter == "r":
#         fruit = "orange"
# print( "Done" )
    
# for x in range( 10 ):
#     print( x )    
    
# num = 1
# while num <= 5:
#     print( num )
#     num += 1
# print( "Done" )   

fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(i, fruits[i])