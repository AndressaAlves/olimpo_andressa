from django.db import models
from accounts.models import User

class Topic(models.Model):
    title =  models.CharField('Título',max_length = 150)
    body = models.TextField('Mensagem')
    author  = models.ForeignKey(User, verbose_name ='Autor',related_name='topic')
    views = models.IntegerField('Visualizações',blank=True, default=0)
    answers = models.IntegerField('Respostas',blank=True, default=0)
    created = models.DateTimeField('Criado em',auto_now_add = True)
    update = models.DateTimeField('Atualizado em',auto_now=True)

    def __str__(self):
        return self.title

    class  Meta:
        verbose_name = 'Tópico'
        verbose_name_plural = 'Tópicos'
        ordering = ['-update']

class reply(models.Model):
    topic = models.ForeignKey(Topic, verbose_name='Tópico',related_name='replies')
    reply = models.TextField('Mensagem')
    author  = models.ForeignKey(User, verbose_name ='Autor',related_name='replies')
    correct = models.BooleanField('Correta?',blank=True,default=False)
    created = models.DateTimeField('Criado em',auto_now_add = True)
    update = models.DateTimeField('Atualizado em',auto_now=True)

    def __str__(self):
        return self.reply[:100]

    class  Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'
        ordering = ['correct','created']

def post_save_reply(created,instance,**kwargs):
    instance.topic.answers = instance.topic.replies.count()
    instance.topic.save()
    if instance.correct:
        instance.topic.replies.exclude(pk=instance.pk).update(correct="False")

def post_delete_reply(instance,**kwargs):
    instance.topic.answers = instance.topic.replies.count()

models.signals.post_save.connect(
    post_save_reply,sender = reply,dispatch_uid = 'post_save_reply'
)


models.signals.post_delete.connect(
    post_delete_reply, sender = reply,dispatch_uid = 'post_delete_reply'
)

# Create your models here.
