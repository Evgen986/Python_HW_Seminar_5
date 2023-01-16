# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример: WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWA
#         9W3B24W1B14W


def main():
    text = 'WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWA'
    print(f'Оригинальный текст - {text}')
    symbol = text[0]
    rle_text = list()
    counter = 1
    for index in range(1, len(text)):
        if text[index] != symbol:
            rle_text.append(counter)
            rle_text.append(symbol)
            symbol = text[index]
            counter = 1
        else:
            counter += 1
        if index == len(text)-1:
            rle_text.append(counter)
            rle_text.append(symbol)
    print('RLE = ', end='')
    print(*rle_text, sep='')
    text = ''
    for index in range(0, len(rle_text), 2):
        text += rle_text[index+1]*rle_text[index]
    print(f'decoding = {text}')


if __name__ == '__main__':
    main()