from os import getcwd, mkdir, utime, system


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
    wf.write (f"\t<title>{projectName}</title>\n")
    wf.write ("\t<link rel='stylesheet' href='./css/style.css' />\n")
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
touch (f"{getcwd ()}/{projectName}/js/main.js")

with open (f"{getcwd ()}/{projectName}/css/style.scss", "w") as wf:
    wf.write ("* {\n    padding: 0;\n    margin: 0;\n    box-sizing: border-box;\n}")

with open (f"{getcwd ()}/{projectName}/compileSass.sh", "w") as wf:
    wf.write ("#! /bin/bash\n\n\nsass css/style.scss css/style.css")

system (f"chmod +x {getcwd ()}/{projectName}/compileSass.sh")