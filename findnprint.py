import os

path=input("Please type the path for check the files: ")
print("The path will be",path)

def file_size(fname):
        info = os.stat(fname)
        return info.st_size

nfiles=0
files=[]
filesize=[]
for root, dirs, files in os.walk(path):
    for filename in files:
        nfiles+=1
        #files=files.append(filename + ': ' + str(file_size(filename)) + " bytes")
        print(root + dirs + files ) 
        print(file_size(filename))


print(nfiles)
#print(files)
#print(filesize)
