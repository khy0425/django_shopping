from django.db import models

# Create your models here.
class Order(models.Model):
    fcuser = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='�����')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name = '��ǰ')
    quantity = models.IntegerField(verbose_name='����')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name = '��ϳ�¥')

    class Meta:
        db_table = 'khy_order'
        verbose_name = '�ֹ�'
        verbose_name_plural = '�ֹ�'