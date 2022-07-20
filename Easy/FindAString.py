def count_substring(string, sub_string):
    count=0
    sinir = len(sub_string)
    j=0
    for i in range (0,len(string)):
        
        if string[i:sinir+j] == sub_string:
            count+=1
            j+=1
        else:
            j+=1
    return count