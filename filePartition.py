import sys
import math
#Finding filename and no of lines per file
filename = str(sys.argv[1])
no_of_lines_per_file = int(sys.argv[2])


fileva = open(filename,"r")

#counting total lines in the bigfile and finding total small files required
lines = []
lines2= []
for line in fileva:
	lines.append(line.rstrip())

for line in lines:
	if line == '':
		continue
	else:
		lines2.append(line)
	
print("Total lines")
print(len(lines2))
total_lines = len(lines2)

total_files = math.ceil(total_lines/no_of_lines_per_file)
print("Total files")
print(total_files)
lines = lines2
#for normal partition
if total_files > 1:
	start = 0
	end = start + no_of_lines_per_file
	for i in range(0,total_files):
		small_filename = "file" + str(i) + ".txt" 
		small_file = open(small_filename,"w")
	
		
		while start < end:
			small_file.write(str(lines[start]))
			start = start + 1
		small_file.close()
		end = start + no_of_lines_per_file
		if len(lines) - start + 1 < no_of_lines_per_file:
			end = len(lines)
		
#If you enter the number of lines per file to be VERY large and all will fit in one file
else:
	small_filename = "singlefile.txt"
	small_file = open(small_filename,"w")	
	for i in range(0,len(lines)):
		small_file.write(str(lines[i]))
