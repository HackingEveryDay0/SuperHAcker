# ​ Write a script that compresses a file into a ZIP archive.
import zipfile

with zipfile.ZipFile("test.zip",'w',zipfile.ZIP_DEFLATED) as zipfile:
    zipfile.write("test.txt")

