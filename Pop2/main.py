rus_letters = "КАМОНВЕРХСТорухаес"
eng_letters = "KAMOHBEPXCTopyxaec"

def start():
    while True:
        choice = int(input("Enter number: 1 - encode, 2 - decode, 3 - quit\n"))

        if choice == 1:
            encode()
        if choice == 2:
            decode()
        if choice == 3:
            break


def encode():
    text = open('text.txt', 'r')
    to_encoded = open('to_encoded.txt', 'r')
    encoded = open('encoded.txt', 'w')


    letter_to_encode = 0
    encoded_bits = 8


    while True:
        symbol_from_text = text.read(1)
        if not symbol_from_text:
            break
        if symbol_from_text in eng_letters:
            if encoded_bits == 8:
                letter_to_encode = to_encoded.read(1)
                if not letter_to_encode:
                    encoded.write(symbol_from_text)
                    break

                print("To encode {0} = {1:b} = {1}".format(letter_to_encode,ord(letter_to_encode))) #:b Запечать аргумент в двоичной системе

                letter_to_encode = ord(letter_to_encode)

                encoded_bits = 0

            bit_from_letter = (letter_to_encode & 0b10000000) >> 7

            print("Read {0}, bit {1}".format(symbol_from_text,bit_from_letter))

            if bit_from_letter:
                symbol_from_text = rus_letters[eng_letters.index(symbol_from_text)] #Русская буква имеет такой же индекс, что и у англ буквы.

            letter_to_encode <<= 1
            letter_to_encode %= 256
            encoded_bits += 1

        encoded.write(symbol_from_text)

    encoded.write(text.read()) # Вернет все оставшиеся символы

    text.close()
    to_encoded.close()
    encoded.close()


def decode():
    encoded = open('encoded.txt', 'r')
    decoded = open('decoded.txt', 'w')

    with open('text.txt','r') as was_encloded:
        to_read = len(was_encloded.read())

    read = 0
    bits_read = 0
    byte = 0


    while read < to_read:
        symbol = encoded.read(1)
        if not symbol:
            break

        if symbol in eng_letters:
            byte <<= 1
            bits_read +=1
            print("Symvol {0}, bit 0, byte {1:b}".format(symbol, byte))
        elif symbol in rus_letters:
            byte <<=1
            byte |= 1
            bits_read += 1
            print("Symvol {0}, bit 1, byte {1:b}".format(symbol, byte))
        if bits_read == 8:
            print("{0}, {0:b}, {0:c}".format(byte))
            decoded.write(chr(byte))
            read += 1
            bits_read = byte = 0


    encoded.close()
    decoded.close()

start()