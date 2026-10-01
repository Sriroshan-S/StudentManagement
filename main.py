
print("Welcome Student Management Sstem")
print("Introduction To GitHub")
import student
student.greet()
l=[["hp",12],["dell",14]]
print(student.display(l))
l=student.add(l)
s=input("enter student:")
student.search(s,l)
m=input("enter student rollno to delete:")
l=student.delete(m,l)
print("deleted sucessfully")
print(student.display(l))
