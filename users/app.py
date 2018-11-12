class User():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def describe_user(self):
        print("firstname", self.firstname)
        print("lastname", self.lastname)
        print("age", self.age)

    def greet_user(self):
        print("Hello", self.firstname, self.lastname, "!")

user1 = User("Juan", "Perez", 20)
user2 = User("John", "Doe", 30)
user3 = User("Jose", "Lopez", 25)

user1.describe_user()
user1.greet_user()
print("")

user2.describe_user()
user2.greet_user()
print("")

user3.describe_user()
user3.greet_user()
print("")

