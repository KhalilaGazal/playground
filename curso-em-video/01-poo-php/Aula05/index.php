<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title></title>
  </head>
  <body>
    <pre>
      <?php
        require_once 'ContaBancaria.php';
        
        $c1 = new ContaBancaria(23568, "cp", "Jubileu");
        $c2 = new ContaBancaria(54172, "cc", "Creuza");  

        $c1->depositar(300);
        $c2->depositar(500);
        
        $c2->sacar(100);
      ?>
    </pre>
  </body>
</html>
