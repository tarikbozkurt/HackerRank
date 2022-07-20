"""def minion_game_Game_Rule_Solution(string):
    # your code goes here
    my_key = 'BANANA'
    len_string = len(string)
    count=0
    for i in range(0,len(my_key)):
        if string.upper() in my_key[i:len_string]:
            len_string +=1
            count +=1
        else:
            len_string += 1

    a ="Stuart"
    return "Stuart {}".format(count)
"""
def minion_game(string):
    vowels = 'AEIOU'
    Stuart_score, Kevin_score = 0, 0
    length = len(string)
    for start_idx in range(length):
        score = length - start_idx
        if string[start_idx] in vowels:
            Kevin_score += score
        else:
            Stuart_score += score
    if Stuart_score == Kevin_score:
        print('Draw')
    if Stuart_score > Kevin_score:
        print('Stuart {}'.format(Stuart_score))
    if Stuart_score < Kevin_score:
        print('Kevin {}'.format(Kevin_score))
        
