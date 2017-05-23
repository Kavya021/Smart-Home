<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "smartfridge";


// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}



$sql = "SELECT * FROM info";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {
        echo "message: " . $row["item"]. " - Time: " . $row["timeOfEmpty"]. "<br>";
        echo '<img src="'.$row["item"].'.jpg">';
    }
} else {
    echo "0 results";
}
mysqli_close($conn);

?>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Information</title>
</head>
<body>
	<h1></h1>

</body>
</html>