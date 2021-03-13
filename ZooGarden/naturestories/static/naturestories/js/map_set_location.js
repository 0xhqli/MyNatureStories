var center_map;
var set_marker;
var center_marker_on_map;
var marker_set_loc;
function initMap(){
    // MAP OPTIONS
    var options = {
        zoom : 16,
        center : {lat: 34.1480, lng: -118.2860}
    }
    var map = new google.maps.Map(document.getElementById('map'),options);

    var marker=new google.maps.Marker({
        position: {lat: 34.1480,lng: -118.2841},
        map: map,
        draggable: true,
        title:"Take me to Your Sit Spot!",
        icon : '/static/naturestories/img/ezgif-3-c836094dc4ce.gif'
    });
    var infoWindow = new google.maps.InfoWindow({
        content:'<h4>Did you see them here?</h4>'
    });
    marker.addListener('click', function(){
        infoWindow.open(map, marker);
    });
    marker_set_loc=()=>{
        var [lat,lng]=[marker.getPosition().lat(),marker.getPosition().lng()];
        console.log(lat,lng);
        $('#id_lat').val(lat);
        $('#id_lng').val(lng);
    }
    google.maps.event.addListener(marker, 'drag', marker_set_loc);
    center_map=(lat,lng)=>map.setCenter({lat, lng})
    set_marker=(lat,lng)=>{$('#id_lat').val(lat);$('#id_lng').val(lng);return marker.setPosition({lat, lng})}
    center_marker_on_map=()=>{
        var l=map.getCenter();
        set_marker(l.lat(),l.lng())
    }
    marker_set_loc();
}
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((pos)=>{
            center_map(pos.coords.latitude,pos.coords.longitude)
            center_marker_on_map()
        });
    }
}
// $("document").ready()
var user_get_location=()=>{console.log("getting location");marker_set_loc();getLocation();}