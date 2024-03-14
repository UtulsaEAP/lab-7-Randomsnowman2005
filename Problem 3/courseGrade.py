#Mohamad Ali Fakhoury Thurs@2pm
def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    fil = open(f'./Problem 3/{str(input())}','r')
    x = str(fil.readline())
    while x != '':
        cut = x[-1,-10]
        print (cut)
        x = str(fil.readline)
        
      
      
    # TODO: Read a file name from the user and read the tsv file here. 
   
   
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    return

if __name__ == "__main__":
    courseGrade()
    
    