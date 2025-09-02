def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents
  
def count_words(text):
  num_words = len(text.split())
  return num_words

def count_characters(text):
  char_dict = {}

  for char in text:
    char = char.lower()
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1

  return char_dict

def sort_on(letter):
  return letter["count"]

def get_sorted_list_from_dict(dict):
  list_from_dict = [{"value": char, "count": dict[char]} for char in dict]
  list_from_dict.sort(reverse=True, key=sort_on)
  return list_from_dict