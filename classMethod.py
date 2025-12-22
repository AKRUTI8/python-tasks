class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1 = Person()
p1.changeName("kjbjfgvjb")
print(p1.name)

# we can change the class attribute