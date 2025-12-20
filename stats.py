def count_words(text):
    words = text.split()
    return print(f"Found {len(words)} total words")

def lower_character(text):
    dict = {}

    for letter in text:
        letter = str.lower(letter)
        if letter in dict:
            # Do add the value of the key + 1
            dict[letter] = dict[letter] + 1
        else:
            # add letter to dict
            dict[letter] = 1
    return dict

    # values = 
    # for letter in text:
    #     #add to dict
    #     lower = str.lower(text)
    #     return lower
    #     #integer of that  