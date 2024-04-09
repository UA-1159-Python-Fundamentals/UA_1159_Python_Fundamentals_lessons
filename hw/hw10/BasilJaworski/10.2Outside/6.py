def class_name_changer(cls, new_name):
    cls.up_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
    cls.low_case = "qwertyuiopasdfghjklzxcvbnm"
    cls.ciphers = "1234567890"
    cls.n = new_name
    cls.lets = True
    cls.noth = False
    cls.first = False
    
    for i in cls.n:
        if i in cls.up_case or i in cls.low_case or i in cls.ciphers:
            pass
        else:
            cls.lets = False
            break
            
    if cls.n == "":
        cls.noth = False
    else:
        cls.noth = True
        
    if cls.n[0] in cls.up_case:
        cls.first = True
    else:
        cls.first = False
        
    if cls.lets and cls.noth and cls.first:
        cls.__name__ = cls.n
    else:
        raise