def filter_words(st):
    words = st.split()
    return " ".join(words).capitalize()

print(filter_words('This    will    not    pass '))


