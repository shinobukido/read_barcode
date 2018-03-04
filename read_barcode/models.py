from django.db import models


class Category(models.Model):
    name = models.CharField('カテゴリー名', max_length=32)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField('商品名', max_length=32)
    price = models.IntegerField('価格')
    amount = models.IntegerField('個数', default=1)

    def __str__(self):
        return self.name


class Amount(models.Model):
    amount = models.PositiveIntegerField('個数', default=1)
