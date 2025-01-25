
  print("b is greater than a")
else:
  print("b is not greater than a")

#3
print(bool("Hello"))
print(bool(7))

#4
x = "Hello"
y = 18

print(bool(x))
print(bool(y))

#5 
bool("abc")
bool(321)
bool(["apple", "cherry", "banana"])

#6 
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#7
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  #8 
  x = 200
print(isinstance(x, int))
