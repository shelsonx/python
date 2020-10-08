#!Python3
#Junta a primeira página de cada comprovante de protocolo do INSS, em um único arquivo
import PyPDF2
import os

from get_pdfs import getPdfs
from get_pdfReader import get_pdfReader

pdfWriter = PyPDF2.PdfFileWriter()
path = 'COMPROVANTES/'

def fileNameAvailable(filename):
    if os.path.exists(filename):
        raise Exception(filename, ' já está sendo usado!')

def savePDF(filename, pdfWriter):
    try:
        fileNameAvailable(filename)
    except Exception as err:
        print(err)
    else:
        pdfFileName = open(filename, 'wb')
        pdfWriter.write(pdfFileName)
        pdfFileName.close()

def joinPdfs(pdfWriter, filename):
    for pdf in sorted(getPdfs(path)):
        filePdfReader = get_pdfReader(path+pdf)
        firstPage = filePdfReader.getPage(0)
        pdfWriter.addPage(firstPage)
        print('Adicionado página: ', pdf)
    savePDF(path+filename, pdfWriter)

joinPdfs(pdfWriter, 'COMPROVANTES.pdf')