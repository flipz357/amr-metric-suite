import re
    

match_of = re.compile(":[0-9a-zA-Z]*-of")
match_no_of = re.compile(":[0-9a-zA-Z]*(?!-of)")

def readFile(filepath):
    with open(filepath, 'r') as content_file:
        content = content_file.read()
    amr_t = content
    amr_t = re.sub(match_no_of,":label",amr_t)
    amr_t = re.sub(match_of,":label-of",amr_t)
    print (amr_t)

import sys
readFile(sys.argv[1])
