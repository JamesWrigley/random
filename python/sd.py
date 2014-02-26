#! /usr/bin/python3
import math

# Yes, I know this is awful style
x = [5.2, 5.4, 6.6, 7.2, 7.5, 7.8, 8.1, 8.3, 9.3, 9.6, 10, 10.1, 10.2, 10.3, 10.5, 10.6, 11, 11.2, 11.6, 12.3, 12.5, 12.9, 13.5, 14.2, 17]
y = [6.5, 7.1, 8.4, 9.6, 9.8, 10.4, 10.6, 11, 11, 11.5, 12, 12.2, 12.5, 12.5, 12.7, 12.8, 13.5, 13.6, 13.8, 13.8, 13.8, 14, 14.4, 14.5, 14.5]
list_sum = 0
mean = sum(x) / len(x)

for n in x:
    list_sum += (n - mean) ** 2
print(mean)

standard_deviation = math.sqrt(list_sum / len(x))

print(standard_deviation)
