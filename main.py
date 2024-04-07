def factorize(n):
    for p in range(2, n):
        if n % p == 0:
            return p, n // p
    return None, None


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        b_div_a, b_mod_a = divmod(b, a)
        g, x, y = egcd(b_mod_a, a)
        return g, y - b_div_a * x, x


def modular_inverse(e, phi_n):
    g, x, _ = egcd(e, phi_n)
    if g != 1:
        raise Exception('gcd(e, phi_n) != 1')
    return x % phi_n


def decode(private_key, C):
    d, n = private_key
    text = ''
    for num in C:
        text += str(pow(num, d, n))
    bytes_arr = [int(text[i:i + 2]) for i in range(0, len(text), 2)]
    # print(["{0:b}".format(b) for b in bytes_arr])
    return bytes(bytes_arr).decode('ascii')


def split_C(C, n):
    chunk_size = len(str(n))
    number_str = str(C)
    chunks = [int(number_str[i:i + chunk_size]) for i in range(0, len(number_str), chunk_size)]
    return chunks


n = 471090785117207
e = 12377
C = split_C(314999112281065205361706341517321987491098667, n)

p, q = factorize(n)
print(f"Простые множители числа {n}: p = {p}, q = {q}")

phi_n = (p - 1) * (q - 1)
print(f"Функция Эйлера (p, q) = {phi_n}")

d = modular_inverse(e, phi_n)
print(f"Обратное по модулю phi_n числу e число d = {d}")
print(f"Закрытый ключ: {d, n}")

print(f"Раскодированное сообщение: {decode((d, n), C)}")
