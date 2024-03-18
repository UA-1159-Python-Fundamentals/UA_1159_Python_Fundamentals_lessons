def filter_words(st):
    st = st.capitalize()
    s = st.split()
    return " ".join(s)
print(filter_words('WOW this is REALLY          amazing'))


# st.split()