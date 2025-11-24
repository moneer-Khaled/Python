# #1. Magic 8-ball
import random 


answers = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]



question = input("Ask your quesion?")

print(random.choice(answers))




# 2. FIFO
"""
A first-in-first-out (FIFO) structure, also called a “queue,” is a list that gets new elements added at the end, 
while elements from the front are removed and processed. Write a program that processes a queue. In a loop, 
ask the user for input. If the user just presses the Enter key, the program ends. If the user enters anything else,
except for a single question mark (?), the program considers what the user entered a new element and appends it to the queue. 
If the user enters a single question mark, the program pops the first element from the queue and displays it.
You have to take into account that the user might type a question mark even if the queue is empty.
"""

queue =[]
while True:
    
    user_input = input("Enter something (or ? to process, Enter to quit): ")
    if user_input =="":
        print("program ends")
        break
    
    elif user_input == "?":
        if len(queue)>0:
        
           print("Proccesed" ,queue.pop(0))
        else:
            print("The queue is empty!")
    else:
        queue.append(user_input)
        print(f'Added to the queue:{user_input}')
        print(queue)
        
        

# ===================
# 3. Fibonacci
# Write a Fibonacci sequence using Python.
n = int(input("How many Fibonacci numbers do you want? "))
a, b = 1, 1
print(a)
print(b)
for i in range(n - 2):
    c = a + b
    print(c)
    temp = b
    a = b
    b = c
    




# ===================
         
         
         





# 4. Counting Letters
# Write a program that counts the Number of Characters Occurring in a String. 
# print(counting_number("an","banan")) # 2 

def count_num(sub,text):
    return text.count(sub)

def replace(text):
    result= ""
    
    for char in text:
        if char not in result:
            result+= char
        
    return result
    
print(count_num("app", "apple"))  
print(replace("apple"))





#5.Polindorme
print("5.Polindorme")
    
def is_Polindorme(text):
    text= text.replace(" ","").lower()
    
    if text== text[::-1]:
        return "Yes"
    else:
        return "No"
    
   

print(is_Polindorme("hello"))






# 6. Largest number 
print("6. Largest number ")
def largest_number(numbers):
    largest=numbers[0]
    for n in numbers:
        if n > largest:
            largest= n
    return largest

list =[10,9,20,8,30,7,40,55]

print(largest_number(list))
     