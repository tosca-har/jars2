getMap = function () {    
    let tfAttr = 'Maps &copy; <a href="https://www.thunderforest.com">Thunderforest</a>, Data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>';
    let mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>';
    let tfUrl = 'https://tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey='+ thsu;
    let mbUrl = 'https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token='+ mbsu;
    let mbSUrl = 'https://api.mapbox.com/styles/v1/mapbox/satellite-v9/tiles/{z}/{x}/{y}?access_token=' + mbsu;

    let landscape = L.tileLayer(tfUrl, {maxZoom: 22, attribution: tfAttr});
    let streets = L.tileLayer(mbUrl, {tileSize: 512, zoomOffset: -1, attribution: mbAttr});
    let satellite = L.tileLayer(mbSUrl, {tileSize: 512, zoomOffset: -1, attribution: mbAttr});
    let sites = L.featureGroup();
    let prod = L.featureGroup();
    let noinfo = L.featureGroup();

    var potIcon = L.icon({
        iconUrl: picon,
        iconSize: [15, 20]
    });
    var potIconB = L.icon({
        iconUrl: bicon,
        iconSize: [15, 20]
    });
    var potIconG = L.icon({
        iconUrl: grcon,
        iconSize: [15, 20]
    });
    let map = L.map('map', {
        center: mapcentre,
        zoom: 4.5,
        layers: [streets, sites, prod, noinfo]
    });

    let baseLayers = {
        'Landscape': landscape,
        'Satellite': satellite,
        'Streets': streets
    };

    for (var i = 0; i < siteNames.length; i += 1) {
        sitename = siteNames[i];
        sitelink = siteLinks[i];
        siteVes = siteVessels[i];
        complex = "<a href=" +sitelink+">"+sitename+ "</a>" + siteVes;
        if (siteColour[i] == 0) {
            marker = L.marker([siteLat[i],siteLng[i]],{icon: potIconB, title: sitename, link: sitelink, ves: siteVes}).bindPopup(complex).on("click", markerOnClick).addTo(sites);
        } else if (siteColour[i] == 1) {
            marker = L.marker([siteLat[i],siteLng[i]],{icon: potIcon, title: sitename, link: sitelink, ves: siteVes}).bindPopup(complex).on("click", markerOnClick).addTo(prod);
        }
        else {
            marker = L.marker([siteLat[i],siteLng[i]],{icon: potIconG, title: sitename, link: sitelink, ves: siteVes}).bindPopup(complex).on("click", markerOnClick).addTo(noinfo);
        }
           
    } 
    let overlays = {}
    overlays = {
        'Production': prod,
        'Import': sites,
        'No Info': noinfo
        }; 

    var layerControl = L.control.layers(baseLayers, overlays).addTo(map);
   
  }

  function markerOnClick(e) {
    targetSite = this.options.title;
    targetLink = this.options.link;
    targetVessels = this.options.ves;
    document.getElementById("targetSite").innerHTML = "Site selected: <a href=" +targetLink+">"+targetSite+ "</a>." +targetVessels ; 
        
}

