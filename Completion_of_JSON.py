#  Description :
#   Convert XML to JSON
#   Time Complexity = O(n)
#   Space Complexity = O(1)

def Json(s=""):
    with open("sample.xml", "r") as file:
        content = file.readlines()
        User_num = 0
        BodyIsOpened = False
        PostIsOpen = False
        Open_Until_Posts_Close_me = False
        TopicIsOpened = False
        Open_Until_Topics_Close_me = False
        Follower_Opened_until_followers_close_me = False
        Follower_Is_Opened = False
        s+="{"

        for i, x in enumerate(content):

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

            if (t_users >= 0 and x[t_users - 1] != '/'):
                Users_label = x[t_users: t_users + 5]
                s+="\""+Users_label+"\":{"

            elif (t_users >= 0 and x[t_users - 1] == '/' and x[(x.find("users")) + 4] == 's'):
                s += "}]}}"


            elif (t_user >= 0 and x[t_user - 1] != '/'):

                User_label = x[t_user: t_user + 4]
                if i == 1 or i == 2 :
                    #     if User_num > 1 :
                    s += "\"" + User_label + "\":[{"
                    # else:
                    #     print("\"" + User_label + "\":{", end="")
                else:
                    s += "},{"



            elif (t_posts >= 0 and x[t_posts - 1] != '/'):
                posts_label = x[t_posts: t_posts + 5]
                s += "\"" + posts_label + "\":{"

            elif (t_posts >= 0 and x[t_posts - 1] == '/'):
                Open_Until_Posts_Close_me = False
                s += "]},{"

            elif (t_post >= 0 and x[
                t_post - 1] != '/'):  # we make flag named PostIsOpen to prevent printing :[ but we print {
                if (Open_Until_Posts_Close_me == True):
                    s += ",{"

                else:
                    Open_Until_Posts_Close_me = True
                    post_label = x[t_post: t_post + 4]
                    s += "\"" + post_label + "\":[{"
                    PostIsOpen = True

            elif (t_post >= 0 and x[t_post - 1] == '/'):
                PostIsOpen = False


            elif (t_topics >= 0 and x[t_topics - 1] != '/'):

                topics_label = x[t_topics: t_topics + 6]
                s += "\"" + topics_label + "\":{"

            
    return s
    
# JSON
