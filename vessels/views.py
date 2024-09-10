from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from decouple import config
from .models import Vessel, Vesselgroup, Site, Sitegroup, Report

mbsu = config('MBSU')
thsu = config('THSU')

def home(request):
    return render(request, "vessels/home.html")

def index(request):
    vesselgroups = Vesselgroup.objects.all().order_by("name")
    return render(request, "vessels/index.html", {
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
    id_vess = identified_vg.vessels.all()
    return render(request, "vessels/vesselgr.html", {
        "groups": identified_vg,
        "vg_vessels": id_vess,
        "vg_sg": identified_vg.sitegroup.all()
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
        "vessels": identified_v.vessel.all()
    })


def vessel(request, slug):
    identified_v = get_object_or_404(Vessel, slug=slug)
    return render(request, "vessels/vessel.html", {
        "the_vessel": identified_v,
        "v_ref": identified_v.refs.all()
    })

def glossary(request):
    return render(request, "vessels/glossary.html")