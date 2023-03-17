from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done')
    )
    summary = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')
    is_finished = models.BooleanField(default=False)

    def delete(self, using=None, keep_parents=False):
        self.is_finished = True
        self.save(using=using)

    def undelete(self):
        self.is_finished = False
        self.save()

    def __str__(self):
        return f'{self.summary}, {self.description} {self.status}'


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    tasks_id = models.ManyToManyField(Task, related_name='projects')

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()
        self.tasks.update(is_finished=True)

    def undelete(self):
        self.is_deleted = False
        self.save()

    def __str__(self):
        return f'{self.name} - {self.description}'
