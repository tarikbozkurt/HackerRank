if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    my_tuple = list(integer_list)
    tut=[]
    
    
    #listem [ 1,2,3,4,5,6,7,8] gibi..
    for i in range(n):
        tut.append(my_tuple[i])
        
    
 

    print(hash(tuple(tut)))
