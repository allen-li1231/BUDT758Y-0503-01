
  function initMap() {
    // Basic options for a simple Google Map
    // For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
    // var myLatlng = new google.maps.LatLng(40.71751, -73.990922);
    var lot1Latlng = {lat:38.983083, lng:-76.947038};
    var pptLatlng = {lat:{{ property_info.cmtid.cmtlatitude}}, lng:{{ property_info.cmtid.cmtlongitude}}};
    var mapOptions = {
        // How zoomed in you want the map to start at (always required)
        zoom: 13,

        // The latitude and longitude to center the map (always required)
        center: {lat:(lot1Latlng.lat+pptLatlng.lat) / 2, lng:(lot1Latlng.lng+pptLatlng.lng) / 2},
		
		styles: [
            {
                "featureType": "administrative.country",
                "elementType": "geometry",
                "stylers": [
                    {
                        "visibility": "simplified"
                    },
                    {
                        "hue": "#ff0000"
                    }
                ]
            }
        ]
    };

    // Get the HTML DOM element that will contain your map 
    // We are using a div with id="map" seen below in the <body>
    var mapElement = document.getElementById('pills-manufacturer');

    // Create the Google Map using out element and options defined above
    var map = new google.maps.Map(mapElement, mapOptions);
	var lot1Marker = new google.maps.Marker({position: lot1Latlng, map: map, draggable: false});
	var pptMarker = new google.maps.Marker({position: pptLatlng, map: map, draggable: false, animation: google.maps.Animation.DROP});
	
	let directionsService = new google.maps.DirectionsService();
  let directionsRenderer = new google.maps.DirectionsRenderer({map: map});
  directionsRenderer.setMap(map); // Existing map object displays directions
  // Create route from existing points used for markers
  const route = {
      origin: lot1Latlng,
      destination: pptLatlng,
      travelMode: 'DRIVING'
  }

  directionsService.route(route,
    function(response, status) { // anonymous function to capture directions
      if (status !== 'OK') {
        window.alert('Directions request failed due to ' + status);
        return;
      } else {
        directionsRenderer.setDirections(response); // Add route to the map
        var directionsData = response.routes[0].legs[0]; // Get data about the mapped route
        if (!directionsData) {
          window.alert('Directions request failed');
          return;
        }
        else {
          //document.getElementById('map_distance').innerHTML += directionsData.distance.text + " (" + directionsData.duration.text + ").";
        }
      }
    });
  }