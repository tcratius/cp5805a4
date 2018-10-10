
# coding: utf-8

# In[9]:


from collections import Counter

def Display_Main_Menu():
    print("""\nWelcome to The Smart Statistician!\n
Please choose from the following options:\n
     1 – Load data from a file
     2 – Display the data to the screen
     3 – Rename a set
     4 – Sort a set
     5 – Analyse a set
     6 - Quit
    """)


def Display_Contents_As_Stats(multiSets):
    for num, val in enumerate(multiSets.values()):
        val.sort()
        print(list(multiSets.keys())[num])
        print("-" * 10)
        numofVals = "Number of values (n)"
        print("{}: {:d}".format(numofVals, len(val)))
        print("{:>10s}: {:.0f}".format("Min", val[0]))
        print("{:>10s}: {:.0f}".format("Max", val[-1]))
        resultMedian = Get_Median(val)
        print("{:>12s}: {:.1f}".format("Median", resultMedian))
        resultMode = Get_Mode(val)
        print("{:>11s}: {:.1f}".format("Mode", resultMode))
        print("-" * 10)
        
def Change_Contents_Str_To_Int(multiSets):
    dictofInts = {}
    newList = []          
    for number, val in enumerate(multiSets.values()):
        name = list(multiSets.keys())[number]
        for item in val[0:]:
            newList.append(float(item))
        
        dictofInts[name] = newList 
        newList = []
       
    return dictofInts

def Display_File_Contents(multiSets):
    print("\n")
    for num, val in enumerate(multiSets):
        print(val)
        print(list(multiSets.values())[num])
        print("-"*10)
    
def Display_Header_Option(multiSets, constant):
    print("\nWhich set do you want to {}?".format(constant))
    for num in range(len(multiSets)):
        print("{:5d}".format(num+1) + "-" + list(multiSets.keys())[num])

def Do_Rename(multiSets):
    constant = "Re-name" 
    rename = ""
    dictKeys = []
    Display_Header_Option(multiSets, constant)
    
    for k, v in multiSets.items(): # make a list of dict names already used.
        dictKeys.append(k)
      
    number = Get_Integer("Select the set to rename (Enter {}-{}): ".format(1, len(multiSets)))
    while number not in range(1, len(multiSets)+1):
        number = Get_Integer("Select the set to rename (Enter {}-{}): ".format(1, len(multiSets)))
    number -= 1
    
    rename = Get_String("Enter new name: ")    
    while rename == "" and (rename in dictKeys):
        print("The name can not be an empty str '' or a name that has already been used")
        rename = Get_String("Enter new name: ")
    
    oldName = list(multiSets.keys())[number]
    multiSets[rename] = multiSets.pop(oldName)
    print("{} renamed to {}".format(oldName, rename))
       
    return dictKeys

def Do_Sort_Sets(multiSets):
    constant = "Sort"
    Display_Header_Option(multiSets, constant)
    
    number = Get_Integer("Select the set of values to sort (Enter {}-{}): ".format(1, len(multiSets)))
    while number not in range(1, len(multiSets)+1):
        number = Get_Integer("Select the set of values to sort (Enter {}-{}): ".format(1, len(multiSets)))
    number -= 1
    
    sortName = list(multiSets.keys())[number]
    
    print("The set {} before sorting {} ".format(sortName, multiSets[sortName]))
    multiSets[sortName].sort()
    print("\tand then after {}".format(multiSets[sortName]))

def Get_File_Name():
    dictFile = {}
    dictToInts = {}
    fileName = Get_String("Please enter file name you wish to open: ")
    try:   
        fileOpen = open(fileName, "r")
        data = fileOpen.read().splitlines()
        for line in data:
            getLine = line.split(',')
            dictFile[getLine[0]] = getLine[1:]         
        
        dictToInts = Change_Contents_Str_To_Int(dictFile)
        print("File name {} was successufully loaded".format(fileName))
                
    except FileNotFoundError:
        print("No such file found or not located in current directory")
        
    return dictToInts, fileName
                              
def Get_Integer(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError: 
        print("The value was str not int")
        return 0
    except:
        print("The input cannot be a number")
        return 0                      

def Get_Median(singleSet):
    countSet = len(singleSet)
    if (countSet % 2) == 0:
        addLeft = singleSet[int((countSet / 2) - 1)]
        addRight = singleSet[int(countSet / 2)]
        result = (addLeft + addRight) / 2
        return result
    else:
        countSet -= 1
        return(singleSet[int(countSet / 2)]) 

def Get_Mode(singleSet):
    modeList = Counter(singleSet)
    result = list(modeList.most_common(1))
    mode, *rest = result.pop()
    return mode

def Get_String(prompt):
    try: 
        value = input(prompt)
        return value
    except ValueError: 
        print("Str required, cannot be of type int")
        return ""
    except:
        print("The input cannot be a string")
        return ""
                              
def main():
    fileName = None
    multiSets = {}
    dictNames = []
    number = 0
       
    while number != 6:
        Display_Main_Menu()
        number = Get_Integer("Enter the option you wish to perform: ")
        if number == 1:
            multiSets, fileName = Get_File_Name()
        elif number == 2 and fileName != None:
            Display_File_Contents(multiSets)
        elif number == 3 and fileName != None:
            dictNames = Do_Rename(multiSets)
        elif number == 4 and fileName != None:
            Do_Sort_Sets(multiSets)
        elif number == 5 and fileName != None:
            Display_Contents_As_Stats(multiSets)
        elif number == 6:
            print("\nGood bye! Thanks for using 'The Smart Statistician'. ")
        else:
            print("\nERROR: Not file opened and loaded into Smart Statistician")
            print("<Enter> option '1' to load a file or '6' to exit.\n")
        
            
        

main()


# In[2]:


import random
number = []
for x in range(6):
    number.append(random.randint(0,100))
print(number)


# In[3]:


{'Rainfall': ['35', '23', '12', '65', '34', '111', '54', '23', '68', '97'],
                 'Age': ['35', '23', '14', '76'], 
                 'Odometer Reading': ['35065', '67443', '23545', '12323', '72335']}


# In[4]:


#The list of lists
list_of_lists = [range(4), range(7)]

#flatten the lists
flattened_list = [y for x in list_of_lists for y in x]
flattened_list


# In[5]:


range(6)

