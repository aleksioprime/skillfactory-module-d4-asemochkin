# Generated by Django 3.1.6 on 2021-02-04 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(verbose_name='Имя автора')),
                ('birth_year', models.SmallIntegerField(verbose_name='Год рожения')),
                ('country', models.CharField(max_length=2, verbose_name='Страна')),
            ],
        ),
        migrations.CreateModel(
            name='publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
                ('address', models.TextField(verbose_name='Юридический адрес')),
                ('web', models.TextField(verbose_name='Web-сайт')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13, verbose_name='Международный стандартный книжный номер')),
                ('title', models.TextField(verbose_name='Название')),
                ('description', models.TextField(verbose_name='Аннотация')),
                ('year_release', models.SmallIntegerField(verbose_name='Год издания')),
                ('copy_count', models.SmallIntegerField(verbose_name='Число копий')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='p_library.author', verbose_name='Автор')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_publisher', to='p_library.publisher', verbose_name='Издательство')),
            ],
        ),
    ]
