if __name__ == '__main__':
    N = int(input())
    
    degerler=[]
    tutucu=[]
    
    for i in range(N):
        x = input().split()
        degerler.append(x)
        
    for i in range(len(degerler)):
        if degerler[i][0] == 'insert':
            #insert 2 deger alir' deger ve index
            x = int(degerler[i][1])
            y = int(degerler[i][2])
            tutucu.insert(x,y)
            
        elif degerler[i][0] == 'print':
            print(tutucu)
            
        elif degerler[i][0] == 'remove':
            tutucu.remove(int(degerler[i][1]))
            
        elif degerler[i][0] == 'append':
            tutucu.append(int(degerler[i][1]))
      
        elif degerler[i][0] == 'sort':
            tutucu.sort()
            
        elif degerler[i][0] == 'pop':
            tutucu.pop()
            
        elif degerler[i][0] == 'reverse':
            tutucu.reverse()
        
