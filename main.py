FILE_PATH = "books/frankenstein.txt"

def get_word_count(text):
    return len(text.split())

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()
    
def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    
def get_alphabet_count(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_count = {letter: 0 for letter in alphabet}
    for letter in text:
        if letter.lower() in alphabet:
            alphabet_count[letter.lower()] += 1
    return alphabet_count

def main():
    text = read_file(FILE_PATH)
    word_count = get_word_count(text)
    alphabet_count = get_alphabet_count(text)
    alphabet_count = sort_dict_by_value(alphabet_count)
    print(f"--- Begin report of {FILE_PATH} ---")
    print(f"{word_count} words found in the document.")
    print()
    for letter, count in alphabet_count.items():
        print(f"The '{letter}' character was found {count} times")
    print(f"--- End report ---")

main()