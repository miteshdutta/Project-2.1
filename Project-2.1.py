Totalterms= int(input("Enter the terms: "))
Term1= 0
Term2= 1
count= 0
if Totalterms<=0:
    print('Enter Positive Number');
elif Totalterms == 1:
   print("Fibonacci sequence upto",Totalterms,":")
   print(Term1)
else:
   print("Fibonacci sequence upto",Totalterms,"terms :")
   while count<Totalterms:
       print(Term1)
       Newterm = Term1 + Term2
       Term1 = Term2
       Term2 = Newterm
       count += 1  
