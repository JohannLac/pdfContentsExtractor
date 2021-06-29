#!/usr/bin/python3

import sys, textract, re
from os.path import exists

def main(argv):
    if len(argv)!=1:
        print("Use: ./extractContents.py <path/to/pdf>")
        sys.exit(0)

    pdf_file = argv[0]
    if not exists(pdf_file):
        print("ERROR: file {} does not exist!".format(pdf_file))
        sys.exit(0)
    
    print("Extract text from {}...".format(pdf_file))
    text = str(textract.process(pdf_file, method='pdfminer'))
    
    print("Process and find matching patterns...")
    text = text.replace('\\n', '\n') #fix \n
    
    arr = re.findall("\n\n[1-9][1-9.]*[ ]+[A-Z][\w ]+", text)
    
    #print results
    print("Result:")
    print("----------------------------------------")
    reg_nb = re.compile("[1-9]")
    section=0 #keep in memory the section, avoid printing references that also match
    
    for s in arr:
        result = reg_nb.search(s)
        current_section = int(result.group(0))
    
        if current_section != section and current_section != section+1: #If there is a weird jump in the section, it's surely we got to the references 
            break
        section = current_section
    
        print("  "*s.count('.') + s.replace('\n', ''))
    print("----------------------------------------")

if __name__ == "__main__":
   main(sys.argv[1:])
