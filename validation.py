
def mark_errors (lines:str):
 class tag :
   def __init__(self,name,row,column):
     self.name = name
     self.row = row
     self.column = column 
 class mistake :
   def __init__(self,type,row,column):
      self.type = type # type maybe absent closed tag (true) or absent opened tag (false)
      self.row = row
      self.column = column
     
 def top_tag (mylist):
   myList = mylist.copy() #shallow copy
   return myList.pop()

 def add_tag(str,row,column):
   newtag = tag(str,row,column)
   tags.append(newtag)

 def add_mistake(str,row,column):
   new_mistake = mistake(str,row,column)
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
                                     add_mistake(is_closed_tag,top_tag(tags).row,top_tag(tags).column)
                                     tags.pop()
                                     count=count -1
                                 tags.pop()
                                 break
                             else:
                                 count +=1 
                                 tagsCopied.pop()
                         if(is_closed_tag == False): #that mean there is an absent open tag
                             add_mistake(is_closed_tag,row,column)
                 else:
                    add_mistake(False,row,s.column-1)
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
     add_mistake(True,tags[n-1].row,tags[n-1].column)
     n-=1
 return mistakes
