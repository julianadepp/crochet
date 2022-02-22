from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def image_size(image):
    max=1024*500 #500kb
    if image.size > max:
        raise ValidationError('Image must be 500kb or less!')

class Hook(models.Model):
    metric_choices = ((1, '.75 mm'),(2, '.85 mm'), (3, '1 mm'), (4, '1.1 mm'), (5, '1.25 mm'), (6, '1.3 mm'), (7, '1.4 mm'), (8, '1.5 mm'), (9, '1.65 mm'), (10, '1.75 mm'), (11, '1.8 mm'), (12, '1.9 mm'), (13, '.75 mm'), (14, '2.1 mm'), (15, '2.25 mm'), (16, '2.5 mm'), (17, '2.75 mm'), (18, '3 mm'), (19, '3.25 mm'), (20, '3.5 mm'), (21, '3.75 mm'), (22, '4 mm'), (23, '4.25 mm'), (24, '4.5 mm'), (25, '5 mm'), (26, '5.5 mm'), (27, '6 mm'), (28, '6.5 mm'), (29, '7 mm'), (30, '7.5 mm'), (31, '8 mm'), (32, '9 mm'), (33, '10 mm'), (34, '12 mm'), (35, '15 mm'), (36, '16 mm'), (37, '19 mm'), (38, '25 mm'), )

    us_choices = ((15,'Size B/1'), (17,'Size C/2'), (19,'Size D/3'), (20,'Size E/4'), (21,'Size F/5'), (22,'Size G/6'), (24,'Size 7'), (25,'Size H/8'), (26,'Size I/9'), (27,'Size J/10'), (28,'Size K/10.5'), (31,'Size L/11'), (32,'Size M/13'), (33,'Size N/15'), (35,'Size P'), (36,'Size Q'), (37,'Size S'), (38, 'Size U'))

    hook_choices = [('Metric', metric_choices), ('US', us_choices)]

    size = models.IntegerField(choices=hook_choices)
    hook_image = models.ImageField(upload_to='hooks', validators=[image_size])
    def __str__(self):
        return self.get_size_display()

class Stitch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    pattern_code = models.CharField(max_length=20, default='no code')
    instructions = models.TextField()
    notes = models.TextField()
    related_stitches = models.ManyToManyField('self', null=True, blank=True,related_name='stitch')
    stitch_image = models.ImageField(upload_to='stitches')
    def __str__(self):
        return self.name

class Yarn(models.Model):
    lace = (0, '0 - Lace')
    superfine = (1, '1 - Superfine')
    fine = (2, '2 - Fine')
    light = (3, '3 - Light')
    medium = (4, '4 - Medium')
    bulky = (5, '5 - Bulky')
    super = (6, '6 - Super Bulky')
    jumbo = (7, '7 - Jumbo')
    weight_choices = (lace, superfine, fine, light, medium, bulky, super, jumbo)

    nickname = models.CharField(max_length=100, help_text='This is how your yarn will be referenced around the site! Could be the brand or something you associate with the yarn, like "Chunky Wool Yarn".')
    weight = models.IntegerField(choices=weight_choices, max_length=100,)
    weight_description = models.CharField(max_length=100, blank=True, help_text='please include any simple specifcs you would like here. For instance, weight choice <em>3 - Light</em> might include "DK, light worsted" here.')
    material = models.CharField(max_length=100,)
    brand = models.CharField(max_length=200, blank=True)
    notes = models.TextField(default='No notes.',)
    suggested_hooks = models.ManyToManyField(Hook, related_name='yarns', null=True, blank=True,)
    yarn_image = models.TextField(default='https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/yarn-ball-karl-addison.jpg', help_text='this should be a link that leads to the image alone. To get this, find an image you like on the internet, then right click and select "Open Image in New Tab". Go to the newly opened tab and copy the full address from the browser address bar, then paste it here!')
    def __str__(self):
        return self.nickname

class Gauge(models.Model):
    title = models.CharField(max_length=100)
    yarn = models.ForeignKey(Yarn, on_delete=models.PROTECT, related_name='gauges')
    hook = models.ForeignKey(Hook, on_delete=models.PROTECT, related_name='gauges')
    stitch = models.ForeignKey(Stitch, on_delete=models.PROTECT, related_name='gauges')
    number_of_stitches = models.DecimalField(max_digits=5, decimal_places=2 )
    notes = models.TextField()
    gauge_image = models.ImageField(upload_to='gauges')
    def __str__(self):
        return self.title

class Pattern(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    notes = models.TextField()
    stitches = models.ManyToManyField(Stitch, related_name='patterns')
    yarn = models.ManyToManyField(Yarn, related_name='patterns')
    hook = models.ForeignKey(Hook, on_delete=models.PROTECT, related_name='patterns')
    gauge = models.ForeignKey(Gauge, on_delete=models.PROTECT, related_name='patterns')
    pattern_image = models.ImageField(upload_to='patterns')
    def __str__(self):
        return self.name