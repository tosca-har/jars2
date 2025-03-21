from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from decouple import config
from .models import Vessel, Vesselgroup, Site, Sitegroup, Report, Image, Feature

mbsu = config('MBSU')
thsu = config('THSU')

def home(request):
    return render(request, "vessels/home.html")

def search(request):
    vesselgroups = Vesselgroup.objects.all().order_by("name")
    return render(request, "vessels/search.html", {
        "groups": vesselgroups
    })

def compare(request):
    vesselgroups = Vesselgroup.objects.all().order_by("name")
    return render(request, "vessels/compare.html", {
        "groups": vesselgroups
    })
def map(request):
    sites = Site.objects.all().order_by("name")
    return render(request, "vessels/map.html", {
        "sites": sites,
        "mbsu": mbsu,
        "thsu":thsu
    })

def vesselgr(request, slug):
    identified_vg = get_object_or_404(Vesselgroup, slug=slug)
    vessels = identified_vg.vessels.all()
    return render(request, "vessels/vesselgr.html", {
        "groups": identified_vg,
        "vg_vessels": vessels,
        "vg_parents": identified_vg.vg_parent.all(),
        "images": Image.objects.all().filter(vessels__in=vessels).distinct(),
        "prod_sites": identified_vg.site.all(),
        "imp_sites": identified_vg.isite.all(),
        "vg_fabrics": identified_vg.fabric.all(),
        "v_ref": identified_vg.refs.all(),
        "mbsu": mbsu,
        "thsu":thsu
    })

def sitegr(request, slug):
    identified_vg = get_object_or_404(Sitegroup, slug=slug)
    id_sites = identified_vg.sites.all()
    return render(request, "vessels/sitegr.html", {
        "groups": identified_vg,
        "sites": id_sites
    })

def site(request, slug):
    identified_v = get_object_or_404(Site, slug=slug)
    return render(request, "vessels/site.html", {
        "site": identified_v,
        "vessels": identified_v.vessel.all(),
        "ivessels": identified_v.import_vessel.all(),
        "vesselgr": identified_v.vesselgroup.all(),
        "ivesselgr": identified_v.import_vesselgroup.all()
    })


def vessel(request, slug):
    identified_v = get_object_or_404(Vessel, slug=slug)
    return render(request, "vessels/vessel.html", {
        "the_vessel": identified_v,
        "fabrics": identified_v.fabric.all(),
        "vessel_images": identified_v.image.all(),
        "v_ref": identified_v.refs.all(),
        "vgr": identified_v.vesselgroup.all(),
        "typ_features": identified_v.typical_feature.all(),
        "com_features": identified_v.occasional_feature.all(),
        "prod_sites": identified_v.site.all(),
        "imp_sites": identified_v.isite.all(),
        "mbsu": mbsu,
        "thsu":thsu
    })
def report(request, slug):
    identified_r = get_object_or_404(Report, slug=slug)
    return render(request, "vessels/report.html", {
        "report": identified_r,
    })
def glossary(request):
    return render(request, "vessels/glossary.html")