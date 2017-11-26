import  sys,json

output_file = "output.json"

def get_input():
	file_path = "data/data1.txt";
	# file_path = raw_input("")
	if (file_path == ""):
		return get_input()
	return file_path
try:
	text = open(get_input())
except IOError:
	print("Error Found!\nExiting...")
	sys.exit()

lines = text.readlines()
myList = []
for line in lines:
	line = line.replace('\n','')
	line = line.strip(' ')
	while line.find('  ')!=-1:
		line = line.replace('  ',' ')
	line = line.split(" ")
	myList.append(line)
	# print line 
# print text.split(" ")
myList = {"data":myList[0:len(myList)-1]}
# myList = json.JSONEncoder().encode(myList)
myList = json.dumps(myList, sort_keys=True, indent=4)
outFile = open(output_file,"w");
outFile.write(myList);
print  type(myList)