# 1. Find Common Elements in Two Lists
# Use sets to find the intersection (common elements) between two lists.
print("1. Find Common Elements in Two Lists")
def common_elements(a, b):
    result=list(set(a).intersection(b))
    return result

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(common_elements(a, b))



# 2. Remove Duplicates While Preserving Order
# You can use a set to track seen elements and build a new list without duplicates.
print("\n2. Remove Duplicates While Preserving Order")
def remove_duplicates(seq):
    seen=set()
    result=[]
    for number in seq:
        if number not in seen:
            seen.add(number)
            result.append(number)
             
    return result



num = [1, 2, 2, 3, 4,1, 3, 5]
print(remove_duplicates(num)) 


#3. Check if Two Sets are Disjoint (No Common Elements)
# This uses the isdisjoint() method, which returns True if sets have no elements in common.
print("\n3.Check if Two Sets are Disjoint (No Common Elements")
def are_disjoint(set1, set2):
    
    result=set1.isdisjoint(set2)
    return result

a = {1, 2, 3}
b = {4, 5, 6}
print(are_disjoint(a, b))  
c = {3, 4}
print(are_disjoint(a, c))  

