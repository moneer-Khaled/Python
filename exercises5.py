# Exercises 5
# Exercise 1: Accessing Tuple Elements
# Create a tuple with the values ("apple", "banana", "cherry", "date").

# Print the first item.
# Print the last item using a negative index.
# Print the second and third items using slicing.


# Exercise 2: Tuple Operations
# Create two tuples:

# Combine them into a new tuple.
# Multiply tuple1 by 2 and print the result.


# Exercise 3: Tuple Methods & Unpacking Create a tuple with the values (10, 20, 30, 40, 50).

# Use tuple unpacking to assign the first two values to variables a and b, and the rest to a variable rest.
# Print a, b, and the rest.
# Count how many times 20 appears in the tuple.
# Find the index of 40 in the tuple.

#Ex1
t1 = ("apple", "banana", "cherry", "date")
print( t1[0] ) 
print(t1[-1])
print(t1[1:3])

#Ex2
t2 =("city","country","year","day")
t3 =("Den haag","Holland",2025,"Monday")
print(t2+t3)
print(t2*2)


#Ex3
t4=(10,20,30,40,50)
a ,b,*rest = t4

print(a)
print(b)
print(rest)

print(t4.count(20))
print(t4.index(40))


