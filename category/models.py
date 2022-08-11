from django.db import models


def blog_directory_path(instance, filename):
	return 'category/{0}/{1}'.format(instance.name, filename)

class Category(models.Model):
	parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)

	name = models.CharField(max_length=250, unique=True)
	thumbnail = models.ImageField(upload_to=blog_directory_path, blank=True, null=True)

	class Meta:
		verbose_name='Category'
		verbose_name_plural='Categories'

	def __str__(self):
		return self.name

	def get_thumbnail(self):
		if self.thumbnail:
			return self.thumbnail.url 
		return ''

