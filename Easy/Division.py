if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    divisionIntegerValues = a//b
    divisionFloatValues = a/b
    
    myValues = [divisionIntegerValues,divisionFloatValues]
    
    for element in myValues:
        print(element)
    
    