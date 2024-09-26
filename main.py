def get_word_count(text):
    return len(text.split())

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()
    
def get_alphabet_count(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_count = {letter: 0 for letter in alphabet}
    for letter in text:
        if letter.lower() in alphabet:
            alphabet_count[letter.lower()] += 1
    return alphabet_count

def main():
    text = read_file("./books/frankenstein.txt")
    word_count = get_word_count(text)
    alphabet_count = get_alphabet_count(text)
    print(f"Word count: {word_count}")
    print("Alphabet count:")
    for letter, count in alphabet_count.items():
        print(f"{letter}: {count}")

main()