def format_dictionary(file_path):
    with open(file_path, 'r') as f:
        words = [word.strip() for word in f.readlines()]
        formatted_words = "['" + "', '".join(words) + "']"
        return formatted_words

file_path = input("Enter the dictionary file path: ")
print(format_dictionary(file_path))
