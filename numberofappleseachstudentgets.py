#To find number of apples each student will get and how many remain in the basket
N = int(input('Number of students present:'))
K = int(input('Number of apples present in basket'))
print('Number of apples each student gets ', K//N)    #integer division and it shows how many will remain basket
print('Number of apples left in basket is ', K % N)  #remainder calculation
                                                     # it tells the number of apples each student gets
