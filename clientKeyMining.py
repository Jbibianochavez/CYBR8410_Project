#!/usr/bin/env python3

import minePassword
import random

def main(loginBlock, acceptanceParam):
    nonce, key = mineClientKey(loginBlock, acceptanceParam)
    print(key.hexdigest())
    
def mineClientKey(loginBlock, param):
    nonce = random.randint(1000000000000, 100000000000000000)
    concat = str(nonce) + loginBlock
    hashVal = minePassword.getHash(concat)
    valid = minePassword.checkValid(param, hashVal.hexdigest())
    
    while(valid == 0):
        nonce = nonce + 1
        concat = str(nonce) + loginBlock
        hashVal = minePassword.getHash(concat)
        valid = minePassword.checkValid(param, hashVal.hexdigest())
    
    return nonce, hashVal
    
if __name__ == "__main__":
    main("", "")
