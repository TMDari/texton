link = "https://raw.githubusercontent.com/TMDari/texton/textonnews/"
file = "news"
a = ""
clear()
pathorig = os.getcwd()
os.chdir(os.getcwd()+"/texton/Apps/")
a = show(link,file)
if a is True:
    clean(file)
a = input("\npress enter to leave: ")
os.chdir(pathorig)