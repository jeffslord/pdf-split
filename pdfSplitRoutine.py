import os
import pdfSplit

rootPath = os.path.join("pdfs")
pdfsPath = os.path.join(rootPath, "_PDFs")

folders = os.listdir(rootPath)
pdfs = os.listdir(pdfsPath)

print(folders)
print(pdfs)

for doc in pdfs:
    docNoExt = os.path.splitext(doc)[0]
    if(docNoExt not in folders):
        print("[INFO] Processing new pdf: {0}".format(doc))
        # docPath = os.makedirs(os.path.join(rootPath, "doc"))
        outPath = os.path.join(rootPath, docNoExt)
        pdfSplit.main(
            ['--pdf', os.path.join(pdfsPath, doc), '--dest', outPath])
