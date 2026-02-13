temperature = [30, 32, 28, 31, 29]

total = 0
for temp in temperature:
    total += temp

average = total /len(temperature)
print("Average temperature:", average)