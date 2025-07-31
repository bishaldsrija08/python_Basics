a= "bishal is a GOOD BOY." 
print(a.upper()) #convert text to upper case
print(a.strip()) # remove white spaces from the starting and begening
print(a.lower()) #convert text to lower case
print(a.replace("GOOD", "BAD"))
print() #returns list
hmm = a.split(" ")

lmm=""
for i in hmm:
    lmm=lmm+" "+i
print(lmm)
print(a.casefold())