import random
random.seed()

def pass_gen(a):
    password = ''
    for i in range(a):
        password += chr(random.randint(32, 126))
    return password

print(pass_gen(int(input("Password Length: "))))