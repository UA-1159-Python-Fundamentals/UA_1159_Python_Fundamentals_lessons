import qrcode

def generate_qr_code(data):
    qr_code = []

    # Кодування даних у бінарний формат
    binary_data = ''.join(f'{ord(char):08b}' for char in data)

    # Додавання маркерів початку та кінця QR-коду
    encoded_data = '0010' + binary_data + '0000'

    # Розрахунок кількості байтів та розміру QR-коду
    num_bytes = len(encoded_data) // 8
    qr_size = int(num_bytes ** 0.5) + 1

    # Додавання пустого простору для QR-коду
    qr_code = [[0] * qr_size for _ in range(qr_size)]

    # Додавання даних до QR-коду
    current_bit = 0
    for row in range(qr_size):
        for col in range(qr_size):
            if row != qr_size - 1 or col != qr_size - 1:
                if current_bit < len(encoded_data):
                    qr_code[row][col] = int(encoded_data[current_bit])
                    current_bit += 1

    return qr_code

# Функція для виводу QR-коду у консоль
def print_qr_code(qr_code):
    for row in qr_code:
        row_str = ''.join(str(bit) for bit in row)
        row_str = row_str.replace('0', '□').replace('1', '■')
        print(row_str)


data = input("anything: ")
# Генерація QR-коду
qr_code = generate_qr_code(data)

# Виведення QR-коду
print_qr_code(qr_code)

#створення зображення 
img = qrcode.make(data)
img.save('MyQRCode.png')
