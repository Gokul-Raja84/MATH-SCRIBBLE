<?php
include 'config.php';

// Handling API requests in PHP

function getUserById($userId) {
    // Replace this with your actual logic for fetching user by ID
    $user = [
        'id' => $userId,
        'username' => 'john_doe',
        'email' => 'john.doe@example.com',
    ];

    return $user;
}

function updateUser($userId, $updateData) {
    // Replace this with your actual logic for updating user
    // $updateData is an associative array with updated values
    $updatedUser = array_merge(getUserById($userId), $updateData);

    return $updatedUser;
}

// Example API routes

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    if (isset($_GET['user_id'])) {
        $userId = $_GET['user_id'];
        $user = getUserById($userId);
        echo json_encode($user);
    } else {
        // Handle other GET requests if needed
        echo "Invalid API request";
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'PUT') {
    parse_str(file_get_contents("php://input"), $putData);
    $userId = $putData['user_id'];
    $updateData = ['email' => $putData['email']]; // Example update
    $updatedUser = updateUser($userId, $updateData);
    echo json_encode($updatedUser);
}
?>
