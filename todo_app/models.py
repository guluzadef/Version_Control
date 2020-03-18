from django.db import models
from base_user.models import MyUser

User = MyUser

# Create your models here.
from django.db.models import Max


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    version = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id},{self.text},{self.desc}'


class UpdatedPosts(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    version = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.post},VERSION: {self.version}'


class Example(models.Model):
    title = models.SlugField()
    version = models.PositiveSmallIntegerField()
    content = models.TextField(blank=True)

    class Meta:
        unique_together = (
            ('title', 'version'),
        )

    def _highest_version(self):
        return Example.objects.filter(title=self.title).aggregate(Max('version'))['version__max'] or 0

    def save(self):
        if self.version is None:
            self.version = self._highest_version() + 1
        return super().save()
