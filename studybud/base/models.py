from ast import For, mod
from django.db import models

class User(models.Model):
    first_name = models.CharField('first_name', max_length=20)
    last_name = models.CharField('last_name', max_length=20)
    email = models.CharField('email', max_length=256, null=False, unique=True, blank=False)
    password = models.CharField('password', max_length=256, null=False, blank=False)
    age = models.IntegerField('age', default=0)
    blog_count = models.IntegerField('blog_count', default=0)

    class Meta:
        db_table = 'User'

    def __str__(self) -> str:
        return f"<User first_name={self.first_name} last_name={self.last_name} age={self.age}>\n"
    
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
    

class Blog(models.Model):
    
    blogger = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    blog_text = models.TextField('blog_text')
    publication_date = models.DateTimeField('publication_date')
    like_count = models.IntegerField('like_count', default=0)
    comment_count = models.IntegerField('comment_count', default=0)

    class Meta:
        db_table = 'Blog'

    def __str__(self) -> str:
        return f"<Blog blogger={self.blogger.full_name} blog_text={self.blog_text}"


class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    like_count = models.IntegerField('like_count', default=0)
    comment_text = models.TextField('comment_text')

    class Meta:
        db_table = 'Comment'

    def __str__(self) -> str:
        return f"<Comment commenter={self.commenter.full_name}"    

class Like(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    liker = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Like'
        
    def __str__(self) -> str:
        return f"<Like comment={self.comment} liker={self.liker.full_name}>"
    