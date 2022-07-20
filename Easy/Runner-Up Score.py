if __name__ == '__main__':
   
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr=list(arr)
    maxV=max(arr)
    
    kontrol=-9999999
    
    for i in range(0,n):
        if arr[i]<maxV and arr[i]>kontrol:
            kontrol = arr[i]
    print(kontrol)
        
   
        
       
    
