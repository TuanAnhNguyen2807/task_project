from django.db import migrations

def create_sample_tasks(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Task = apps.get_model('task_manager', 'Task')

    # Get all users (or specific ones if needed)
    users = User.objects.all()

    for user in users:
        tasks = []
        for i in range(1, 50):
            tasks.append(Task(
                user=user,
                title=f"Hi test {i}",
                description=f"Hi test {i}",
                is_completed=False,
            ))
        Task.objects.bulk_create(tasks)

def delete_sample_tasks(apps, schema_editor):
    Task = apps.get_model('task_manager', 'Task')
    Task.objects.filter(title__startswith="Hi test").delete()

class Migration(migrations.Migration):
    dependencies = [
        ('task_manager', '0003_remove_task_user'),
    ]


    operations = [
        migrations.RunPython(create_sample_tasks, delete_sample_tasks),
    ]
