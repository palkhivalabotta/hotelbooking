# Generated by Django 2.1.1 on 2018-12-17 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='availablerooms',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('room_type', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rom', models.CharField(max_length=50)),
                ('paru', models.CharField(max_length=50)),
                ('cin', models.DateField()),
                ('cout', models.DateField()),
                ('cno', models.IntegerField()),
                ('addr', models.CharField(max_length=250)),
                ('cnum', models.IntegerField()),
                ('cv', models.IntegerField()),
                ('cord_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='card',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('card_type', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Email_id', models.EmailField(max_length=20)),
                ('phone_no', models.IntegerField()),
                ('message', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('rpassword', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='amount',
            name='idno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hydapp.availablerooms'),
        ),
    ]