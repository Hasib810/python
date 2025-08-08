class user:


    def ___init__(self, name, age):
        self.name = name
        self.age = age
        self.followers = 0
        self.following = 0 
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = user("001","Hasib")
user2 = user("002","Rahman")


print(user1.name)