def sort_sentence(sentence):
    words = sentence.split()
    words.sort()
    return ' '.join(words)

sentence = "this is a sample sentence"
print(sort_sentence(sentence))
