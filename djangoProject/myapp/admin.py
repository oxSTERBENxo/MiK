from django.contrib import admin
from .models import Country, Question, Choice, Polaroid, Song


# Register your models here.

class CountryQuestionInline(admin.TabularInline):
    model = Question
    extra = 0


class CountryPolaroidInline(admin.TabularInline):
    model = Polaroid
    extra = 0

class QuestionChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    fields = ['content', 'is_correct']


class CountryAdmin(admin.ModelAdmin):
    inlines = [CountryQuestionInline, CountryPolaroidInline, ]
    list_display = ("name",)

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True



class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionChoiceInline, ]
    list_display = ("country", "content",)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("question","content",)

class PolaroidAdmin(admin.ModelAdmin):
    list_display = ("country", "headline", "explanation")
    fields = ("country", "headline", "photo", "explanation")

class SongAdmin(admin.ModelAdmin):
    list_display = ("country", "file")
    fields = ("country", "file")




admin.site.register(Country, CountryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Polaroid, PolaroidAdmin)
admin.site.register(Song, SongAdmin)
