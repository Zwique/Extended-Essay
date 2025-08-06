###---Modular Inverse Function---###

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("The modular inverse does not exist.")
    else:
        return x % m

# Example usage:
e1 = 3
n = 100
inverse = mod_inverse(e1, n)
print(f"The modular inverse of {e1} modulo {n} is {inverse}")
