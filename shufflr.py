from random import shuffle
import sys
def shuffl(data):
 data = list(data)
 shuffle(data)
 return ''.join(data)

if __name__ == '__main__':
 try:
   info = sys.argv[1]
   print(info)
 except Exception as e:
   info = "JUSTshuffl"
 print(shuffl(info))

