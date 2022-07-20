def swap_case(s):
    kontrol = list(s)
    my_new_list=""
   
    for i in range(len(kontrol)):
        if kontrol[i].isupper():
            my_new_list+=kontrol[i].lower()
        elif kontrol[i].islower():
            my_new_list+=kontrol[i].upper()
        else:
            my_new_list+=s[i]
    return str(my_new_list)
            

