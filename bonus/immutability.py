filenames = ['1.Raw Data.txt','2.Reports.txt','3.Presentations.txt'] # List of filenames

for filename in filenames:
    filenames[filenames.index(filename)] = filename.replace('.', '-', 1) # Replace the first occurrence of '.' with '-'    

print(filenames)
