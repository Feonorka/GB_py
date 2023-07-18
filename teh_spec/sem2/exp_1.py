def decimal_to_hex(num):
    hex_chars = "0123456789ABCDEF"
    hex_str = ""
    if num == 0:
        hex_str = "0"
    else:
        while num > 0:
            remainder = num % 16
            hex_str = hex_chars[remainder] + hex_str
            num = num // 16
    return hex_str

num = int(input("Enter an integer: "))
hex_num = decimal_to_hex(num)
print(f"Hexadecimal representation: {hex_num}")

hex_num = hex(num)
print(f"Hexadecimal representation: {hex_num}")