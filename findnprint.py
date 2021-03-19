import os

path=input("Please type the path for check the files: ")
print("The path will be",path)

path="/var/log"
total_s=0
total_files=len(os.listdir(path))
top_5 = []

for files in os.listdir(path):
    location = os.path.join(path, files)
    if os.path.isfile(location):
        size = os.path.getsize(location)
        total_s += size
        top_5.append((size, files))
        #print(files , size)

top_5.sort(reverse=True, key=lambda s: s[0])
i=0
for file_size in top_5:
        print(file_size)
        i+=1
        if i == 5:
            break

print("Total files: " + str(total_files))
print("Total: " + str(total_s))
avg_file_s = total_s/total_files
print("Avg File size: " + str(avg_file_s))
