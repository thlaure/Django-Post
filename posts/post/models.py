from django.db import models
# from django.urls import reverse
# from django.template.defaultfilters import slugify


# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     slug = models.SlugField(unique=True, max_length=200)

#     def get_absolute_url(self):
#         return reverse('blog_post_detail', args=[self.slug])
    
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super(Post, self).save(*args, **kwargs)