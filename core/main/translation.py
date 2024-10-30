
from .models import Tour,Video,SlideshowImage,AboutUs
from modeltranslation.translator import register, TranslationOptions

@register(Tour)
class TourTranslationOptions(TranslationOptions):
    fields = ('name','description','duration','location',)



@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)



@register(SlideshowImage)
class SlideshowImageTranslationOptions(TranslationOptions):
    fields = ('caption',)



@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = (
        'mission',
        'expert_guides',
        'personalized_itineraries',
        'authentic_experiences',
        'our_story',
        'why_choose_armenia',
    )