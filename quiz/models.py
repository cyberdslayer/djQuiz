from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
import datetime







# basemodel is the base class for all models in the application.
# It provides a primary key field and a model manager.
# We will be using nase class for all models in the application.
# dry code principle: DRY (Don't Repeat Yourself)
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # For registering it as base class for all models in the application.
    class  Meta:
        abstract = True
        # ordering = ['-created_at', '-updated_at']
        
# category model
# Importing it from base model instead of models.Model
class Category(models.Model):    
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


# Quiz model
class Quizzes(BaseModel):

    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')
        ordering = ['-created_at', '-updated_at']

    title = models.CharField(max_length=100, default= _('New Quiz'), verbose_name= _('Quiz Title')  )


    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)


# quesion model
class Question(models.Model):
    quiz = models.ForeignKey(Quizzes,related_name='question', on_delete=models.DO_NOTHING)
    # cate = models.ForeignKey(Category,  on_delete=models.CASCADE)
    ques = models.CharField(max_length=100)
    marks = models.IntegerField(default=4)

# answer model
class Answer(models.Model):
    ques = models.ForeignKey(Question, related_name="answer"  , on_delete=models.DO_NOTHING)
    ans = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)


