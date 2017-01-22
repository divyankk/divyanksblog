from django.db import models

# Create your models here.

class Post(models.Model):
    # Below are the four fields that will be used on home page to display
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        # This will return the title on the admin page to display the posts according to its title
        return self.title

    def pub_date_pretty(self):
        # This function will be used to display date in a specific format on home.html page
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        # This function will be used to return 100 characters from body field, we will use this in home.html page
        return self.body[:100]
