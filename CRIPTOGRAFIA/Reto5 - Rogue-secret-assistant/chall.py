from Crypto.Util.number import getPrime as get_prime
import os


def build_message(secret, e):
    m = f'The secret token is {secret.hex()} and it is encrypted with e = {e}.'.encode()
    return int.from_bytes(m, 'big')

def main():
     # No envíe hkcert22{***REDACTED***}. ¡El indicador real está en el servicio netcat!
    flag = os.environ.get('FLAG', 'hkcert22{***REDACTED***}')

    p, q = [get_prime(1024) for _ in 'pq']
    n = p * q

    secret = os.urandom(64)

    for _ in range(3):
        e = int(input())
        if e == 1: raise Exception('¡Envíame mejores valores!')
        m = build_message(secret, e)
        c = pow(m, e, n)
        print(f'c = {hex(c)}')

    guess = input()
    if secret != bytes.fromhex(guess): raise Exception('¡Secreto incorrecto!')

    print(flag)

if __name__ == '__main__':
    try:
        main()
    except:
        print('Mejor suerte la proxima vez!')