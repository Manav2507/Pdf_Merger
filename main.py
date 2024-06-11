import pypdf

pdfiles = ['Profile (1).pdf', 'Profile (2).pdf', 'Profile (3).pdf']
merger = pypdf.PdfWriter()
for filename in pdfiles:
    pdfFile = open(filename,'rb')
    pdfReader = pypdf.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write("result.pdf")
