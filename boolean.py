# ftue false

print(id(True))
  
a = 8 
b = 6
c = 7
#rint(a>b)
#rint(c=a)
#int(c=b)

print(bool(12)) 
print(bool(0))
print("srtinglar uchun")
print(bool(""))
print(bool("just"))

word  = input()
if not bool(word.strip()):
      print("Please enter something")
else:
         print("You entered:" , word)