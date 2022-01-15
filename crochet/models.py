from django.db import models

# Create your models here.
class Hook(models.Model):
    metric_choices = ((1, '.75 mm'),(2, '.85 mm'), (3, '1 mm'), (4, '1.1 mm'), (5, '1.25 mm'), (6, '1.3 mm'), (7, '1.4 mm'), (8, '1.5 mm'), (9, '1.65 mm'), (10, '1.75 mm'), (11, '1.8 mm'), (12, '1.9 mm'), (13, '.75 mm'), (14, '2.1 mm'), (15, '2.25 mm'), (16, '2.5 mm'), (17, '2.75 mm'), (18, '3 mm'), (19, '3.25 mm'), (20, '3.5 mm'), (21, '3.75 mm'), (22, '4 mm'), (23, '4.25 mm'), (24, '4.5 mm'), (25, '5 mm'), (26, '5.5 mm'), (27, '6 mm'), (28, '6.5 mm'), (29, '7 mm'), (30, '7.5 mm'), (31, '8 mm'), (32, '9 mm'), (33, '10 mm'), (34, '12 mm'), (35, '15 mm'), (36, '16 mm'), (37, '19 mm'), (38, '25 mm'), )

    us_choices = ((15,'Size B/1'), (17,'Size C/2'), (19,'Size D/3'), (20,'Size E/4'), (21,'Size F/5'), (22,'Size G/6'), (24,'Size 7'), (25,'Size H/8'), (26,'Size I/9'), (27,'Size J/10'), (28,'Size K/10.5'), (31,'Size L/11'), (32,'Size M/13'), (33,'Size N/15'), (35,'Size P'), (36,'Size Q'), (37,'Size S'), (38, 'Size U'))

    hook_choices = [('Metric', metric_choices), ('US', us_choices)]

    size = models.IntegerField(choices=hook_choices)
    hook_image = models.ImageField(upload_to='hooks')
    def __str__(self):
        return self.get_size_display()