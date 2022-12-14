# from Prettify import filepath
def Minify(path):
    with open(path, "r") as file:
        lines = file.readlines()
        lines.insert(
            0, '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>')
        for i, line in enumerate(lines):
            trimmedline = line.strip()
            if trimmedline.find("\n"):
                trimmedline.replace("\n", "")
            lines[i] = trimmedline
    lines = ''.join(lines)
    return lines
    # with open(".\\minified.xml","w") as file:
    #     #file.write('\n'.join(lines) + '\n')
    #     file.writelines(lines)
# Minify(filepath)
