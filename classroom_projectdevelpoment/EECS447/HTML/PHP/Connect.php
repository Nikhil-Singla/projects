<?php

$server = 'mysql.eecs.ku.edu';
$database = "n210s707";
$name = "n210s707";
$pass = "nikhil12345";

$server = "localhost";
$database = "n210s707";
$name = "root";
$pass = "";


$mysqli = new mysqli($server, $name, $pass, $database);
                     
if ($mysqli->connect_errno) 
{
    die("Connection error: " . $mysqli->connect_error);
}

return $mysqli;

?>