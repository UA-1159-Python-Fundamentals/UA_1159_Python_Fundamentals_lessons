def filter_words(st):
    sentance = st.split()
    return ' '.join(sentance).capitalize()

print(filter_words('This    will    not    pass '))