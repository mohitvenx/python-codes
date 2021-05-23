years = float(input('Enter the number of years loan is taken for: '))   #To read the time loan taken for
amount = float(input('Enter the loan amount: '))                        #To read the amount taken as loan
interest = float(input('Enter the interest rate for the loan: '))       #To read the rate at which loan is taken
si = float((amount*years*interest)/100)                                 #calculating simple interest
print('the simple interest for the amount taken for', years, 'years is', si)  #printing the simple interest