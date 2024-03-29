# Generated by Django 2.2.7 on 2019-11-19 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20191119_1011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Questions', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterField(
            model_name='question',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='question/images/%Y/%m/%d', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('easy', 'easy'), ('normal', 'normal'), ('hard', 'hard')], max_length=200, null=True, verbose_name='level'),
        ),
        migrations.AlterField(
            model_name='question',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=300, verbose_name='question text'),
        ),
    ]
