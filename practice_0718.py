def extract_txt(s):
    number_str = ''.join(c for c in s if c.isdigit() or c == '.')
    if '.' not in number_str:
        number_str += '.00'
    else:
        parts = number_str.split('.')
        integer_part = parts[0]
        decimal_part = parts[1][:2]  # 取小数点后两位
        number_str = f"{integer_part}.{decimal_part}"

    return number_str


# test
print(extract_txt("abc123.456"))  # 输出: 123.45
print(extract_txt("abc123"))  # 输出: 123.00
