from PIL import Image
import stepic
import json

def decrypt(key2,message):
    flipped = {v: k for k, v in key2.items()}
    return ''.join(flipped[l] for l in message)

def decrypted_message(path,message):
    im2=Image.open(path)
    s=stepic.decode(im2)
    key3=s.decode()
    key2=json.loads(key3)
    return decrypt(key2,message)
