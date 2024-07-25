import random

# 1. Create list of 100 random numbers from 0 to 1000
random_numbers = random.sample(range(0, 1001), 100)
print("List of random numbers:", random_numbers)

# 2. Sort list from min to max
for i in range(0, len(random_numbers)):
    for j in range(i + 1, len(random_numbers)):
        if random_numbers[i] >= random_numbers[j]:
            random_numbers[i], random_numbers[j] = random_numbers[j], random_numbers[i]

print("Sorted List:", random_numbers)

# 3. Calculate average for even and odd numbers
even_numbers = []
odd_numbers = []
sum_even = 0
sum_odd = 0
for i in random_numbers:
    mod = i % 2
    if mod == 0:
        even_numbers.append(i)
        sum_even = sum_even + i
    elif mod == 1:
        odd_numbers.append(i)
        sum_odd = sum_odd + i
even_average = sum_even/len(even_numbers)
odd_average = sum_odd/len(odd_numbers)

# 4. Print both average result in console
print("Average of even numbers:", even_average)
print("Average of odd numbers:", odd_average)

