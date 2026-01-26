<?php
// 1. Datos JSON simulados (puedes reemplazar con datos reales)
$data = [
    ["label" => "A", "value" => 88],
    ["label" => "B", "value" => 120],
    ["label" => "C", "value" => 150],
    ["label" => "D", "value" => 60],
    ["label" => "E", "value" => 100],
    ["label" => "F", "value" => 130],
    ["label" => "G", "value" => 90],
];

// Convertir a JSON (opcional si quieres mostrarlo)
$jsonData = json_encode($data);

// 2. Configuración del gráfico
$chartWidth = 200;
$chartHeight = 200;
$barWidth = 16; // ancho fijo para cada barra
$spacing = 10;  // espacio entre barras
$maxValue = max(array_column($data, "value")); // valor máximo para escalar

// 3. Generar SVG dinámico
header("Content-Type: image/svg+xml");

echo '<?xml version="1.0" encoding="UTF-8"?>';
echo '<svg width="'.$chartWidth.'mm" height="'.$chartHeight.'mm" viewBox="0 0 '.$chartWidth.' '.$chartHeight.'" xmlns="http://www.w3.org/2000/svg">';

// Fondo y ejes
echo '<rect width="'.$chartWidth.'" height="'.$chartHeight.'" fill="#fff"/>';
echo '<line x1="0" y1="'.($chartHeight-10).'" x2="'.$chartWidth.'" y2="'.($chartHeight-10).'" stroke="#000"/>';

// 4. Dibujar barras
$x = 10; // posición inicial
foreach ($data as $item) {
    $height = ($item["value"] / $maxValue) * ($chartHeight - 20); // escala
    $y = $chartHeight - 10 - $height; // posición vertical
    echo '<rect x="'.$x.'" y="'.$y.'" width="'.$barWidth.'" height="'.$height.'" fill="#4a0396"/>';
    echo '<text x="'.($x+2).'" y="'.($chartHeight-2).'" font-size="8">'.$item["label"].'</text>';
    $x += $barWidth + $spacing;
}

echo '</svg>';
?>

