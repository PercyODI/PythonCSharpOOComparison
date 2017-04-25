import sys, os, re

pattern = re.compile('\[.+\]\((?P<file>.+)\)', re.MULTILINE)


print("\n")
os.chdir("..") # Assumes this utility is one directory deep.
startDirectory = os.path.abspath(".")
tableOfContentsPath = os.path.abspath("README.md")

mdFiles = []
for root, subFolders, files in os.walk("."):
    if "\." in root: # Ignore hidden directories
        continue
    for f in files:
        if ".md" in f: # Only modify MarkDown files
            mdFiles.append(os.path.abspath(os.path.join(root, f)))

for mdFile in mdFiles:
    backOne = ":arrow_backward: [Back to Intro](./Intro.md) <!-- BackOne -->\n"
    pathToToC = os.path.relpath(tableOfContentsPath, os.path.dirname(mdFile)).replace("\\", "/")
    backToC = ":rewind: [Back to Table of Contents](" + pathToToC + ") <!-- BackToC -->\n"
    backOneFlag = False
    backToCFlag = False
    data = []
    with open(mdFile, "r") as f:
        oldData = f.readlines()

    for index, line in enumerate(oldData):
        if line.find("<!-- BackOne -->") != -1:
            if(oldData[index - 1] != "\n"):
                data.append("\n")
            data.append(backOne)
            backOneFlag = True
        elif line.find("<!-- BackToC -->") != -1:
            if(oldData[index - 1] != "\n"):
                data.append("\n")
            data.append(backToC)
            backToCFlag = True
        else:
            data.append(line)

    if not backOneFlag and os.path.basename(mdFile) != "Intro.md":
        data.append("\n")
        data.append(backOne)
    if not backToCFlag:
        data.append("\n")
        data.append(backToC)


    print(data)
    with open(mdFile, 'w') as f:
        f.writelines(data)
