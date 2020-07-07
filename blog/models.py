from django.db import models


# Create your models here.
class BlogPost(models.Model):
    # 博客标题
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150, blank=True)
    # 博客正文
    body = models.TextField()
    # 博客创建时间
    pub_date = models.DateTimeField()
    #author = models.ForeignKey(User, on_delete=)

    class Meta:
        ordering= ('-pub_date', )

    def __str__(self):
        return self.title


