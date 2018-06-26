#Le o arquivo e checa se existe "palavrão", usando webservice

import urllib

def read_text():
    quotes = open("C:\python\palavrao.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_palavrao(contents_of_file)

def check_palavrao(texto):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+texto)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in response:
        print "Profanity alert!"
    elif "false" in response:
        print "This document has no curse words"
    else:
        print "Could not scan the document properly"

read_text()    
