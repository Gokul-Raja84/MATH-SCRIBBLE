<?php
// General utility functions in PHP

function capitalize($str) {
    return ucfirst($str);
}

function formatDate($date) {
    // Replace this with your actual logic for formatting date
    return date('Y-m-d', strtotime($date));
}
?>
