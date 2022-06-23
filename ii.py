import os
from pydoc import doc
from docx2pdf import convert

print(os.path.dirname(os.path.abspath(__file__)))

docs = ['DP4 REPORt-corr.docx','final report dp4..11.docx']
for dd in docs:
    convert(os.path.dirname(os.path.abspath(__file__)) + "/files/" + dd , dd.split(".")[0] + ".pdf")