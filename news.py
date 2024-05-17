import os, base as b
link = "https://raw.githubusercontent.com/TMDari/texton/textonnews/"
file = "news"
a = ""
b.clear()
pathorig = os.getcwd()
os.chdir(os.getcwd()+"/texton/Apps/")
a = b.show(link,file)
if a is True:
    b.clean(file)
a = input("\npress enter to leave: ")
os.chdir(pathorig)