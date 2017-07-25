n = int(input("enter the number"))
tem =n
rev = 0
while (n > 0):
dig = n % 10
rev = (rev * 10)+dig
n = n//10
if (temp ==rev):
print(enter the number is palindrome)
else:
print(enter the number is not a palindrome)
