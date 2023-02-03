def get_post(path, topic: str):
    ourdict = dict()
    s = ""
    t = ""
    flag_body = False
    flag_topic = False
    with open(path, "r") as file:
        content = file.readlines()
        for i, x in enumerate(content):
            t_body = x.find("body")
            t_topic = x.find("topic")

            if(t_body >= 0 and x[t_body-1] != '/'):  # body_Open
                s = ""
                flag_body = True

            elif(t_body >= 0 and x[t_body-1] == '/'):  # body_close
                if ourdict.get(s) is None:
                    ourdict[s] = list()
                flag_body = False

            elif(flag_body == True):  # body_fetch
                x = x.strip()
                s = s + x[:len(x)]

            elif(t_topic >= 0 and x[t_topic-1] != '/'):  # topic_open
                flag_topic = True
                t = ""

            elif(t_topic >= 0 and x[t_topic-1] == '/'):  # topic_close
                flag_topic = False

            elif(flag_topic == True):  # topic_fetch
                x = x.strip()
                t = t + x[:len(x)]
                (ourdict[s]).append(t)

    ans = "body:" + "\n"
    post = ""
    for key, inner in ourdict.items():
        for val in inner:
            if val == topic:
                post = key
                break

    if(post != ""):
        ans = ans + post
        ans = ans + "\n"
        ans = ans + "topics:" + "\n"
        for val in ourdict[post]:
            ans = ans + val
            ans = ans + "\n"
        return ans

    for key in ourdict.keys():
        if(key.find(topic) != -1):
            post = key
            break

    ans = ans + post
    ans = ans + "\n"
    ans = ans + "topics:" + "\n"
    for val in ourdict[post]:
        ans = ans + val
        ans = ans + "\n"
    return ans
