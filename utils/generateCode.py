import random


# code contains letters and numbers
def generate_code():
    code = ""
    for i in range(6):
        code += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    return code

