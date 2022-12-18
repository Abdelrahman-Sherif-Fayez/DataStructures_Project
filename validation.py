
with open ("C:\\Users\\aliel\\Desktop\\python\\sample.xml") as file:
     lines = file.readlines()
     mistakes = []
     tags = []
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

     def pop_tag():
        tags.pop()
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
             column = n+1
             if(tags.__sizeof__() > 40): # check if the tag lists doesn't empty
               if(s.name == top_tag(tags).name): # closed tag matches the opened tag
                 tags.pop() # clear the opened tag from the stack
               else: # if it enters here , so there is an opening tag that doesn't close
                 is_closed_tag = False
                 tagsCopied = tags.copy() 
                 tagsCopied.pop() # remove the top element 
                 while(tagsCopied.__sizeof__() > 40):
                   if (s.name == top_tag(tagsCopied).name): # there exist an opening tag without its closed one
                     is_closed_tag = True
                     temptag = top_tag(tags)
                     tags.pop()    
                     temp_row = temptag.row + 1
                     str = "</"+ temptag.name +">\n"
                     while(temp_row < len(lines)):
                       if(lines[temp_row][temptag.column-1] != " "): #determining where the closed tag must be put
                        lines.insert(temp_row,(temptag.column-1)*" " + str)
                        add_mistake("there is an absent closed tag after line",temp_row)
                        break
                       temp_row+=1
                   tagsCopied.pop()
                 if(is_closed_tag == False): #that mean there is an absent open tag
                   temp_row = s.row
                   str = "<"+ s.name +">\n"
                   while(temp_row>=0):
                     if(lines[temp_row][s.column-1] != " "):
                       lines.insert(temp_row-1,(s.column-2)*" " + str)
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


    # l=0
    #  while(l < len(tags)):
    #   print(tags[l].name,tags[l].row , tags[l].column)
    #   l+=1
    #  while(l<len(mistakes)):
    #    print(mistakes[l].expression,mistakes[l].row)
    #    l+=1
    #  print(tags.__sizeof__())
     for line in lines:
      print(line,end=" ")
    #  print(top_tag(tags).row)
        

# # with open("output.txt","w")as file:
# #     file.writelines(lines)

