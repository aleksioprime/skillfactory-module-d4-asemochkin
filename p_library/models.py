import uuid

from django.utils.translation import gettext as _
from django.db import models


class Author(models.Model):
    full_name = models.TextField(verbose_name=_("Имя автора"))
    birth_year = models.SmallIntegerField(verbose_name=_("Год рожения"))
    country = models.CharField(max_length=2, verbose_name=_("Страна"))

    def __str__(self):
        return self.full_name

class Book(models.Model):
    ISBN = models.CharField(max_length=13,
                            verbose_name=_("Международный стандартный "
                                           "книжный номер"))
    title = models.TextField(verbose_name=_("Название"))
    description = models.TextField(verbose_name=_("Аннотация"))
    year_release = models.SmallIntegerField(verbose_name=_("Год издания"))
    copy_count = models.SmallIntegerField(verbose_name=_("Число копий"))
    price = models.DecimalField(max_digits=12, decimal_places=2,
                                verbose_name=_("Цена"))
    author = models.ForeignKey("p_library.Author", on_delete=models.CASCADE,
                               verbose_name=_("Автор"),
                               related_name="book_author")
    publisher = models.ForeignKey("p_library.publisher", on_delete=models.CASCADE,
                                  verbose_name=_("Издательство"),
                                  related_name="book_publisher")

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.TextField(verbose_name='Название')
    address = models.TextField(verbose_name='Юридический адрес')
    web = models.TextField(verbose_name='Web-сайт')

    def __str__(self):
        return self.name