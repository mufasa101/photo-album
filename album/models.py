from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    # added_on = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #      ordering = ['-added_on']
       
    def __str__(self):
        return self.description