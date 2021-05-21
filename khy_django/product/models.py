from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name = '��ǰ��')
    price = models.IntegerField(verbose_name = '��ǰ����')
    description = models.TextField(verbose_name = '��ǰ����')
    stuck = models.IntegerField(verbose_name ='���')
    register_date = models.DateTimeFieldField(auto_now_add=True, verbose_name='��ϳ�¥')

    class Meta:
        db_table = 'khy_order'
        verbose_name = '��ǰ'
        verbose_name_plural = '��ǰ'