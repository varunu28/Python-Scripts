import urllib

def read_text():
    quotes = open("PATH FOR DRAFT HERE") #Give the path to the text file in between the quotes and run the script to do a profanity check
    contents_of_file=quotes.read()
    #print contents_of_file
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    #print(output)
    if "true" in output:
        print("Profanity Alert")
    elif "false" in output:
        print("This output has no curse words")
    else:
        print("Could not scan the documents properly")
    connection.close()

read_text()
