def ClearSpaces(path):
    with open(path,"r") as file:
        lines = file.readlines()
        for i,line in enumerate(lines):
            trimmedline = line.strip() #trim every line of spaces and place it in the list of lines
            if trimmedline.find("\n"):
                trimmedline.replace("\n","")
            lines[i] = trimmedline
    with open("C:\\TestCode\\Project CPP\\minified.xml","w") as file:
        #file.write('\n'.join(lines) + '\n')
        file.writelines(lines)
ClearSpaces(filepath)
