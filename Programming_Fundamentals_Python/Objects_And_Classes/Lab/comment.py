class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


object_comment = Comment("user1", "super cool app")
print(object_comment.username)
print(object_comment.content)
print(object_comment.likes)
