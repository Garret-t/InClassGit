import random
random.seed()

def pass_gen(a):
    password = ''
    for i in range(a):
        password += chr(random.randint(32, 126))
    return password
