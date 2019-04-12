<!DOCTYPE html>
<html>
<body>

<?php
  $grille = fopen("grille.txt", "r") or die("Impossible d'ouvrir grille");
  while( !feof($grille)) {
    echo fgets($grille) . "<br>";
  }
  fclose($grille);
?>
</body>
</html>
