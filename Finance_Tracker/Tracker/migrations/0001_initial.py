# Generated by Django 5.0.1 on 2024-02-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finance_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField()),
                ('Category', models.CharField(choices=[('BL', 'Bills'), ('RT', 'Rent'), ('FD', 'Food'), ('ED', 'Education'), ('MC', 'Misc'), ('TR', 'Travel')], default='BL', max_length=2)),
                ('Date', models.DateTimeField()),
                ('Desc', models.CharField(max_length=50)),
            ],
        ),
    ]