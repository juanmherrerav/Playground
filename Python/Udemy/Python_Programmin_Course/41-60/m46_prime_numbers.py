def is_prime_number(number):
     for i in range(2, number):
         if number % 2 == 0:
             #print(f'E1 numero {numero} no es primo, {i} es divisor')
             return False
         elif number % number == 0 and number % 1 == 0:
             #print(f'El numero {numero} es primo')
             return True

print(is_prime_number(142))
print(is_prime_number(256))
print(is_prime_number(1303))

is_prime_number = is_prime_number(1983)

if is_prime_number:
    print('E1 numero 1303 es primo')
else:
    print('E1 numero 1303 no es primo')

