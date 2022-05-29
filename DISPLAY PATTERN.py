# DISPLAY PATTERN
def displayPattern(n):
    n = eval(input("Enter a number "))

    for i in range(1, n + 1):
        for j in range(n, 0, -1):
            print(j if j <= i else " ", end=" ")
        print()

displayPattern('n')


# DISPLAYING THE LEAP YEAR
'''years_per_line  = 10
count = 0
for year in range(2000, 2100):
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        count += 1
        print(format(year, "5d"), end = '')
        if count % years_per_line == 0:
            print()


# FIND THE NUMBERS DIVISIBLE BY 5 AND 6
numbers_per_line = 10
count = 0
for i in range(100, 1000):
    if i % 5 == 0 and i % 6 == 0:
        count += 1
        print(format(i, "5d"), end=" ")
        if count % numbers_per_line == 0:
            print()'''


# find the num divisible by 5 or 6, but not both
'''for num in range(100, 200):
    if num % 5 == 0 or num % 6 == 0 and not 
(num % 5 == 0 and num % 6 == 0):
        count += 1
        print(format(num, "5d"), end=' ')
        if count % numbers_per_line == 0:
            print()


# FUTURE INVESTMENT VALUE:
def futureInvestmentValue(investmentAmount,
 monthlyInterestRate, years):
    amount = eval(input("The amount Invested: "))
    rate = eval(input("Annual interest rate: "))
    print("Years        Future value ")

    monthlyInterestRate = rate / 1200
    for years in range(1, 31):
        futureInvestmentValue = amount * 
(1 + monthlyInterestRate) ** (years * 12)
        print(years, format(futureInvestmentValue,
 ">20.2f"))


futureInvestmentValue('investmentAmount',
 'monthlyInterestRate','years')










# FIND_FUTURE_DATES
today = eval(input("Enter today's date : "))
numberOfDays = (eval(input("Enter the number of 
days elapsed since today: ")))
if today == 0:
    print("Today is Sunday")
elif today == 1:
    print("Today is Monday")
elif today == 2:
    print("Today is Tuesday")
elif today == 3:
    print("Today is Wednesday")
elif today == 4:
    print("Today is Thursday")
elif today == 5:
    print("Today is Friday")
elif today == 6:
    print("Today is Saturday")
else:
    print("Wrong Entry")

futureDay = (today + numberOfDays) % 7
if futureDay == 0:
    print(" and future day will be Sunday")
elif futureDay == 1:
    print(" and future day will be Monday")
elif futureDay == 2:
    print(" and future day will be Tuesday")
elif futureDay == 3:
    print(" and future day will be Wednesday")
elif futureDay == 4:
    print(" and future day will be Thursday")
elif futureDay == 5:
    print(" and future day will be Friday")
elif futureDay == 6:
    print(" and future day will be Saturday")
else:
    print("Wrong Entry")


# GREATEST COMMON DIVISOR
n1 = eval(input("Enter an integer 1 :"))
n2 = eval(input("enter an integar 2: "))
gcd = 1
k = 2
while k <= n1 and k <= n2:
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
    k += 1
print("The greatest common divisor is ", gcd)


# GCD WITH FUNCTION
def gcd(n1, n2):
    gcd = 1
    k = 2
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1
    return gcd


n1 = eval(input("Enter the first integar: "))
n2 = eval(input("Enter the second integar : "))
print("GCD is ", gcd(n1,n2))'''






