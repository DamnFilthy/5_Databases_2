# Generated by Django 3.1.2 on 2021-02-17 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20210217_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='articles',
            field=models.ManyToManyField(related_name='scopes', through='articles.ArticleScope', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='scope',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.scope'),
        ),
    ]
