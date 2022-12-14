# filepath = "C:\\TestCode\\Project CPP\\sample.xml"


def clearSpacing(path):
    with open(path, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            trimmedline = line.lstrip()
            lines[i] = trimmedline
    return lines


def Prettifyfunction(filelines):
    level = 0
    previousstatus = spaced = ""
    for x, line in enumerate(filelines):
        # find positions of tags if exists, otherwise return -1
        openingb = line.find('<')
        closingb = line.find('>')
        closingtag = line.find('/')
        if x == 0:
            # to indent in case of header (taking level 0)
            previousstatus = "openedlevel"
        if openingb != -1 and closingb != -1:  # check for o/c tags
            # / is found and before it, the openedleveling tag
            if closingtag != -1 and line[closingtag - 1] == '<':
                if line[openingb + 1] != '/' and line[closingtag + 1] != '>':
                    if previousstatus == "openedlevel":  # the parent tag didn't close in on the child so child is indented
                        level += 4
                    previousstatus = "closedlevel"
                else:
                    if previousstatus == "closedlevel":  # to reset the spacing
                        level -= 4
                    previousstatus = "closedlevel"
            if closingtag == -1:  # keep indenting if there's no parent closing
                if previousstatus == "openedlevel":
                    level += 4
                previousstatus = "openedlevel"
            if closingtag != -1 and line[closingtag - 1] != '<' and line[closingtag + 1] != '>':
                if previousstatus == "openedlevel":
                    level += 4
                previousstatus = "openedlevel"
        for i in range(level):
            spaced += ' '
        spaced += line
    spaced = spaced.split("\n")
    spaced.insert(
        0, '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>')
    spaced = '\n'.join(spaced)
    return spaced

# clearSpacing(filepath)
# Prettifyfunction(filepath)
