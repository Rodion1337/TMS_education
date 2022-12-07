"""
4* Реализовать кодирование и декодирование ключевых слов для латинского алфавита согласно указанному соответствию (маппингу). 
Шифр (используйте данное соответствие букв при решении задания)
"""




class Crypto():
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    z = "CRYPTOABDEFGHIJKLMNQSUVWXZ"
    s += s.lower()
    z += z.lower()
    encode_str = dict(zip(s, z))
    decode_str = dict(zip(z, s))

    def encode(self, string):
        crypto_encode = ''
        for i in string:
            if i in self.encode_str:
                crypto_encode += self.encode_str[i]
            else:
                crypto_encode += i
        return crypto_encode

    def decode(self, string):
        crypto_decode = ''
        for i in string:
            if i in self.decode_str:
                crypto_decode += self.decode_str[i]
            else:
                crypto_decode += i
        return crypto_decode


crypto = Crypto()
print(crypto.encode('HELLO WORLD'))
print(crypto.encode('Hello world'))

print(crypto.decode('BTGGJ VJMGP'))
print(crypto.decode('Btggj vjmgp'))