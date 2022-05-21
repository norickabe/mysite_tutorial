from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField('タイトル', max_length=255, help_text='作業概要',)
    author = models.CharField('作成者', max_length=50, help_text='作成者',)
    worker = models.CharField('作業担当者', max_length=50, help_text='作業担当者',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    #duration = models.DurationField(verbose_name='有効期間', 
    #                                default=90,
    #                                null=True,
    #                                blank=True,
    #                                help_text=('HH:MM:SS'),)

    def __str__(self) -> str:
        return self.title