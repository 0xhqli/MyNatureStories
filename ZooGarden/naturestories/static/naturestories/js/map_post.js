var center_map
var set_marker
var center_marker_on_map
function initMap(){
    // MAP OPTIONS
    var options = {
        zoom : 16,
        center : {lat: 34.1480, lng: -118.2860},
        draggable:false,
        mapTypeControl: false
    }
    let map = new google.maps.Map(document.getElementById('map'),options);

    let marker=new google.maps.Marker({
        position: {lat: 34.1480,lng: -118.2841},
        map: map,
        title:"Sit Spot Marked",
        icon : '/static/naturestories/img/ezgif-3-c836094dc4ce.gif'
    });
    var infoWindow = new google.maps.InfoWindow({
        content:'<span>This was spotted here!</span>'
    });
    marker.addListener('click', function(){
        infoWindow.open(map, marker);
    });
    map.addListener("center_changed", () => {
        // 3 seconds after the center of the map has changed, pan back to the
        // marker.
        window.setTimeout(() => {
            map.panTo(marker.getPosition());
        }, 3000);
    });
    

    google.maps.event.addListener(marker, 'drag', function() {
        let [lat,lng]=[marker.getPosition().lat(),marker.getPosition().lng()];
        console.log(lat,lng);
    });
    center_map=(lat,lng)=>map.setCenter({lat, lng})
    set_marker=(lat,lng)=>{$('#id_lat').val(lat);$('#id_lng').val(lng);return marker.setPosition({lat, lng})}
    center_marker_on_map=()=>{
        let l=map.getCenter();
        set_marker(l.lat(),l.lng())
    }
}
function setLocation() {
    center_map(lati,lngi)
    center_marker_on_map()
}
$("document").ready(setLocation)