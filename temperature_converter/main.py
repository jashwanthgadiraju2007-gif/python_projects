def c_to_f(c):
    F=c*(9/5)+32
    return F
def f_to_c(f):
    C=(f-32)*(5/9)
    return C
def c_to_k(c):
    k=c+273
    return k
def k_to_c(k):
    c=k-273
    return c

def main():
    while True:
        print("Choose conversion:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. exit")
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
           c=int(input("enter temperature in celsius:"))
           print("temperature in fahrenheit is:",c_to_f(c))
        elif choice == 2:
           f=int(input("enter temperature in fahrebheit:"))
           print("temperature in celsius is:",f_to_c(f))
        elif choice ==3 :
           C=int(input("enter temperature in celsius:"))
           print("temperature in kelvin is:",c_to_k(C))
        elif choice==4:
           k=int(input("enter temperature in kelvin:"))
           print("temperature in kelvin is:",k_to_c(k))
        elif choice==5:
           print("exit")
           break
        else:
           print("invalid choice")
main()
