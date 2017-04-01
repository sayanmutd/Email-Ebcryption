import random
from PIL import Image
import stepic
import json

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
        'abcdefghijklmnopqrstuvwxyz' + \
        '0123456789' + \
        '~:.;,?!@#$%&()+=-*/_<> []{}`~^"\'\\'

#content = 'This is a demo mail'
encrypted=""

def generate_key():
    shuffled = sorted(chars, key=lambda k: random.random())
    return dict(zip(chars, shuffled))

def encrypt(key, content):
    return ''.join(key[l] for l in content)

def encryptIT(content,path):
    global encrypted
    key = generate_key()
    encrypted = encrypt(key, content)
    keystr=json.dumps(key)
    im=Image.open(path)
    im1=stepic.encode(im,keystr)
    im1.save('output.png','PNG')

