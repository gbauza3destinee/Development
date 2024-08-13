print("I will run from module two ", __name__ )

def main():
    print("I will run from module 1 directly not from module two ", __name__)

if __name__ == "__main__":
    main()