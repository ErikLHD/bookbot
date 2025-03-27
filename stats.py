def count_words(file_contents):
    word_list = file_contents.split()
    count = 0
    for word in word_list:
        count += 1
    return count

def char_count(file_contents):
    char_c = {}
    for word in file_contents:
        for char in word.lower():
            if not (char.isalpha()):
                pass
            elif char not in char_c:
                char_c[char] = 1
            else:
                char_c[char] += 1


    return char_c
