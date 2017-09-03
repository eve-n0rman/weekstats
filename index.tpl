<!DOCTYPE html>
<html>
<head>
    <title>Last weeks BRAVE kills/losses</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.16/js/jquery.dataTables.min.js"></script>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.16/css/jquery.dataTables.min.css">
</head>
<body>
<script>
$(document).ready(function() {
    $('#killtable').DataTable({
      "order": [[ 1, "desc" ]]
    });
} );
</script>
<table id="killtable" class="display" cellspacing="0" width="100%">
  <thead><tr>
  <th>Pilot</th>
  <th>Kills</th>
  <th>Losses</th>
  </tr></thead>
  <tbody>
% for char, vals in characters.iteritems():
    <tr>
      <td><a href="{{'https://zkillboard.com/character/' + str(vals['id']) + '/'}}">{{char}}</a></td>
      <td>{{vals['kills']}}</td>
      <td>{{vals['losses']}}</td>
    </tr>
% end
  </tbody>
</table>
</body>
</html>