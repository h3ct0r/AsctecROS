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
          var waypoint = [];
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
          }
          /**************************************************************************/



          /* Waypoints functions */
          /**************************************************************************/
          function pixelToLatlng(xcoor, ycoor) {
              var ne = map.getBounds().getNorthEast();
              var sw = map.getBounds().getSouthWest();
              var projection = map.getProjection();
              var topRight = projection.fromLatLngToPoint(ne);
              var bottomLeft = projection.fromLatLngToPoint(sw);
              var scale = 1 << map.getZoom();
              var newLatlng = projection.fromPointToLatLng(new google.maps.Point(xcoor / scale + bottomLeft.x, ycoor / scale + topRight.y));

              //marker.setPosition(newLatlng);
              return newLatlng;
          };

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

          function updateMarkerWaypoint(px, py){
            var i;
            if (waypoint.empty) return;
            for (i = 0; i < waypoint.length; i++) {
                newPos = pixelToLatlng(px[i], py[i])
                waypoint[i].setPosition(newPos);
            }
          }

          function getWaypointPloted(){
            if (waypoint.empty) return;
            var wpLatLng = [];
            for (var i = 0; i < waypoint.length; i++){
                wpLatLng.push([waypoint[i].getPosition().lat(), waypoint[i].getPosition().lng()] );
            }
            return wpLatLng;
          }

          /**************************************************************************/

          google.maps.event.addDomListener(window, 'load', initialize);
        </script>
      </head>

      <body>
        <div id="map-canvas"></div>
      </body>
    </html>
"""