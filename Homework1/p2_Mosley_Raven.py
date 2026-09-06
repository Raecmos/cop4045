#Reference: chapters 1-5

def find_pythagorean(n):

   # creates empty list to store triples
   list = []

   # starts a at 1
   a = 1 

   while a <= n: # while a is less than or equal to n

      # starts b at 1
      b = 1

      while b <= n: # while b is less than or equal to n

       # starts c at 1
       c = 1

       while c <= n: # while c is less than or equal to n

        # checks to see pythagorean triple
        if a*a + b*b == c*c:

         # add triple to list
         list.append((a,b,c))

         # increases a, b, and c by 1
         c = c + 1
         b = b + 1
         a = a + 1

       # returns list of triples
       return list

      # asks user for positive integer 
      n_str = input("Enter a positive integer: ")
      n = int(n_str)
      # finds triples
      tuples = find_pythagorean(n)
      # prints each triple
      for triple in tuples:
       print(triple)
      
      
