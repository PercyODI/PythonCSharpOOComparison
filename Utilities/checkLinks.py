import sys, os, re

pattern = re.compile('\[.+\]\((?P<file>.+)\)', re.MULTILINE)
numBadLinks = 0;

print("\n")
os.chdir("..") # Assumes this utility is one directory deep.

mdFiles = []
for root, subFolders, files in os.walk("."):
    if("\." in root):
        continue
    for f in files:
        mdFiles.append(os.path.join(root, f))



for mdFile in mdFiles:
    fileContent = open(mdFile, 'r')
    for lineNum, line in enumerate(fileContent, start=1):
        matches = pattern.findall(line)
        for match in matches:
            if not os.path.isfile(match):
                numBadLinks += 1
                print(match + " is a bad link.")
                print("    Found in " + mdFile + " on line " + str(lineNum))

if numBadLinks < 1:
    print("No Bad Links Found!")
else:
    print("\nFound " + str(numBadLinks) + " bad links.")
