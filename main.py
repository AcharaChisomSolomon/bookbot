def main():
    with open("./books/frankenstein.txt", "r") as file:
        text = file.read()
        print(text)

main()