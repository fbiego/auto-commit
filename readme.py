import glob, os


commitFiles = glob.glob("commit*.txt")
readMe = open('README.md', 'w')
readMe.write("# auto-commit\n\n")
readMe.write("### execution time \n\n")

readMe.write("| script | run time |\n")
readMe.write("| ------ | -------- |\n")

for f in commitFiles:
    ln = open(f, 'r').readlines()
    c = ln[1].replace("\n", "")
    nm = ln[0].replace("\n", "")
    readMe.write("| "+nm+" | "+c+" |\n")

readMe.close()
print(len(commitFiles))

os.system("git add --all")
os.system('git commit -am "update README.md"')
