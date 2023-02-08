import string

def remove_punctuation(input_string):
    # make a translation table
    translator = str.maketrans('', '', string.punctuation)
    # use this table to remove punctuation characters
    return input_string.translate(translator)

input_string = "This is a sample string! How are you?"
print(remove_punctuation(input_string))
