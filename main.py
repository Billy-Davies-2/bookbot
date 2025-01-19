def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count_report = word_count(file_contents)
    book_report = unique_character_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print("%i words found in the document" % word_count_report)
    for k, v in book_report.items():
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")

def word_count(str):
    words = str.split()
    return len(words)

def unique_character_count(str):
    unique_character_dict = {}
    for character in str.lower():
        if character in unique_character_dict:
            unique_character_dict[character] += 1
        else:
            unique_character_dict[character] = 1
    return unique_character_dict

if __name__ == "__main__":
    main()