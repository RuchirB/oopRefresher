#from FILE import CLASS
from Dog import Dog

#putting Dog in parennthasis is the same as Extends Dog
class Husky(Dog):
	class_variable = 9;



	def huskyJump(self, b, c):
		print("Husky jumped " +str(b) + " feet high")

	def overridenParentMethod(self):
		return 10000000



x = Dog("hi", 23)
y = Husky("bye", 32)
y.age = 3000


print(Husky.class_variable)
Husky.class_variable+=1
print(Husky.class_variable)


print(y.class_variable) #Should be zero

y.instanceVariable = 23
print(y.instanceVariable)
y.instanceVariable +=10
print(y.instanceVariable)


print(type(y))
print(y.name +" " + str(y.age))

y.huskyJump(2, 3)


print(y.parentMethod())
print(y.overridenParentMethod())

