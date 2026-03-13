<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "Student";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$regno = $_POST['regno'];
$name = $_POST['studentname'];
$age = $_POST['age'];
$gender = $_POST['gender'];
$dob = $_POST['dob'];
$programme = $_POST['programme'];
$school = $_POST['school'];
$mode = $_POST['mode'];

$sql = "INSERT INTO StudentRegistration 
(Regno, StudentName, Age, Gender, DateOfBirth, Programme, School, ModeOfStudy)
VALUES ('$regno','$name','$age','$gender','$dob','$programme','$school','$mode')";

if ($conn->query($sql) === TRUE) {
    echo "Student Registered Successfully";
} else {
    echo "Error: " . $conn->error;
}

$conn->close();

?>
