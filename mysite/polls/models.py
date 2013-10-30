from django.db import models



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text
    votes = models.IntegerField(default=0)




class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    age = models.IntegerField()

    def __unicode__(self):
        return "{0} {1} {2} {3} {4}".format(
            self, self.first_name, self.last_name, self.email, self.age)

class Book(models.Model):
    book_name=models.CharField(max_length=30)
    publisher_name=models.CharField(max_length=40)

    def __unicode__(self):
        return "{0} {1} {2}".format(
            self.pk, self.book_name, self.publisher_name)
