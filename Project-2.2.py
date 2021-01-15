list1 = []
list2 = [] 

n1 = int(input("Enter number of elements in list1 : ")) 

print('Enter terms in list1: \n')

for i in range(0, n1): 
    element = int(input()) 
    list1.append(element) 

print("list1 =",list1)

for num in list1: 
    if num >= 0: 
       print(num, end = " ")
print('\n')
       

n2 = int(input("Enter number of elements in list2 : ")) 

print('Enter terms in list2: \n')

for i in range(0, n2): 
    element = int(input()) 
    list2.append(element)

print("list2 =",list2)

for num in list2: 
    if num >= 0: 
       print(num, end = " ")
       
