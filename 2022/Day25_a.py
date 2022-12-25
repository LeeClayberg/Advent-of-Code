five_bases = [pow(5, i) for i in range(20)]


def snafu_to_decimal(snafu):
    subtotal = 0
    for b, char in enumerate(reversed(list(snafu))):
        if char in ['0', '1', '2']:
            subtotal += int(char) * five_bases[b]
        elif char == '-':
            subtotal -= five_bases[b]
        else:
            subtotal -= 2 * five_bases[b]
    return subtotal


seen = set()


def decimal_to_snafu(decimal):
    snafu = []
    current = decimal
    for base in reversed(five_bases):
        divisor = current // base
        remainder = current % base
        snafu.append(divisor)
        current = remainder
    for i in range(1, len(snafu)+1):
        if snafu[-i] > 4:
            snafu[-i-1] += snafu[-i] // 5
            snafu[-i] = snafu[-i] % 5
        if snafu[-i] == 3:
            snafu[-i-1] += 1
            snafu[-i] = -2
        if snafu[-i] == 4:
            snafu[-i-1] += 1
            snafu[-i] = -1
    while snafu[0] == 0:
        snafu.pop(0)
    text = ''
    for s in snafu:
        text += str(s) if s >= 0 else ('=' if s == -2 else '-')
    return text


total = 0
with open("files/input_25.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        total += snafu_to_decimal(line[:-1])

print(decimal_to_snafu(total))
