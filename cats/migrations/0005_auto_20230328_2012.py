# Generated by Django 3.2 on 2023-03-28 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_achievement'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.achievement')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.cat')),
            ],
        ),
        migrations.AddField(
            model_name='cat',
            name='achievements',
            field=models.ManyToManyField(through='cats.AchievementCat', to='cats.Achievement'),
        ),
    ]