# filepath = "C:\\TestCode\\Project CPP\\sample.xml"

def clearSpacing(path):
    with open(path,"r") as file:
        lines = file.readlines()
        xmlheader = '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>'
        lines.insert(0,xmlheader)
        for i,line in enumerate(lines):
            trimmedline = line.lstrip()
            lines[i] = trimmedline
    return lines

def Prettifyfunction(cleared):
    level = 0
    previousstatus = spaced = ""
    for x,line in enumerate(cleared):
        openingb = line.find('<') #find positions of tags if exists, otherwise return -1
        closingb = line.find('>')
        closingtag = line.find('/')
        if x == 0:
            previousstatus = "openedlevel" #to indent in case of header (taking level 0)
        if openingb !=-1 and closingb !=-1: #check for o/c tags
            if closingtag != -1 and line[closingtag -1] == '<': #/ is found and before it, the openedleveling tag
                if line[openingb + 1] != '/' and line[closingtag +1] !='>':
                    if previousstatus == "openedlevel": #the parent tag didn't close in on the child so child is indented
                        level += 4
                    previousstatus = "closedlevel"
                else:
                    if previousstatus == "closedlevel": #to reset the spacing
                        level -= 4
                    previousstatus = "closedlevel"
            if closingtag == -1: #keep indenting if there's no parent closing
                if previousstatus == "openedlevel":
                    level += 4
                previousstatus = "openedlevel"
            if closingtag != -1 and line[closingtag - 1] != '<' and line[closingtag +1] !='>':
                if previousstatus == "openedlevel":
                    level+=4
                previousstatus = "openedlevel"
        for i in range(level):
            spaced += ' '
        spaced += line
    return spaced
# clearSpacing(filepath)
# Prettifyfunction(filepath)

