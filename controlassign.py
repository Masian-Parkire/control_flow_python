#Write a function that uses while, if and continue 
#statements to print all the even numbers between 0 and 50.
def all_even_numbers():
    x=0
    while x<50:
         x+=1
         if x%2!=0:
            continue
         print(x)  
    
#Write a function that takes an integer argument and prints
# "Prime" if the number is prime, and "Not prime" if the number is not prime. 
def number_is_prime(number):
    if number <2:
        print("Not a prime")
    for i in range(2,number):
        if number%i==0:
            print("Not a prime")
        else:
            print("prime")
# number_is_prime(3)
 
#Write a function that takes a list of integers as input and prints 
# the sum of all the even numbers in the list.
def takes_intergers(*nums):
   sum=0
   for i in nums:
      if i %2==0:
         sum+=i
         print(sum)
         
   
  #Write a function that takes any two integers as input,
  # and prints the sum of all the numbers between the two integers
  # (inclusive) that are divisible by 3.
def takes_two_intergers():
   
   sum=0
   for i in range(6,10):
      if i %3==0:
         sum+=i
   print(sum)      


    
      
         
         
                   
                 

