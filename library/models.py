from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_task'
        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_task_title')
        ]


class SubTask(models.Model):
    title = models.CharField(max_length=255, unique=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['-created_at']
        verbose_name = 'SubTask'
        verbose_name_plural = 'SubTasks'
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_subtask_title')
        ]


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_category_name')
        ]
