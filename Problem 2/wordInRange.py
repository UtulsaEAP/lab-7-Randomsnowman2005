#Mohamad Ali Fakhoury Thurs@2pm
def wordInRange():
    file = open(str(input()),'r')
    min = str(input())
    max = str(input())
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