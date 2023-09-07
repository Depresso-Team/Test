from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sessions.models import Session
# Create your models here.


# List of languages
LANGUAGES = [
    ("en", "English"),
    ("es", "Spanish"),
    ("fr", "French"),
    ("de", "German"),
    ("it", "Italian"),
    ("pt", "Portuguese"),
    ("nl", "Dutch"),
    ("ru", "Russian"),
    ("ja", "Japanese"),
    ("zh-cn", "Chinese (Simplified)"),
    ("ar", "Arabic"),
    ("hi", "Hindi"),
    ("ko", "Korean"),
    ("tr", "Turkish"),
    ("pl", "Polish"),
    ("uk", "Ukrainian"),
    ("cs", "Czech"),
    ("sv", "Swedish"),
    ("ro", "Romanian"),
    ("hu", "Hungarian"),
    ("vi", "Vietnamese"),
    ("el", "Greek"),
    ("th", "Thai"),
    ("he", "Hebrew"),
    ("id", "Indonesian"),
    ("da", "Danish"),
    ("fi", "Finnish"),
    ("no", "Norwegian"),
    ("bn", "Bengali"),
    ("ta", "Tamil"),
    ("hr", "Croatian"),
    ("fa", "Persian"),
    ("sk", "Slovak"),
    ("sl", "Slovenian"),
    ("ms", "Malay"),
    ("et", "Estonian"),
    ("lt", "Lithuanian"),
    ("lv", "Latvian"),
    ("sr", "Serbian"),
    ("sw", "Swahili"),
    ("tl", "Tagalog"),
    ("is", "Icelandic"),
    ("ka", "Georgian"),
    ("hy", "Armenian"),
    ("ur", "Urdu"),
    ("uz", "Uzbek"),
    ("kk", "Kazakh"),
    ("az", "Azerbaijani"),
    ("ky", "Kyrgyz"),
    ("bn", "Bengali"),
    ("gu", "Gujarati"),
    ("mr", "Marathi"),
    ("ne", "Nepali"),
    ("pa", "Punjabi"),
    ("si", "Sinhala"),
    ("ta", "Tamil"),
    ("te", "Telugu"),
    ("ml", "Malayalam"),
    ("kn", "Kannada"),
    ("or", "Odia"),
    ("as", "Assamese"),
    ("my", "Burmese"),
    ("dz", "Dzongkha"),
    ("km", "Khmer"),
    ("lo", "Lao"),
    ("mn", "Mongolian"),
    ("my", "Burmese"),
    ("ne", "Nepali"),
    ("ps", "Pashto"),
    ("sd", "Sindhi"),
    ("tg", "Tajik"),
    ("tk", "Turkmen"),
    ("ug", "Uighur"),
    ("ur", "Urdu"),
    ("yi", "Yiddish"),
]



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.PositiveIntegerField(unique=True , null=True)
    address = models.CharField(max_length=150)
    country_code = models.PositiveIntegerField(null=True)
    photo_url = models.URLField(max_length=255)
    languages = languages = models.CharField(max_length=50, choices=LANGUAGES)
    session_message = models.CharField(max_length=200, blank=True, null=True)
    is_guide = models.BooleanField(default=False)



    def __str__(self):
        return self.username
    

# Signal for handling user creation
@receiver(post_save, sender=CustomUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        message = f"New user '{instance.username}' has been created! Welcome aboard!"
        instance.session_message = message
        instance.save()
    

class Guide(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    rate = models.FloatField(default=0.0)
    reviews = models.TextField(max_length=255)
    photos = models.ImageField(upload_to=None)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username
    
# Signal to create a Guide object when a CustomUser with is_guide=True is created
@receiver(post_save, sender=CustomUser)
def create_guide(sender, instance, created, **kwargs):
    if created and instance.is_guide:
        Guide.objects.create(user=instance)