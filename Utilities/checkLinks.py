import sys, os, re

pattern = re.compile('\[.+\]\((?P<file>.+?)\)', re.MULTILINE) # Matches [text](directory/file.md)
folderDict = {}
numBadLinks = 0;


os.chdir("..") # Assumes this utility is one directory deep.
startDirectory = os.path.abspath(".")

mdFiles = []
for root, subFolders, files in os.walk("."):
    if("\." in root):
        continue
    for f in files:
        if ".md" in f: # Only modify MarkDown files
            mdFiles.append(os.path.abspath(os.path.join(root, f)))

for mdFile in mdFiles:
    os.chdir(os.path.dirname(mdFile))
    fileContent = open(mdFile, 'r')
    for lineNum, line in enumerate(fileContent, start=1):
        matches = pattern.findall(line)
        for match in matches:
            if not os.path.isfile(match):
                numBadLinks += 1
                print("\n")
                print(os.path.relpath(mdFile, startDirectory) + ", line " + str(lineNum))
                print("\t" + match + " is a bad link.")

print("\n")
if numBadLinks < 1:
    print("No Bad Links Found!")
else:
    print("Found " + str(numBadLinks) + " bad links.")
