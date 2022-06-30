import PyPDF2 
import os
 
pdfInput = ""
pdfNames = []
#Grab user input to check files they want to merge
while True:
    pdfInput = input("Enter PDF file name: ")
    if(pdfInput == "q"): break
    if(not pdfInput.endswith(".pdf")):
        pdfInput = pdfInput + ".pdf"
    pdfNames.append(pdfInput)

print("Trying to merge files: \n")
print(pdfNames)

if(len(pdfNames)<2):
    print("You need at least 2 files to merge")
    quit()


# Open the files that have to be merged one by one
pdf1File = open(pdfNames[0], 'rb')
pdf2File = open(pdfNames[1], 'rb')
 
# Read the files that you have opened
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
 
# Create a new PdfFileWriter object which represents a blank PDF document
pdfWriter = PyPDF2.PdfFileWriter()
 
# Loop through all the pagenumbers for the first document
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
 
# Loop through all the pagenumbers for the second document
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
 
# Now that you have copied all the pages in both the documents, write them into the a new document
pdfOutputFile = open('MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

#Do rest of files in pdfNames if more files than two
if(len(pdfNames)>2):
    for i in range(2,len(pdfNames)):
        # Open the files that have to be merged one by one
        pdf1File = open("MergedFiles.pdf", 'rb')
        pdfTemp = open("tempMerge.pdf", 'wb')

        pdfTempReader = PyPDF2.PdfFileReader(pdf1File)
        pdfTempWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdfTempReader.numPages):
            pageObj = pdfTempReader.getPage(pageNum)
            pdfTempWriter.addPage(pageObj)
        pdfTempWriter.write(pdfTemp)
        pdf1File.close()
        pdfTemp.close()
        pdfTemp = open("tempMerge.pdf", 'rb')
        pdf2File = open(pdfNames[i], 'rb')
        
        # Read the files that you have opened
        pdf1Reader = PyPDF2.PdfFileReader(pdfTemp)
        pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
        
        # Create a new PdfFileWriter object which represents a blank PDF document
        pdfWriter = PyPDF2.PdfFileWriter()
        
        # Loop through all the pagenumbers for the first document
        for pageNum in range(pdf1Reader.numPages):
            pageObj = pdf1Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        
        # Loop through all the pagenumbers for the second document
        for pageNum in range(pdf2Reader.numPages):
            pageObj = pdf2Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        
        
        # Now that you have copied all the pages in both the documents, write them into the a new document
        pdfOutputFile = open('MergedFiles.pdf', 'wb')
        pdfWriter.write(pdfOutputFile)

        # Close all the files - Created as well as opened
        pdfOutputFile.close()
        pdf2File.close()
        pdfTemp.close()
        os.remove("tempMerge.pdf")
