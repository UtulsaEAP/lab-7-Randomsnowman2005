#Mohamad Ali Fakhoury Thurs@2pm
def fileNameChange():
    fil = open(str(input()),'r')
    x= str(fil.readline())
    cut=[]
    newl=''
    if x != '':
        while x != '':
            cut = x.split('_')
            newl = str(cut[0]) + '_info.txt'
            print(f'{newl}\n')
            x=fil.readline()
    else:
        fil.close
        return
    fil.close
    return

if __name__ == '__main__':
    fileNameChange()