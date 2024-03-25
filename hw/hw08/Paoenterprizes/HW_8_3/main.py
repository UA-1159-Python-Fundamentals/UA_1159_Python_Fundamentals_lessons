import area
print("Радіус чого потрібно найти?\n1. Площа прямокутника\n2. Площа трикутника\n3. Площа кола")
n = input(": ")
match n:
    case "1":
        print("Площа прямокутника: ",area.rec())
    case "2":
        print("Площа трикутника: ",area.trian())
    case "3":
        print("Площа кола: ",area.cir())