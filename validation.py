
def mark_errors (lines:str):
 class tag :
   def __init__(self,name,row,column):
     self.name = name
     self.row = row
     self.column = column 
 class mistake :
   def __init__(self,type,row,column,name):
      self.type = type # type maybe absent closed tag (true) or absent opened tag (false)
      self.row = row
      self.column = column
      self.name = name
     
 def top_tag (mylist):
   myList = mylist.copy() #shallow copy
   return myList.pop()

 def add_tag(str,row,column):
   newtag = tag(str,row,column)
   tags.append(newtag)

 def add_mistake(str,row,column,name):
   new_mistake = mistake(str,row,column,name)
   mistakes.append(new_mistake)

 mistakes = []
 tags = []
 row = 0
 while(row < len(lines)): # Here i will iterate for each row
     column = 0 
     columns_no = len(lines[row]) # number of characters in specified line(row)
     while (column < columns_no-1):
         if (lines[row][column] == '<'):
             if(lines[row][column+1] == '/'):
                 column +=2
                 n=lines[row].index(">",column,len(lines[row]))
                 s=tag (lines[row][column:n] ,row,column)# here i stored the closed tag in s
                 if(tags.__len__() !=0): # check if the tag lists doesn't empty
                     if(s.name == top_tag(tags).name): # closed tag matches the opened tag
                         tags.pop() # clear the opened tag from the stack
                     else: # if it enters here , so there is an opening tag that doesn't close
                         is_closed_tag = False
                         tagsCopied = tags.copy() 
                         count = 1
                         while(tagsCopied.__len__() != 0):
                             if (s.name == top_tag(tagsCopied).name): # there exist an opening tag without its closed one
                                 is_closed_tag = True
                                 while (count > 1):
                                     add_mistake(is_closed_tag,top_tag(tags).row,top_tag(tags).column,top_tag(tags).name)
                                     tags.pop()
                                     count=count -1
                                 tags.pop()
                                 break
                             else:
                                 count +=1 
                                 tagsCopied.pop()
                         if(is_closed_tag == False): #that mean there is an absent open tag
                             add_mistake(is_closed_tag,row,column,s.name)
                 else:
                    add_mistake(False,row,s.column-1,s.name)
             else:
                 column +=1
                 n = lines[row].index(">",column,len(lines[row])) 
                 add_tag(lines[row][column:n],row,column)   # adding the openning tag into tags Stack
                 column = n+1
         else:
             column+=1     
     row+=1 
 n = tags.__len__()
 while(n>0):
     add_mistake(True,tags[n-1].row,tags[n-1].column,tags[n-1].name)
     n-=1
 return mistakes

def Correct_Errors(lines:str):
 mistakes=mark_errors(lines)
 if (not mistakes.__len__()):
     print("there are not any errors")
 else:
    i= mistakes.__len__()-1
    while(i>=0):
     if(mistakes[i].type == True): # correction for absent closing tags
         string = "</"+ mistakes[i].name +">\n"
         if(mistakes[i].name == "id" or mistakes[i].name == "name"):
              n = lines[mistakes[i].row].index("\n",mistakes[i].column,len(lines[mistakes[i].row])) 
              lines[mistakes[i].row]=lines[mistakes[i].row][0:n].join(['',string]) #to delete the \n signature
              del mistakes[i] 
         elif(mistakes[i].name == "users"):
            if(lines[len(lines)-1][0]=="\n"):
                 del lines[len(lines)-1]
                 lines[len(lines)-1]=string
            else:
                 lines.insert(len(lines),"\n")
                 lines.insert(len(lines),string)
            del mistakes[i] 
         else:
            temp_row = (mistakes[i].row)+1
            while(temp_row < len(lines)):
             if(lines[temp_row][0]=="\n"):
                 del lines[temp_row]
                 continue
             if(lines[temp_row][mistakes[i].column-1] != " "): #determining where the closed tag must be put
                 lines.insert(temp_row,(mistakes[i].column-1)*" "+string)
                 del mistakes[i] 
                 break
             temp_row+=1
     else: #correction for abset openning tags
          string = "<"+ mistakes[i].name +">"
          if(mistakes[i].name == "id" or mistakes[i].name == "name"):
             str1=lines[mistakes[i].row].lstrip()
             string = string+str1
             del lines[mistakes[i].row]
             counter=0 # to determine where i should put the new line : start column
             while(lines[mistakes[i].row][counter] == " "):
                 counter+=1
             if(mistakes[i].name == "id"):
                 lines.insert(mistakes[i].row,(counter)*" "+string)
             elif(mistakes[i].name == "name"):
                 lines.insert(mistakes[i].row,(counter)*" "+string)
             del mistakes[i]
          elif(mistakes[i].name == "users"):
             if(lines[0][0] != "\n"):
                 string += "\n"
             lines.insert(0,string)
             del mistakes[i]
          else:
             temp_row = (mistakes[i].row)-1
             string +="\n"
             while(temp_row>=0):
                 if(lines[temp_row][0]== "\n"):
                     del lines[temp_row]
                     continue
                 if(lines[temp_row][mistakes[i].column-1] !=" "):
                      lines.insert(temp_row+1,(mistakes[i].column-2)*" " + string)
                      break
                 temp_row-=1
             del mistakes[i]    
     i-=1 
 if (not mistakes.__len__()):
     return lines
     
