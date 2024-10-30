from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255, null=True)
    video_file = models.FileField(upload_to='videos/', null=True)

    def __str__(self):
        return self.title or 'Untitled Video'


class SlideshowImage(models.Model):
    image = models.ImageField(upload_to='slideshow/', null=True, blank=True)
    caption = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.caption if self.caption else "Slideshow Image"


class Tour(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    hero_image = models.ImageField(upload_to='hero_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name or "Default string"


class Gallery(models.Model):
    tour = models.ForeignKey(Tour, related_name='gallery', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='gallery/', null=True, blank=True)

    def __str__(self):
        return f"Gallery Image for {self.tour.name if self.tour else 'No Tour'}"


class Review(models.Model):
    tour = models.ForeignKey(Tour, related_name='reviews', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Review by {self.name if self.name else 'Anonymous'} for {self.tour.name if self.tour else 'No Tour'}"


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name if self.name else 'No Name'


class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField(null=True)

    def __str__(self):
        if self.tour:
            return f"{self.customer_name} - {self.tour.name}"
        return f"{self.customer_name} - Tour not assigned"


class AboutUs(models.Model):
    mission = models.TextField(null=True, blank=True)
    expert_guides = models.TextField(null=True, blank=True)
    personalized_itineraries = models.TextField(null=True, blank=True)
    authentic_experiences = models.TextField(null=True, blank=True)
    our_story = models.TextField(null=True, blank=True)
    why_choose_armenia = models.TextField(null=True, blank=True)

    def __str__(self):
        return "About Us Page Content"
