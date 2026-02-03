from django.contrib import admin
from .models import SuperHeroType,HeroReview,hero_work_permit,heroBranch


# Register your models here.


class HeroReviewInline(admin.TabularInline):
    model =HeroReview
    extra = 1
    
    
class SuperHeroTypeAdmin(admin.ModelAdmin):
 list_display =('name','location','joined_at')
 inlines =[HeroReviewInline]


class heroBranchAdmin(admin.ModelAdmin):
    list_display =('branch_name','location')
    filter_horizontal =['available_hero']
    
    
class hero_work_permitAdmin(admin.ModelAdmin):
    list_display =('hero','permit_number','issue_date','valid_until')    

admin.site.register(SuperHeroType,SuperHeroTypeAdmin)
admin.site.register(hero_work_permit,hero_work_permitAdmin)
admin.site.register(heroBranch,heroBranchAdmin)
# admin.site.register()
