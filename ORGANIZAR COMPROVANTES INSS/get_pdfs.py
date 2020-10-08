import os

def getPdfs(path):
    pdfs = []
    for file in os.listdir(path):
        if file.endswith('.pdf'):
            pdfs.append(file)
    return pdfs