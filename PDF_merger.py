from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list,output):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf.strip())
    merger.write(output)
    merger.close()

pdfs=input("Enter PDF's to Merge (coma-separated):").split(",")
print("Merging PDF files...\n")
merge_pdfs(pdfs,"merged.pdf")
print("PDF files merged and saved as merged.pdf !")
