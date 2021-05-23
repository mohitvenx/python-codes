#to find shipping cost for 60 copies where cost of shipping for first copy is 3rs and the rest is 75 paise
org_price = float(input('Enter cover price of 1 book '))
#40% discount for bookstore
disc_price = org_price - (org_price*(40.0/100.0)) 
total_books = float(input('Enter total number of books '))
books_cost = total_books * disc_price
#cost of shipping for first copy is 3rs and for rest is 0.75 rs
ship_cost = 3.0 + ((total_books - 1.0)*(0.75))
total_cost = books_cost + ship_cost
print('The total wholesale cost for', total_books,'is',total_cost)