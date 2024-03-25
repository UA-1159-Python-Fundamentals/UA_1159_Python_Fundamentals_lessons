def number_of_char(strng:str):
    count_dict = {}
    for i in range(len(strng)):
        if strng[i] in count_dict.keys():
            count_dict[strng[i]] += 1
        elif strng[i] not in count_dict.keys():
            count_dict[strng[i]] = 1
    return count_dict