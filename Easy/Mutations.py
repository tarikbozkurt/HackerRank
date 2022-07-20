def mutate_string(string, position, character):
    
    s=string
    new_list= list(s)

    new_list[position] = character
    
    my_str =''.join(new_list)
    
    
    return my_str