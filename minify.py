# from Prettify import filepath
def Minify(path):
    with open(path,"r") as file:
        lines = file.readlines()
        for i,line in enumerate(lines):
            trimmedline = line.strip()
            if trimmedline.find("\n"):
                trimmedline.replace("\n","")
            lines[i] = trimmedline
    return lines
    # with open(".\\minified.xml","w") as file:
    #     #file.write('\n'.join(lines) + '\n')
    #     file.writelines(lines)
# Minify(filepath)
