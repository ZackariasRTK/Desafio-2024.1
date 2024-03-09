# Generated by Django 5.0.3 on 2024-03-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='acharIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50, verbose_name='IP')),
                ('cidade', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cidade')),
                ('regiao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Região')),
                ('paisC', models.CharField(blank=True, max_length=50, null=True, verbose_name='Código do país')),
                ('paisN', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome do país')),
                ('capital', models.CharField(blank=True, max_length=50, null=True, verbose_name='Capital do país')),
            ],
        ),
    ]