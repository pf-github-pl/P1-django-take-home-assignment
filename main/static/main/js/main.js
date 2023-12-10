function getLocation() {
    var latitude, longitude;

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(success, error, {timeout:10000, enableHighAccuracy: true, maximumAge:0});
    }

    function success(position) {
        latitude = position.coords.latitude;
        longitude = position.coords.longitude;

        var latInput = document.getElementById('id_latitude');
        var lonInput = document.getElementById('id_longitude');

        if (latInput && lonInput) {
            latInput.value = latitude.toFixed(7);
            lonInput.value = longitude.toFixed(7);
        }
    }

    function error() {
        console.log('Unable to retrieve location data');
        document.getElementById('feedback').textContent = 'Unable to retrieve location data';
    }
}
