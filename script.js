function toggleSwitch(switchNumber) {
    const statusDiv = document.getElementById('status');
    const url = `/${switchNumber}`; // Relative URL for the route

    fetch(url, {
        method: 'GET'
    })
    .then(response => {
        if (response.ok) {
            statusDiv.textContent = `Status: Switch ${switchNumber} toggled successfully!`;
        } else {
            statusDiv.textContent = `Status: Failed to toggle Switch ${switchNumber}.`;
        }
    })
    .catch(error => {
        statusDiv.textContent = `Status: Error toggling Switch ${switchNumber}.`;
        console.error('Error:', error);
    });
}