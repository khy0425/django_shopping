from django.db import models

# Create your models here.

class Fcuser(models.Model):
    email = models.EmailField(verbose_name = '�̸���')
    password = models.CharField(max_length = 64)
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='��ϳ�¥')

    class Meta:
        db_table = 'khy_order'
        verbose_name = '�����'
        verbose_name_plural = '�����'