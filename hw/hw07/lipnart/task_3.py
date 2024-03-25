def calc_char(word):
    d = {}
    for i in word:
        d[i] = word.count(i)
    print(d)

user_word = str(input("Please enter here Your word: ")) 
calc_char(user_word.lower())