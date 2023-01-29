def validation(path):
 with open (path) as file:
    lines = file.readlines()
    mistakes = []
    tags = []
    row = 0
    class tag :
     def __init__(self,name,row,column):
        self.name = name
        self.row = row
        self.column = column 
    class mistake :
     def __init__(self,expression,row):
        self.expression = expression
        self.row = row
        
    def top_tag (mylist):
     myList = mylist.copy() #shallow copy
     return myList.pop()

    def add_tag(str,row,column):
     newtag = tag(str,row,column)
     tags.append(newtag)

    def add_mistake(str,row):
     new_mistake = mistake(str,row)
     mistakes.append(new_mistake)

    def pop_tag(tag):
        tag.pop()
    while(row < len(lines)): # Here i will iterate for each row
        column = 0 
        columns_no = len(lines[row]) # number of characters in specified line(row)
        while (column < columns_no-1):
            if (lines[row][column] == '<'):
                if(lines[row][column+1] == '/'):
                 column +=2
                 n=lines[row].index(">",column,len(lines[row]))
                 s=tag (lines[row][column:n] ,row,column)# here i stored the closed tag in s
                 column = n+1
                 if(tags.__len__() !=0): # check if the tag lists doesn't empty
                    if(s.name == top_tag(tags).name): # closed tag matches the opened tag
                     tags.pop() # clear the opened tag from the stack
                    else: # if it enters here , so there is an opening tag that doesn't close
                     is_closed_tag = False
                     tagsCopied = tags.copy() 
                     pop_tag(tagsCopied) # remove the top element 
                     while(tagsCopied.__len__() != 0):
                        if (s.name == top_tag(tagsCopied).name): # there exist an opening tag without its closed one
                         is_closed_tag = True
                         temptag = top_tag(tags)
                         tags.pop()    
                         str = "</"+ temptag.name +">\n"
                         temp_row = temptag.row + 1
                         # id the closed tag ID or name 
                         while(temp_row < len(lines)):
                            if(lines[temp_row][temptag.column-1] != " "): #determining where the closed tag must be put
                             lines.insert(temp_row,(temptag.column-1)*" " + str)
                             add_mistake("there is an absent closed tag after line",temp_row)
                             break
                            temp_row+=1
                        tagsCopied.pop()
                    if(is_closed_tag == False): #that mean there is an absent open tag
                        str = "<"+ s.name +">"
                        if(s.name == "id" or s.name == "name"):
                         str1=lines[row].lstrip()
                         str = str+str1
                         del lines[row]
                         lines.insert(row,(top_tag(tags).column +3)*" " + str)
                         add_mistake("there is an absent open tag in line",row)
                         row-=1
                         # print(str)
                        else:
                         temp_row = s.row-1
                         str += "\n"
                         while(temp_row>=0):
                            if(lines[temp_row][s.column-1] !=" "):
                             lines.insert(temp_row+1,(s.column-2)*" " + str)
                             add_mistake("there is an absent open tag in line",temp_row+1)
                             break
                            temp_row-=1
                        row+=1
                else:
                 column +=1
                 n = lines[row].index(">",column,len(lines[row])) 
                 add_tag(lines[row][column:n],row,column)   # adding the openning tag into tags Stack
                 column = n+1
            else:
             column+=1     
        row+=1
 validation_list = [lines,mistakes]
 return validation_list
