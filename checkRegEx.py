# ===============================================
# Simple utility for checking RegEx (or strings) in text files,
# reading a file line by line 
#
#
# ToDo:
#   - Add output text file instead of just printing
#   - Add feature to look at all files in the directory to replace file_list variable
# ===============================================
import re

#====================================================
# variable pattern: the ReGex or string to search to
# ===================================================
pattern = re.compile("[. {]X_")

#====================================================
# variable file_prefix: path to text files
# variable file_list: list of text files (with extension) that will be read
# ===================================================
file_prefix = "C:/ExamplePath/"
file_list = ["File1.txt", "File2.txt"]

#====================================================
# variable file_hits: list of files in which the pattern was found
# ===================================================
file_hits = []

#====================================================
# Going through each line of each file and printing results
# grouped by file
# ===================================================
for i in range(len(file_list)):
    print("------" + file_list[i] + "------ \n")
    for line in open(file_prefix + file_list[i]):
        for match in re.finditer(pattern, line):
            print(file_list[i] + ": " + line)
            if file_list[i] in file_hits:
                pass
            else:
                file_hits.append(file_list[i])
                
#====================================================
# Finally, displaying how many and which files have the pattern
#====================================================
print("*** The following " + str(len(file_hits)) + " files have the pattern:")
for i in range(len(file_hits)):
    print(file_hits[i])