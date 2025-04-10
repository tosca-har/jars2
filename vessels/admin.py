from django.contrib import admin
from .models import Vessel, Vesselgroup, Site, Report, Feature, Image, Fabric

class FabricAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)
    
admin.site.register(Fabric, FabricAdmin)

class ReportAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)
    
admin.site.register(Report, ReportAdmin)

class FeatureAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)
    list_display = ("name", "type",)
admin.site.register(Feature, FeatureAdmin)


class ImageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)
    
admin.site.register(Image, ImageAdmin)

class VesselAdmin(admin.ModelAdmin):
    list_filter = ("vesselgroup",)
    list_display = ("name", "region",)
    ordering = ('name',)
    show_facets = admin.ShowFacets.ALWAYS

admin.site.register(Vessel, VesselAdmin)

class SiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name",)
    ordering = ('name',)
    show_facets = admin.ShowFacets.ALWAYS
    
admin.site.register(Site, SiteAdmin)

class VesselgroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)
    
admin.site.register(Vesselgroup, VesselgroupAdmin)
