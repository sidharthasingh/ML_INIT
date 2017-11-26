import  sys,json

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
myList = json.JSONEncoder().encode(myList)
print  type(myList)