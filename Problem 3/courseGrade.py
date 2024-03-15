#Mohamad Ali Fakhoury Thurs@2pm
def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    temp = str(input())
    fil = open(temp,'r')
    if temp == "./Problem 3/StudentInfo.tsv":
         end = open('./Problem 3/report.txt','w')
    elif temp == "./Problem 3/StudentInfo1.tsv":
         end = open('./Problem 3/report1.txt','w')
    else:
         end = open('./Problem 3/report2.txt','w')
    x = str(fil.readline())
    cut=''
    lis = []
    nem = []
    grade =[]
    lett = []
    name=[]
    y=0
    mid1 = 0
    mid2 = 0
    fina = 0
    cut2=''
    # TODO: Read a file name from the user and read the tsv file here. 
    while x != '':
      cut=cut + x[-9:]
      leg = len(x)
      cut2 = cut2 + x[:leg-9]
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
        end.write(f'{name[0]}\t{name[1]}\t{grade[0]}\t{grade[1]}\t{grade[2]}\t{lett[y]}\n')
        mid1 = mid1 + int(grade[0])
        mid2 = mid2 + int(grade[1])
        fina = fina + int(grade[2])
        y=y+1
    mid1 = mid1/len(lis)
    mid2 = mid2/len(lis)
    fina= fina/len(lis)
    end.write(f'Averages: midterm1 {mid1:.2f}, midterm2 {mid2:.2f}, final {fina:.2f}')
    end.close
    return

if __name__ == "__main__":
    courseGrade()
    
    