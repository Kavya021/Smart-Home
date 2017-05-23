<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "smartfridge";
$info = $_GET['message'];

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}


$sql = "INSERT INTO info VALUES ('$info',NOW())";
if (mysqli_query($conn, $sql)) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
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