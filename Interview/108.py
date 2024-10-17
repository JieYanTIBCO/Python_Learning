# numbers = range(1,1000)

# primes_numbers = filter(lambda x: x%i == 0 for i in range(2,999) , numbers)
# primes_numbers = filter(lambda x: any(x % i == 0 for i in range(2, 1000)), numbers)

# print(list(even_numbers))


nums = list(range(1, 1000))


primes = list(filter(lambda num: all(num % x != 0 for x in range(2, num)), nums))

print(primes)
