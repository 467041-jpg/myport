print("=== โปรแกรมคำนวณพื้นที่สี่เหลี่ยม ===")

while True:
    width = float(input("ความกว้าง: "))
    length = float(input("ความยาว: "))

    area = width * length

    print("พื้นที่ =", area)

    ans = input("คำนวณต่อหรือไม่ (y/n): ")

    if ans == "n":
        break