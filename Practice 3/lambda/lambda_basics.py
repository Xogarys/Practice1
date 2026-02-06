x = lambda a : a + 10  #Add 10 to argument a
print(x(5))

x = lambda a, b : a * b  #Multiply argument a with argument b
print(x(5, 6))


#you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))



def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))