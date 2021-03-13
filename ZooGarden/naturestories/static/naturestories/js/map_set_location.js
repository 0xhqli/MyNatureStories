function initMap(){
    // MAP OPTIONS
    var options = {
        zoom : 16,
        center : {lat: 34.1480, lng: -118.2860}
    }
    // NEW MAP
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

    google.maps.event.addListener(marker, 'drag', function() {
        let [lat,lng]=[marker.getPosition().lat(),marker.getPosition().lng()]
        console.log(lat,lng)
        $('#id_lat').val(lat)
        $('#id_lng').val(lng)
    });
}