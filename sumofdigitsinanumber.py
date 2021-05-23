num = 1234                                          #enter the 4 digit number
num1 = num//1000                                    #divide number with 1000 to find thousandth's digit
x1 = (num - num1*1000)//100                         #to find hundredth's digit
x2 = (num - (num1*1000 + x1*100))//10               #to find tenth's digit
x3 = (num - (num1*1000 + x1*100 + x2*10))           #to find one's digit
sum = x1 + x2 + x3 + num1                           #sum of all digits of number
print(num1)
print(x1)
print(x2)
print(x3)
print(sum)