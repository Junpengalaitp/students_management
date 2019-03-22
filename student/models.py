from django.db import models


class Student(models.Model):
    SEX_ITEMS = [
        (1, 'Male'),
        (2, 'Female'),
        (0, 'Unknown')
    ]

    STATUS_ITEMS = [
        (0, 'Apply'),
        (1, 'Pass'),
        (2, 'Denine'),
    ]
    name = models.CharField(max_length=128)
    sex = models.IntegerField(choices=SEX_ITEMS)
    profession = models.CharField(max_length=128)
    email = models.EmailField(verbose_name='Email')
    qq = models.CharField(max_length=128, verbose_name='QQ')
    phone = models.CharField(max_length=128)
    status = models.IntegerField(choices=STATUS_ITEMS, default=0)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '<Student: {}>'.format(self.name)

    class Meta:
        verbose_name, verbose_name_plural = 'Student', 'Students'
