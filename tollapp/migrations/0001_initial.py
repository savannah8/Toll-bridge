# Generated by Django 2.2.6 on 2019-11-03 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bursary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=40)),
                ('Last_name', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Prefer not to say', 'Prefer not to say')], max_length=100, null=True)),
                ('Have_you_participated_in_any_aid_providing_programme_before', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True)),
                ('Which_avenue_was_most_influential_in_your_learning', models.CharField(choices=[('Books', 'Books'), ('Newspapers', 'Newspapers'), ('Magazines', 'Magazines'), ('E-Learning', 'E-Learning'), ('Online Articles', 'Online Articles'), ('Journals', 'Journals'), ('Teachers', 'Teachers'), ('Other', 'Other')], max_length=100, null=True)),
                ('What_is_your_average_family_monthly_income', models.CharField(choices=[('Above 60,000 ksh', 'Above 60,000 ksh'), ('40,000 - 50,000 ksh', '40,000 - 50,000 ksh'), ('20,000 - 40,000 ksh', '20,000 - 40,000 ksh'), ('1,000 - 20,000 ksh', '1,000 - 20,000 ksh'), ('Below 1,000 ksh', 'Below 1,000 ksh')], max_length=100, null=True)),
                ('What_is_your_highest_level_of_education_completed', models.CharField(choices=[('Kindergarten', 'Kindergarten'), ('Primary School', 'Primary School'), ('High School', 'High School'), ('Diploma', 'Diploma'), ('Bachelor Degree', 'Bachelor Degree'), ('Masters Degree', 'Masters Degree'), ('Doctorate', 'Doctorate'), ('Other', 'Other')], max_length=100, null=True)),
                ('Please_outline_any_community_work_you_have_undertaken', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='DEFAULT VALUE', upload_to='photos/')),
                ('heading', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500, null=True)),
                ('time', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Future_plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='DEFAULT VALUE', upload_to='photos/')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500, null=True)),
                ('location', models.CharField(max_length=50)),
                ('time_taken', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=150)),
                ('image', models.ImageField(default='DEFAULT VALUE', upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='DEFAULT VALUE', upload_to='photos/')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500, null=True)),
                ('location', models.CharField(max_length=50)),
                ('time_taken', models.CharField(max_length=20)),
            ],
        ),
    ]
