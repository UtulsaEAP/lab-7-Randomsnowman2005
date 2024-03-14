#Mohamad Ali Fakhoury Thurs@2pm
def wordInRange():
    file = open('./Problem 2/input1.txt','r')
    min = 'ammoniated'
    max = 'millennium'
    x= file.readline()
    lines = file.readlines()
    for line in lines:
        lin = line.strip('\n')
        if (lin >= min) and (lin <= max):
            print(f'{line.strip()} - in range')
        else:
            print(f'{line.strip()} - not in range') 
    file.close
    return
if __name__ == '__main__':
    wordInRange()