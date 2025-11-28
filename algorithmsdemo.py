"""
1- Create a fumntion that takes array as an araguemnt 
2- Check if teh array not empty, if yes return the array is empty
3- Save the last index in a new variable
4- remove the last Index
5-insert the new variable in the first Index
6- return the array and print it 



"""
print("\nA1")
def shift_array(arr):
    if len(arr)==0:
        return "The array is empty"
    
    last_number=arr[-1]
    arr.pop()
    arr.insert(0,last_number)
    return arr
print(shift_array([2,1,6,4,-7]))



"""
Q2
1-Create a function that takes an array as an argument
2-Check if the array is not empty
3-Check if the index is smaller than 0, remove it
4-retrun the rest of the elements

    
    
    
    
    """
print("\nA2")
def negative_array(arr):
    if len(arr)==0:
        return "The list is empty"
    for i in arr:
        if i < 0:
            arr.remove(i)
            
    else:
        return arr
            
print(negative_array([1,-2,1,-3]))



"""
Q3
1-Create a function that takes a text as an argument
2-Check if the list is not empty
3-split the text into a list of words
4-initalize the first index as the largest one
5-using for loop to find the largest word between the first index and the rest
6-return the largest word and print it
"""

print("\nA3")
def longest_word(text):
    if len(text)==0:
        return "The list is empty"
    words=text.split()
    longest=words[0]
    for word in range(1,len(words)):
        if len(words[word]) > len(longest):
            longest=words[word]
    return longest

text=("The quick brown fox jumped over the lazy dog")
print(longest_word(text))



"""
Q4
1-Create a that takes array as an argument
2-Create a new empty variable for the result
3-loop over each sub-array
4-initalize the first element as the largest one
5-use for loop to compare with the rest
6-Using if statement if the number is larger,append it to the new variable
7-return the new variable and print it
"""


print("\n4")
def largest_number(arr):
    result=[]
    for sub in  arr:
        largest=sub[0]
        
        for num in sub[1:]:
            if num > largest:
                largest=num
        
        result.append(largest)
    return result
    
print(largest_number([[13, 27, 18, 26],
                      [32, 35, 37, 39],
                      [1000, 1001, 857, 1]]))



""" 
Q5
1-Create a fuction  that takes text as an argument
2-Split the text into a list of words
3-Create a new varaible for the new text
4-for loop for each word to capitalize the first letter
5-append the each word into the the result variable
6-rejoin the letter to the text
7-return the result

"""
print("\nA5")

def title_case(text):
    words=text.split()
    result=[]
    for word in words:
        result.append(word[0].upper() + word[1:].lower() )

        
    return " ".join(result)
  
print(title_case("i'm a little tea pot")  )