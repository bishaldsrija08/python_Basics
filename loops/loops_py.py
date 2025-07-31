# # While Loops


# i=0
# while i<=10:
#     print(i)
#     i+=1
# else:
#     print("i is no longer than 10.")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if "cherry" in x:
    break
  print(x)

  for x in "banana":
    if "n" in x:
      break
    print(x)


    for i in range(2,10,2):
      print(i)