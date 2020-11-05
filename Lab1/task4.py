import os

# run normally
def part_1(filename):
    f = open(filename, "w")
    text = input("Enter any text: ")
    f.write(text)
    f.close()


# run and change permission
def part_2(filename):
    f = open(filename, "w")
    text = input("Enter any text: ")
    os.chmod(filename, 0o444)
    f.write(text)
    f.close()


# run without permission
def part_3(filename):
    f = open(filename, "w")
    text = input("Enter any text: ")
    os.remove(filename)
    f.write(text)
    f.close()


def main():
    print(" 1. Task 1. \n 2. Task 2. \n 3. Task 3.\n")
    task = int(input(" Input task to run: "))
    filename = "sample.txt"
    if task == 1:
        part_1(filename)
    elif task == 2:
        part_2(filename)
    elif task == 3:
        part_3(filename)


if __name__ == "__main__":
    main()
