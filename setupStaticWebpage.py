from os import getcwd, mkdir, utime


def touch (path):
    with open (path, 'a'):
        utime (path, None)


while True:
    projectName = input ("Enter project name: ")
    
    try:
        mkdir (f"{getcwd ()}/{projectName}")
        break
    except:
        print (f"\nProject name already exists in {getcwd ()}. Choose another name.\n")
   
with open (f"{getcwd ()}/{projectName}/index.html", "w") as wf:
    wf.write ("<!DOCTYPE html>\n")
    wf.write ("<html lang='en'>\n")
    wf.write ("<head>\n")
    wf.write ("\t<meta charset='UTF-8'>\n")
    wf.write ("\t<meta http-equiv='X-UA-Compatible' content='IE=edge'>\n")
    wf.write ("\t<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
    wf.write ("\t<title>{projectName}</title>\n")
    wf.write ("<link rel='stylesheet' href='./css/style.css' />")
    wf.write ("</head>\n")
    wf.write ("<body>\n")
    wf.write ("\tYour content goes here!\n")
    wf.write ("\t<script src='./js/main.js'></script>\n")
    wf.write ("</body>\n")
    wf.write ("</html>")

mkdir (f"{getcwd ()}/{projectName}/css")
mkdir (f"{getcwd ()}/{projectName}/js")
mkdir (f"{getcwd ()}/{projectName}/media")

touch (f"{getcwd ()}/{projectName}/css/style.scss")  

