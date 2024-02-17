
def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    chars_dict = get_char_dict(text)
    # letters = char_dict_to_sorted_list(text)
    chars_sorted_list = char_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def char_dict_to_sorted_list(letters):
    sorted_list = []
    for letter in letters:
        sorted_list.append({"char": letter, "num": letters[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]


def get_char_dict(text):
    letter_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in letter_count:
            letter_count[lowered] +=1
        else:
            letter_count[lowered] = 1
    return letter_count


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()
