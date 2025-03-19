# class Car:
#     def move(self):
#         print("Car is moving")
        
#     def stop(self):
#         print("Car stopped")
        
# my_car = Car()
# my_car.move()
# my_car.stop()

class Comment:
    def __init__(self, text, initial_votes_qty=0):
        self.text = text
        self.votes_qty = initial_votes_qty
        
    def upvote(self, qty):
        self.votes_qty += qty
        
    def reset_votes_qty(self):
        self.votes_qty = 0
        
first_comment = Comment("my comment")

print(first_comment.votes_qty)

first_comment.upvote(10)
first_comment.upvote(20)
print(first_comment.votes_qty)

first_comment.reset_votes_qty()

print(first_comment.votes_qty)



# task 1 
# class Image:
#     def __init__(self, resolution, title, extention):
#         self.resolution = resolution
#         self.title = title 
#         self.extention = extention
     
#     def resize(self, new_resolution):
#         self.resolution = new_resolution 
        
#     def __str__(self):
#         return f"{self.title}. {self.extention}"
        
# first_img = Image('1920x1080', 'My dog', 'jpg')

# print(first_img.resolution)
# print(first_img.title)
# print(first_img.extention)

# first_img.resize('4000x3000')

# print(first_img.resolution)

# second_img = Image('8000x5000', 'jango', 'lato')

# print(first_img)


