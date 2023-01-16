# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def main():
    text = 'пра прАБВ огнр длорпАБВовгв зщзыфшвщ вфыыАБВгыоы АБВывовдлыф'
    text = list(filter(lambda el: 'абв' not in el.lower(), text.split()))
    print(' '.join(text))


if __name__ == '__main__':
    main()
