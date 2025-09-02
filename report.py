from stats import (
  get_book_text, 
  count_words, 
  count_characters,
  get_sorted_list_from_dict
  )

def print_report(file_path):
  text = get_book_text(file_path)
  word_count = count_words(text)
  letters_dict = count_characters(text)
  sorted_letter_count_list = get_sorted_list_from_dict(letters_dict)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file_path}...")
  print("----------- Word Count -----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count --------")

  # print(sorted_letter_count_list)
  for letter in sorted_letter_count_list:
    if letter["value"].isalpha():
      print(f"{letter['value']}: {letter['count']}")

  print("============= END =============")