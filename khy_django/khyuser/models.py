from django.db import models

# Create your models here.


class Khyuser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64)
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        db_table = 'khy_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
