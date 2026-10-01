def add(l):
	s=input("Enter Student Name To Add:")
	l.append(s)
	return l
def display(l):
	for data in l:
		print("Student Name :",data)
def search(s,l):
	for i in l:
		if s == i:
			print(f"{s} found")
