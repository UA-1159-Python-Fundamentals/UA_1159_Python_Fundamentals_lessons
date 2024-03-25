"""Reversing Words in a String"""
def reverse(st):
    list_st = st.split()
    list_st.reverse()
    return " ".join(list_st)