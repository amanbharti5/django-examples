from django.db import models
from django.forms import ModelForm

EXPTYPE_CHOICES = (
    ('S', 'SO'),
    ('AL', 'AL')
)

class Experiment(models.Model):
    name = models.CharField(max_length=100)
    experiment_type = models.CharField(max_length=2, choices=EXPTYPE_CHOICES)
    start_date = models.DateField(blank=True, null=True)
    def __unicode__(self):
        return self.name


class ExperimentForm(ModelForm):
    class Meta:
        model = Experiment
        fields = ['name', 'experiment_type','start_date']
