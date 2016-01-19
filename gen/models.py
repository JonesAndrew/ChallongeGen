from django.db import models

class Player(models.Model):
    mu = models.DecimalField(max_digits=52, decimal_places=48)
    sigma = models.DecimalField(max_digits=52, decimal_places=48)
    name = models.CharField(max_length=24,unique=True)
    Swins = models.IntegerField(default=0);
    Slosses = models.IntegerField(default=0);
    Gwins = models.IntegerField(default=0);
    Glosses = models.IntegerField(default=0);

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            c = cls()
            c.save()
            return c

class Tournament(models.Model):
    name = models.CharField(max_length=24,unique=True)

class TournamentList(SingletonModel):
    tournaments = models.ManyToManyField(Tournament)

# Create your models here.
