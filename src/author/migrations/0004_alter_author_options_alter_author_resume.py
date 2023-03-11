# Generated by Django 4.1.7 on 2023-03-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("author", "0003_rename_link_author_resume"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={
                "verbose_name": "Информация об авторе",
                "verbose_name_plural": "Информация об авторе",
            },
        ),
        migrations.AlterField(
            model_name="author",
            name="resume",
            field=models.URLField(verbose_name="Ссылки на резюме"),
        ),
    ]