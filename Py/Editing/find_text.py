# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from docx import Document
import re
import sys
document = Document(r'E:\OneDrive\Information\Writing and Editing\AutoEdit\test.docx')
texttobefound = [r"antiinflammatory\b",
r"antiinvasive\b",
r"biorelevant\b",
r"noncoordinating\b",
r"nondeprotonated\b",
r"nonmalignant\b",
]
sys.stdout = open('E:\OneDrive\Information\Writing and Editing\AutoEdit\out.txt', 'w', encoding="utf8")
for x in texttobefound:
    # with open('E:\OneDrive\Information\Writing and Editing\AutoEdit\out.txt', 'w') as out:
    print(x)
    for paragraph in document.paragraphs:
        if re.search(x,paragraph.text):
        #if x in paragraph.text:
            #print(x)
            # with open('E:\OneDrive\Information\Writing and Editing\AutoEdit\out.txt', 'w') as out:
            print(paragraph.text)
            print("\n")
            #paragraph.text = 'new text containing ocean'
sys.stdout.close()
sys.stdout = sys.__stdout__            
            
