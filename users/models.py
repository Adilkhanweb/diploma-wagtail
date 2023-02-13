from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    class Roles(models.TextChoices):
        STUDENT = "STUDENT", _("Student")
        TEACHER = "TEACHER", _("Teacher")

    base_role = Roles.STUDENT

    role = models.CharField(_("Role"), max_length=20, choices=Roles.choices, default=base_role, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.role = self.base_role
        return super().save(*args, **kwargs)


class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.STUDENT)


class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.TEACHER)


class Student(User):
    base_role = User.Roles.STUDENT

    objects = StudentManager()

    class Meta:
        proxy = True


class Teacher(User):
    base_role = User.Roles.TEACHER

    objects = TeacherManager()

    class Meta:
        proxy = True
