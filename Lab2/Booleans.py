#Booleans 
print(6 > 3)
print(5 == 7)
print(9 < 4)


a = 500
b = 44
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#3
print(bool("Hello"))
print(bool(7))


x = "Hello"
y = 18

print(bool(x))
print(bool(y))


bool("abc")
bool(321)
bool(["apple", "cherry", "banana"])


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  
  x = 200
print(isinstance(x, int))

#Operators
print(4 + 3)

print(50 + 4 * 5)

print(7 + 5 - 4 + 5)

#Lists
thislist = ["ford", "lexus", "kia"]
print(thislist)

list1 = ["orange", "lemon", "pear"]
list2 = [4, 5, 7, 9, 10]
list3 = [True, True, False]

#Tuples
thistuple = ("lemon", "grape", "cherry")
print(thistuple)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Sets
thisset = {"apple", "pear", "kiwi"}
print(thisset)

set1 = {"apple", "banana", "cherry"}
set2 = {2, 4, 5, 9, 3}
set3 = {True, True, False}

thisset = {"pear", "banana", "cherry"}

for x in thisset:
  print(x)

#Dictionaries
thisdict = {
  "brand": "Kia",
  "model": "K5",
  "year": 2020
}

car = {
"brand": "Toyota",
"model": "Camry",
"year": 2018
}

x = car.keys()

print(x) #before the change

#If ... Else 

car["color"] = "white"

print(x) #after the change

