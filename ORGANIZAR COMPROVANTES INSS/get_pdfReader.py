import PyPDF2
def openFile(filename):
    try:
        fileObj = open(filename, 'rb')
    except FileNotFoundError:
        print(filename, ' Não encontrado!')
    else:
        return fileObj

def get_pdfReader(filename):
    fileObj = openFile(filename)
    pdfReader = PyPDF2.PdfFileReader(fileObj)
    return pdfReader