while True:
    try:
        num1 = int(input("İlk sayıyı girin: "))
        num2 = int(input("İkinci sayıyı girin: "))
        break
    except ValueError:
        print("Geçersiz giriş. Lütfen bir tam sayı girin.")

print("Lütfen yapmak istediğiniz işlemi seçin: ")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

while True:
    choice = input("Seçiminiz (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            result = num1 + num2
            print(num1, "+", num2, "=", result)
        elif choice == '2':
            result = num1 - num2
            print(num1, "-", num2, "=", result)
        elif choice == '3':
            result = num1 * num2
            print(num1, "*", num2, "=", result)
        elif choice == '4':
            if num2 == 0:
                print("Geçersiz giriş. Sıfıra bölme hatası.")
            else:
                result = num1 / num2
                print(num1, "/", num2, "=", result)
        break
    else:
        print("Geçersiz giriş. Lütfen 1, 2, 3 veya 4'ten birini seçin.")

