#Mohamad Ali Fakhoury Thurs@2pm
def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    temp = str(input())
    fil = open(temp,'r')
    end = open('report.txt','w')
    if temp == "./Problem 3/StudentInfo.tsv":
         end = open('report.txt','w')
    elif temp == "./Problem 3/StudentInfo1.tsv":
         end = open('report1.txt','w')
    else:
         end = open('report2.txt','w')
    x = str(fil.readline())
    cut=''
    lis = []
    nem = []
    grade =[]
    lett = []
    name=[]
    y=0
    cut2=''
    # TODO: Read a file name from the user and read the tsv file here. 
    while x != '':
      cut=cut + x[-9:-1]
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
            lett.append('B')
        elif aver >= 70:
            lett.append('C')
        elif aver >= 60:
           lett.append('D')
        else:
           lett.append('F')
        end.write(f'{name[0]}   {name[1]}   {grade[0]}  {grade[1]}  {grade[2]}  {lett[y]}')
        y=y+1
    end.close
    return

if __name__ == "__main__":
    courseGrade()
    
    