document.addEventListener("DOMContentLoaded", function () {
    const getLiveDataButton = document.getElementById("getLiveData");
    if (getLiveDataButton) {
        getLiveDataButton.addEventListener("click", fetchRandomData);
    }
});

function fetchRandomData() {
    fetch('http://127.0.0.1:5000/get_status')
        .then(response => {
            if (!response.ok) throw new Error("Network response was not ok");
            return response.json();
        })
        .then(data => {
            console.log("Received data:", data);
            updateUI(data);
        })
        .catch(error => console.error("Error fetching data:", error));
}

function submitUserData() {
    const temperature = document.getElementById("inputTemp").value;
    const heart_rate = document.getElementById("inputHR").value;
    const activity = document.getElementById("inputActivity").value;

    fetch('http://127.0.0.1:5000/submit_data', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ temperature, heart_rate, activity })
    })
    .then(response => response.json())
    .then(data => updateUI(data))
    .catch(error => console.error("Error submitting data:", error));
}

function updateUI(data) {
    document.getElementById("temperature").innerText = data.temperature;
    document.getElementById("heart_rate").innerText = data.heart_rate;
    document.getElementById("activity").innerText = data.activity;
    const statusElement = document.getElementById("status");
    statusElement.innerText = data.status;
    statusElement.style.color = data.status === "SICK" ? "red" : "green";
}
  
