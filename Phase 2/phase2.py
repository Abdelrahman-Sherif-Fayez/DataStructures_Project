def getlist(path):
    with open(path) as file:
        content = file.readlines()
        ourlist = []
        for i,x in enumerate(content):
            t_user = x.find("user")
            t_id = x.find("id")
            if ( t_user>=0 and x[t_user-1]!='/' and x[t_user+4]!='s' ):        
                ourlist.append(-1)

            elif(t_id >=0 and x[t_id-1]!='/'and x[t_id+2]=='>' ):
                sub_string = x[t_id : ]
                exact_id = sub_string[sub_string.find(">")+1 :  sub_string.find("<")]
                ourlist.append(int(exact_id))
    return ourlist

def users_dictionary(ourlist):
    ourdict = dict()
    for i in range(len(ourlist)-2):
        if(ourlist[i]==-1):
            ourdict[ourlist[i+1]] = list()
        else: 
            continue
        j = i + 2 
        while j < len(ourlist) and ourlist[j]!= -1 :
            (ourdict[ourlist[i+1]]).append(ourlist[j])
            j+=1
    return ourdict

def most_influencer_user(ourdict):
    val_dict = dict()
    for inner_list in ourdict.values():
        for val in inner_list:
            if val_dict.get(val) is not None:
                val_dict[val] += 1 
            else :
                val_dict[val] = 1

    greatest = -1
    mostInfluencerId = -6
    for key, val in val_dict.items():
        if val_dict[key] > greatest:
            greatest = val_dict[key]
            mostInfluencerId = key
        
    return mostInfluencerId

def most_active_user(ourdict):
    #Dictionary to know list length for each user 
    val_dict = dict()
    for id, inner_list in ourdict.items():
        val_dict[id] = len(inner_list)

    greatest = -1
    mostActiveId = -6
    for key, val in val_dict.items():
        if val_dict[key] > greatest:
            greatest = val_dict[key]
            mostActiveId = key
        
    return mostActiveId

def mutual(id1,id2,ourdict):
    mutual_friends = []
    id1_list = ourdict.get(id1)
    id2_list = ourdict.get(id2)

    for id1 in id1_list:
        for id2 in id2_list:
            if(id1 == id2):
                mutual_friends.append(id1)
    return mutual_friends

def suggestedFollowers(ourdict):
    #Dictionary to know suggested list of users to follow for each user 
    suggested_users_dict = dict()
    for id, inner_list in ourdict.items():
        userList =[]
        for val in inner_list:
            userList.extend(ourdict.get(val))
        userList = list(set(userList))
        for val in inner_list:
             if val in userList:
                userList.remove(val)
        if id in userList:
                userList.remove(id)
        suggested_users_dict[id] = userList
    return suggested_users_dict

# print(ourdict)
#print(most_influencer_user(ourdict))
#print(suggestedFollowers(ourdict))
#print(mutual(4, 5, ourdict))
#print(most_active_user(ourdict))
