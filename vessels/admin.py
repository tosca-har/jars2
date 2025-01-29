from django.contrib import admin
from .models import Vessel, Vesselgroup, Site, Sitegroup, Report, Feature, Image

class ReportAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)
    
admin.site.register(Report, ReportAdmin)

class FeatureAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)
    
admin.site.register(Feature, FeatureAdmin)


class ImageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)
    
admin.site.register(Image, ImageAdmin)

class VesselAdmin(admin.ModelAdmin):
    list_filter = ("vesselgroup",)
    list_display = ("name", "form", "region",)
    ordering = ('name',)
    show_facets = admin.ShowFacets.ALWAYS

admin.site.register(Vessel, VesselAdmin)

class SiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("sitegroup",)
    list_display = ("name",)
    ordering = ('name',)
    show_facets = admin.ShowFacets.ALWAYS
    
admin.site.register(Site, SiteAdmin)

class SitegroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)
    
admin.site.register(Sitegroup, SitegroupAdmin)

class VesselgroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)
    list_filter = ("sitegroup",)
    
admin.site.register(Vesselgroup, VesselgroupAdmin)
