my_file = "file.txt"
my_string = "oida"

infile = open(my_file,"r")

numlines = 0
found = 0
for line in infile:
	numlines += 1
	while 1:
		str_found_at = line.find(my_string)
		if str_found_at == -1:
			#string not found in line ...
			#go to next (ie break out of the while loop)
			break
		else:
			#string found in line
			found += 1
			print line
			line = line[str_found_at + len(my_string):]
infile.close()

print my_string + " was found " + str(found) + " times in " + str(numlines) + " lines"
