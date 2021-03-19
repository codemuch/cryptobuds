import binascii
import base64

if __name__ == '__main__':
  hexstr = '1c0111001f010100061a024b53535009181c'
  xorkey = '686974207468652062756c6c277320657965'

  res = bytes(a ^ b for (a, b) in zip(binascii.unhexlify(hexstr), binascii.unhexlify(xorkey)))
  print(binascii.hexlify(res).decode('utf-8'))
