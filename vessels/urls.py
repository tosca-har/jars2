from django.urls import path, include
from . import views
app_name = 'vessels'

urlpatterns = [
    path("", views.home, name="home"),
    path("map", views.map, name="map"),
    path("search", views.search, name="search"),
    path("compare", views.compare, name="compare"),
    path("glossary", views.glossary, name="glossary"),
    path("vessel_<slug:slug>", views.vessel, name="vessel"),
    path("vesselgroup_<slug:slug>", views.vesselgr, name="vesselgr"),
    path("report_<slug:slug>", views.report, name="report"),
    path("site_<slug:slug>", views.site, name="site"),
    path("sitegroup_<slug:slug>", views.sitegr, name="sitegr"),
    
]
