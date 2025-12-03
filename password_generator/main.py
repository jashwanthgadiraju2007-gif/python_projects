import random
import string
def generate_password(length):
    characters=string.ascii_letters+string.punctuation+string.digits
    password="".join(random.choice(characters) for _ in range(length))
    return password
def main():
 length=int(input("enter a length:"))
 print("generated password : "+generate_password(length))
main()
