from django.db import migrations, models
from django.conf import settings

class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='Task',
            name='user',
            field=models.ForeignKey(
                on_delete=models.CASCADE,
                related_name='tasks',
                to=settings.AUTH_USER_MODEL,
                null=True,
            ),
        ),
    ]