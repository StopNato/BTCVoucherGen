import random

print(' ')
print('➖➖➖➖➖➖➖[ BTCVoucherGen ]➖➖➖➖➖➖➖')
print(' ')
print('Генератор ваучеров для @BTC_CHANGE_BOT.')
print('Скрипт написан для канала ❌ ТЕНЕВОЙ БИЗНЕС ❌')
print('Вступить в канал: t.me/shadowbiznes | Наш чат: t.me/shadowbchat')
print(' ')
print('➖➖➖➖➖➖➖[ BTCVoucherGen ]➖➖➖➖➖➖➖')
print(' ')
chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('[❌] Введите желаемое количество ссылок для генерации.'+ "\n")
print(' ')
length = input('[❌] Введите число символов в ваучере (по стандарту 32).'+ "\n")
print(' ')
number = int(number)
length = int(length)
print(' ')
print('[✅] Успешно сгенерировали', number, 'ссылок:')
print(' ')
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print('https://t.me/BTC_CHANGE_BOT?start=b_',password)
