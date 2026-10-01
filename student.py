def add(l):
	n=input("Enter Student Name To Add:")
	r=int(input("enter roll number:"))
	l.append([n,r])
	return l
def display(l):
	for data in l:
		print("Student Details :",data)
def search(s,l):
	for i in l:
		if s == i[0]:
			print(f"{s} found")
def delete(a,l):
	for i in l:
		if a == i[1]:
			l.remove(i)
	print("removed sucessfully.")
	return l
