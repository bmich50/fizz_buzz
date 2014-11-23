limit = 30
print("Fizz buzz counting up to " + str(limit))
num = 0
while num < limit:
  num += 1
  if num % 3 == 0 and num % 5 == 0:
    print("fizbuzz")
    continue
  if num % 3 == 0:
    print("fizz")
    continue
  elif num % 5 == 0:
    print("buzz")
    continue
  else:
    print(num)

   