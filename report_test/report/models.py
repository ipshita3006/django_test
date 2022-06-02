from django.db import models
from django.db.models import Count

class VisitManager(models.Manager):
    def get_visits_by_user(self):
        return self.get_queryset().values('policy_id__user_id__name').annotate(count=Count('policy_id'))


class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False, unique=True)
    is_active = models.BooleanField(default=True)


class Policy(models.Model):
    user_id = models.OneToOneField(User, related_name="policy", on_delete=models.CASCADE)
    hash_id = models.CharField(unique=True, null=False, max_length=10)
    start_date = models.DateField(auto_now=True)
    state = models.CharField(max_length=20)


class Page(models.Model):
    name = models.CharField(max_length=100)


class Visit(models.Model):
    policy_id = models.ForeignKey(Policy, related_name="visits", on_delete=models.CASCADE)
    page_id = models.ForeignKey(Page, related_name="visits", on_delete=models.CASCADE)

    objects = VisitManager()
