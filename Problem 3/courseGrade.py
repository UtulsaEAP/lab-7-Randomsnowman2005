#Mohamad Ali Fakhoury Thurs@2pm
def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    fil = open(f'./Problem 3/{str(input())}','r')
    end = open('report.txt','w')
    x = str(fil.readline())
    cut=''
    lis = []
    nem = []
    grade =[]
    lett = ''
    name=[]
    y=0
    cut2=''
    # TODO: Read a file name from the user and read the tsv file here. 
    while x != '':
      cut=cut + x[-10:-1]
      leg = len(x)
      cut2 = cut2 + x[:leg-10]
      lis.append(cut.split(  ))
      nem.append(cut2.split())
      x = str(fil.readline())
      cut=''
      cut2=''
    fil.close
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    while y < len(lis):
        grade = lis[y]
        name = nem[y]
        aver = (int(grade[0]) + int(grade[1]) + int(grade[2]))/3
        if aver >= 90:
            lett.append('A')
        elif aver>= 80:
            lett ='B'
        elif aver >= 70:
            lett = 'C'
        elif aver >= 60:
           lett = 'D'
        else:
           lett = 'F'
        print(f'{name[0]}   {name[1]}   {grade[0]}  {grade[1]}  {grade[2]}  {lett}')
        y=y+1
    end.close
    return

if __name__ == "__main__":
    courseGrade()
    
    