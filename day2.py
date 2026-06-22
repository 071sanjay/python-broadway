a = 10
a = 1.2
a = True
a = None
a = 1
a = "s"
a = 12.2
a = ""
print(type(a))
print(a)


a = ""
a = None

# type casting
a = "hello"
a = "10"

print("before casting", type(a))
a = float(a)
print("after casting", type(a))

a = 12.8
print(isinstance(a, int))


a = 10
b = 11

print(
    a+b,
    a-b,
    a*b,
    a/b,
    a**b,
    a%b,
    a//b
)

a = "testing"
b = "world"
#b = 1

print(a+b)

a = " broadway"
b = 5
print(a*b)

# Operator	Meaning	Example	Result
# ==	Equal to	5 == 5	True
# !=	Not equal to	5 != 3	True
# >	Greater than	7 > 3	True
# <	Less than	2 < 5	True
# >=	Greater than or equal to	6 >= 6	True
# <=	Less than or equal to	4 <= 6	True

age = 20
citizen = True
print(age >= 18 and citizen)  # True

is_weekend = False
is_holiday = True
print(is_weekend or is_holiday)  # True


logged_in = False
print(not logged_in)  # True


if (1==1):
    print("1 is equal")
else:
    print("1 is not equal")
