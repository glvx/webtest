import sys
import os

def main(arg1="pasbien"):
    print("Hello World!"+arg1)
    os.system('ls -l'++arg1)
    secret="1234"
    password="12345"

if __name__ == "__main__":
    main(sys.argv[1])

print("Guru99")
