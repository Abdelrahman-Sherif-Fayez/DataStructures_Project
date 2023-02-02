ourlist = []
ourdict = dict()

with open("C:\\Users\Mohamed Gad\\Downloads\\sample.xml","r") as file:
    content = file.readlines()
    for i,x in enumerate(content):

        t_user = x.find("user")
        t_id = x.find("id")
        if ( t_user>=0 and x[t_user-1]!='/' and x[t_user+4]!='s' ):        
           ourlist.append(-1)

        elif(t_id >=0 and x[t_id-1]!='/'and x[t_id+2]=='>' ):
            sub_string = x[t_id : ]
            exact_id = sub_string[sub_string.find(">")+1 :  sub_string.find("<")]
            ourlist.append(int(exact_id))

for i in range(len(ourlist)-2):
    if(ourlist[i]==-1):
        ourdict[ourlist[i+1]] = list()
    else: 
        continue
    j = i + 2 
    while j < len(ourlist) and ourlist[j]!= -1 :
        (ourdict[ourlist[i+1]]).append(ourlist[j])
        j+=1

# print(ourdict)
val_dict = dict()

for lnner_list in ourdict.values():
    for val in lnner_list:
        if val_dict.get(val) is not None:
            val_dict[val] += 1 
        else :
            val_dict[val] = 1

greatest = -1
ans = -6
for key, val in val_dict.items():
    if val_dict[key] > greatest:
        greatest = val_dict[key]
        ans = key
    

print (ans)

    



    
    
        

        

    