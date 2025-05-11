def main():
    try:
        num = int(input("Enter a number: "))
        for _ in range(num):
            print("*", end=" ")
        
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
