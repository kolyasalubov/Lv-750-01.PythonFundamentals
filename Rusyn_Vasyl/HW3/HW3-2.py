number = input("Уведіть число?")

number_len = len(number)
count = 1
for i in range(number_len):
    count *= int(number[i])

reverce_number = number[::-1]

sorted_number = "".join(sorted(number))

print('Уведене вами число - {} : , добуток його цифр - {}, обернене число'
      ' - {} , а також впорядковане - {}'.format(number, count, reverce_number, sorted_number))

