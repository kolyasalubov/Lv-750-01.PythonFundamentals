even = []
odd3 = []
other = []

for i in range(1, 11):
    even.append(i) if i % 2 == 0 else \
        odd3.append(i) if i % 3 == 0 \
            else other.append(i)

print(f'Even numbers: {even}',
      f'Odd numbers divisible by 3: {odd3}',
      f'Other numbers {other}', sep='\n\n')

