from django.db import models

class BookList(models.Model):
    
    book_title = models.CharField(
        blank=False,
        null=False,
        verbose_name="タイトル",
        max_length=100,
    )
    
    author = models.CharField(
        blank=False,
        null=False,
        verbose_name="タイトル",
        max_length=100,
    )
    
    created_at_date = models.DateTimeField(
        auto_now_add=True
    )
    
    updata_date = models.DateTimeField(
        auto_now=True
    )
