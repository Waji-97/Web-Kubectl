function navigateToBackend(backendUrl) {
    window.location.href = backendUrl;
}

// JavaScript for deleting a session
function deleteSession(sessionId) {
    fetch(`/sessions/${sessionId}/delete/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': getCookie('csrftoken') // Function to get CSRF token not shown
        }
    }).then(response => response.json())
    .then(data => {
        if (data.success) {
            // Remove the session element from the page
            const button = document.querySelector(`.delete-button[data-session-id="${sessionId}"]`);
            button.parentNode.remove();
        }
    });
}