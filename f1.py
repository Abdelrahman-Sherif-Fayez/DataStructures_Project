with open("sample.xml","r") as file:
    content = file.readlines()
    User_num = 0
    # Follower_num = 0
    # Post_num = 0
    # Topic_num = 0
    #
    for i, x in enumerate(content):
        if(x.find("user")>=0 and x[(x.find("user"))-1]!='/' and x[(x.find("user"))+4]!='s'):
            User_num=User_num+1
    #     elif (x.find("follower") >= 0 and x[(x.find("follower"))-1]!='/'and x[(x.find("follower"))+8]!='s'):
    #         Follower_num=Follower_num+1
    #     elif (x.find("post") >= 0 and x[(x.find("post"))-1]!='/'and x[(x.find("post"))+4]!='s'):
    #         Post_num=Post_num+ 1
    #     elif (x.find("topic") >= 0 and x[(x.find("topic"))-1]!='/'and x[(x.find("topic"))+4]!='s'):
    #         Topic_num=Topic_num+ 1
    #
    # print (User_num)

    # topic_flag = False
    # topic_flag2 = False
    # topics_flag = False
    # post_flag = False
    # post_flag2 = False
    # posts_flag= False
    BodyIsOpened = False
    PostIsOpen = False
    Open_Until_Posts_Close_me = False
    TopicIsOpened = False
    Open_Until_Topics_Close_me = False
    Follower_Opened_until_followers_close_me = False
    Follower_Is_Opened = False

    print("{",end="")
    for i,x in enumerate(content):

        t_users = x.find("users")
        t_user = x.find("user")
        t_name = x.find("name")
        t_id = x.find("id")
        t_posts = x.find("posts")
        t_post = x.find("post")
        t_topics = x.find("topics")
        t_topic = x.find("topic")
        t_body = x.find("body")
        t_followers = x.find("followers")
        t_follower = x.find("follower")

        if(t_users>=0 and x[t_users-1]!='/'):
            Users_label = x[t_users : t_users + 5]
            print("\""+Users_label+"\":{",end="")

        elif (t_users >= 0 and x[t_users - 1] == '/'and x[(x.find("users"))+4]=='s'):
            print("}]}}",end="")




        elif ( t_user>=0 and x[t_user-1]!='/' ):

            User_label = x[t_user: t_user + 4]
            if i == 1:
            #     if User_num > 1 :
                print("\"" + User_label + "\":[{",end="")
                # else:
                #     print("\"" + User_label + "\":{", end="")
            else:
                print("},{", end="")



        elif(t_posts>=0 and x[t_posts-1]!='/'):
            posts_label = x[t_posts: t_posts + 5]
            print("\"" + posts_label + "\":{", end="")

        elif (t_posts >= 0 and x[t_posts - 1] == '/'):
            Open_Until_Posts_Close_me = False
            print("]},{",end="")

        elif (t_post >= 0 and x[t_post - 1] != '/'): #we make flag named PostIsOpen to prevent printing :[ but we print {
            if(Open_Until_Posts_Close_me == True):
                print(",{",end="")
            else:
                Open_Until_Posts_Close_me = True
                post_label = x[t_post: t_post + 4]
                print("\"" + post_label + "\":[{", end="")
                PostIsOpen = True

        elif (t_post >= 0 and x[t_post - 1] == '/'):
            PostIsOpen = False


        elif (t_topics >= 0 and x[t_topics - 1] != '/'):

            topics_label = x[t_topics: t_topics + 6]
            print("\"" + topics_label + "\":{", end="")

        elif (t_topics >= 0 and x[t_topics - 1] == '/'):
            Open_Until_Topics_Close_me = False;
            print("]}}",end="")

        elif (t_topic >= 0 and x[t_topic - 1] != '/'):# we make a flag called TopicIsOpened to acknoledge its data

            if Open_Until_Topics_Close_me == True:
                print(",",end="")
            else:
                Open_Until_Topics_Close_me = True
                topic_label = x[t_topic: t_topic + 5]
                print("\"" + topic_label + "\":[", end="")
            TopicIsOpened = True


        elif (TopicIsOpened == True and t_topic < 0):
            my_str = x.lstrip()
            print(my_str[0: len(my_str) - 1], end="")


        elif (t_topic >= 0 and x[t_topic - 1] == '/'):
            TopicIsOpened = False
            # print("]}", end="")



        elif (t_body >= 0 and x[t_body - 1] != '/'): # we make a flag called BodyIsOpened to acknoledge its data
            BodyIsOpened =True
            body_label = x[t_body: t_body + 4]
            print("\"" + body_label + "\":", end="")

        elif(BodyIsOpened == True and t_body < 0):
            my_str = x.lstrip()
            print(my_str[0: len(my_str) - 1], end=",")

        elif (t_body >= 0 and x[t_body - 1] == '/'):
            BodyIsOpened = False


        elif(t_followers>=0 and x[t_followers - 1] != '/'):
            followers_label = x[t_followers: t_followers + 9]
            print("\"" + followers_label + "\":{", end="")

        elif (t_followers >= 0 and x[t_followers - 1] == '/'):
            Follower_Opened_until_followers_close_me = False
            print("}]}",end="")

        elif (t_follower >= 0 and x[t_follower - 1] != '/'):
            if Follower_Opened_until_followers_close_me == True:
                print("},{",end="")
            else:
                follower_label = x[t_follower: t_follower + 8]
                print("\"" + follower_label + "\":[{", end="")
                Follower_Opened_until_followers_close_me = True
            Follower_Is_Opened = True  # flag to help us acknowledge id

        elif (t_follower >= 0 and x[t_follower - 1] == '/'):
            Follower_Is_Opened = False

        elif(t_id>=0 and x[t_id - 1] != '/'and Follower_Is_Opened == True):
            Id_label = x[t_id: t_id + 2]
            sub_string = x[t_id:]
            exact_id = sub_string[sub_string.find(">") + 1:  sub_string.find("<")]
            print("\"" + Id_label + "\":" + str(exact_id), end="")


            


        elif(t_name>=0):
            Name_label = x[t_name : t_name+4]
            sub_string = x[t_name : ]
            exact_name = sub_string[sub_string .find(">")+1 :  sub_string .find("<")]
            print("\"" + Name_label + "\":\""+exact_name, end="\",")

        elif(t_id >=0 and x[t_id-1]!='/' ):
            Id_label = x[t_id : t_id+2]
            sub_string = x[t_id : ]
            exact_id = sub_string[sub_string .find(">")+1 :  sub_string.find("<")]
            print("\"" + Id_label + "\":"+str(exact_id), end=",")
            
            


            



