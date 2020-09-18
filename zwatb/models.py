from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=20, null=False, verbose_name='项目名称')
    desc = models.CharField(max_length=50, null=False, default='', verbose_name='项目详情')

    class Meta:
        db_table = "project"


class Case(models.Model):
    uid = models.IntegerField(null=False)
    name = models.CharField(max_length=50, null=False, verbose_name="case名称")
    page_path = models.CharField(max_length=50, null=False, verbose_name="case对应的页面路径")
    content = models.CharField(max_length=500, null=False, default='{}', verbose_name="case详情")
    status = models.BooleanField(null=False, default=1, verbose_name="case状态，1：正常，0：删除")
    create_time = models.DateTimeField(null=False, auto_now_add=True)
    project = models.ForeignKey(to="Project", verbose_name="所属项目", on_delete=models.CASCADE)

    class Meta:
        db_table = "case"


class Log(models.Model):
    uid = models.IntegerField(null=False)
    status = models.SmallIntegerField(
        choices=((2, '执行中'),(1,'已通过'),(0,'未通过')),
        null=False,
        default=0,
        verbose_name='用例执行状态'
    )
    create_time = models.DateTimeField(null=False, auto_now_add=True)
    project = models.ForeignKey(to="Project", verbose_name="所属项目", on_delete=models.CASCADE)

    class Meta:
        db_table = "log"