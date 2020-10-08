#!python3
#Programa para renomear os comprovantes de protocolo do sistems INSS.
#Renomear cada comprovante segundo o nome e cpf do socio
import re
import os
from get_pdfs import getPdfs
from get_pdfReader import get_pdfReader

def getFirstPagePdf(pdfReader):
    return pdfReader.getPage(0)

def getResultSearchRegex(regex, search):
    regex = re.compile(regex)
    resultSearchRegex = regex.search(search)
    return resultSearchRegex.group()

def getNameTextPagePdf(textPage):
    resultSearchRegexText = getResultSearchRegex(r'Requerente.{60}', textPage)
    resultSearchRegexName = getResultSearchRegex(r'Serviço.*', resultSearchRegexText)
    name = resultSearchRegexText[10:].replace(resultSearchRegexName,'')
    return name

def getCpfTextPagePdf(textPage):
    resultSearchRegex = getResultSearchRegex(r'RequerenteCPF:\s.{14}', textPage)
    cpf = resultSearchRegex[15:].replace('.','').replace('-','')
    return cpf

def rename():
    path = 'COMPROVANTES/'
    for pdfFile in getPdfs(path):
        firstPage = getFirstPagePdf(get_pdfReader(path+pdfFile))
        textPage = firstPage.extractText()
        newFileName = getNameTextPagePdf(textPage) +'_'+ getCpfTextPagePdf(textPage) + '_COMPROVANTE.pdf'
        os.rename(path+pdfFile, path+newFileName)
        print(pdfFile +' renamed for: '+newFileName)

rename()