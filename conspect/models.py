from django.db.models import *



class SubjectModel(Model):
    name = CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ('name',)

    def __str__(self):
        return self.name


class StructureComponentModel(Model):
    subject = ForeignKey(SubjectModel, on_delete=CASCADE,
                         verbose_name='Предмет', related_name='structure_components')
    name = CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Структурный компонент'
        verbose_name_plural = 'Структурные компоненты'

    def __str__(self):
        return self.name


class AnswerModel(Model):
    structure_component = ForeignKey(StructureComponentModel, on_delete=CASCADE,
                                     verbose_name='Структурный компонент', related_name='answers')
    content = TextField(verbose_name='Вариант')

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

    def __str__(self):
        return self.content


class ConspectModel(Model):
    name = CharField(max_length=255, verbose_name='Название')
    owner = CharField(max_length=255, verbose_name='Автор')
    subjects = ManyToManyField(SubjectModel,
                               verbose_name='Предметы', related_name='conspects')
    structure_components = ManyToManyField(StructureComponentModel,
                                           verbose_name='Структурные компоненты', related_name='conspects')
    answers = ManyToManyField(AnswerModel, verbose_name='Ответы', related_name='conspects')
    date_created = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Конспект'
        verbose_name_plural = 'Конспекты'
        ordering = ('date_created',)

    def __str__(self):
        return f'{self.name}, Автор: {self.owner}'


class CustomAnswerModel(Model):
    conspect = ForeignKey(ConspectModel, on_delete=CASCADE,
                          verbose_name='Конспект', related_name='custom_answers')
    structure_component = ForeignKey(StructureComponentModel, on_delete=CASCADE,
                                     verbose_name='Структурный компонент', related_name='custom_answers')
    content = TextField(verbose_name='Вариант')

    class Meta:
        verbose_name = 'Свой вариант'
        verbose_name_plural = 'Свои варианты'

    def __str__(self):
        return self.content
