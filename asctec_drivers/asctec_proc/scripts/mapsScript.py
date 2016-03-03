#!/usr/bin/python

html = """
<!DOCTYPE html>
    <html>
      <head>
        <style>
          html, body, #map-canvas {
            height: 100%;
            margin: 0px;
            padding: 0px
          }
        </style>

        <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&libraries=drawing"></script>
        <script src="http://google-maps-utility-library-v3.googlecode.com/svn/trunk/markerwithlabel/src/markerwithlabel.js"></script>
        <script language="JavaScript">
          var marker = 'undefined';
          var waypoint = [];
          var flightPath = 'undefined'
          var flightPlanCoordinates = []
          var map = 'undefined';


          /* Initialize function */
          /**************************************************************************/
          function initialize() {
            var mapOptions = {
              center: new google.maps.LatLng(-19.8695912, -43.9583309),
              zoom: 19,
              tilt: 0,
              mapTypeId: google.maps.MapTypeId.SATELLITE
            };

            map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

            marker = new google.maps.Marker({
              position: new google.maps.LatLng(-19.8695912, -43.9583309),
              title: 'hum1',
              icon: {
                path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW,
                fillColor: 'gold',
                fillOpacity: 1,
                scale: 4,
                strokeColor: 'gold',
                strokeWeight: 2,
                anchor: new google.maps.Point(0,2.6),
                rotation: 0
              },
              map: map
            });

            flightPath = new google.maps.Polyline({
                path: flightPlanCoordinates,
                geodesic: true,
                strokeColor: 'gold',
                strokeOpacity: 1.0,
                strokeWeight: 1,
                map: map
            });
          }
          /**************************************************************************/



          /* Waypoints functions */
          /**************************************************************************/
          function initWaypointMarker(size){
            var i;
            for (i = 0; i < size; i++) {
                var i_str = (i+1).toString();
                waypoint.push(new MarkerWithLabel({
                    position: new google.maps.LatLng(-19.8695912, -43.9583309),
                    title: i_str,
                    labelContent: i_str,
                    labelInBackground: false,
                    map: map
                }));
            }
          }

          function updateMarkerWaypoint(lat, lon){
            var i;
            if (waypoint.empty) return;
            for (i = 0; i < waypoint.length; i++) {
                newPos = new google.maps.LatLng(lat[i], lon[i]);
                waypoint[i].setPosition(newPos);
            }
          }

          function showWaypoints(on){
            if (on){
                for (i = 0; i < waypoint.length; i++) {
                    waypoint[i].setMap(map);
                }
            }else{
                for (i = 0; i < waypoint.length; i++) {
                    waypoint[i].setMap(null);
                }            }
          }
          /**************************************************************************/



          /* Flight Path functions*/
          /**************************************************************************/
          function updateFlighPath(lat, lng){
            flightPlanCoordinates.push(new google.maps.LatLng(lat, lng));
            flightPath.setPath(flightPlanCoordinates);
          }

          function showFlighPath(on){
            if (on){
                flightPath.setMap(map);
            }else{
                flightPath.setMap(null);
            }
          }
          /**************************************************************************/



          /* Quadrotor Marker */
          /**************************************************************************/
          function updateMarkerPos(lat, lon, name, rot){
            newPosition = new google.maps.LatLng(lat, lon);
            marker.setTitle(name);
            marker.setIcon({
                path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW,
                fillColor: 'gold',
                fillOpacity: 1,
                scale: 4,
                strokeColor: 'gold',
                strokeWeight: 2,
                anchor: new google.maps.Point(0,2.6),
                rotation: rot}),
            marker.setPosition(newPosition);
          }

          function showMarkerPos(on){
            if (on){
                marker.setMap(map);
            }else{
                marker.setMap(null);
            }
          }
          /**************************************************************************/

          function addWaypoint(point){}

          google.maps.event.addDomListener(window, 'load', initialize);
        </script>
      </head>

      <body>
        <div id="map-canvas"></div>
      </body>
    </html>
"""