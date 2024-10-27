// script.js

document.getElementById("submit-btn").addEventListener("click", function() {
    const city = document.getElementById("city-input").value;
    if (city) {
        fetch(`/weather/${city}`)
            .then(response => response.json())
            .then(data => {
                const resultDiv = document.getElementById("result");
                resultDiv.innerHTML = `
                    <h3>Weather in ${data.city}</h3>
                    <p>Temperature: ${data.temperature} °C</p>
                    <p>Condition: ${data.condition}</p>
                    <p>${data.tips}</p>
                `;
            })
            .catch(error => {
                console.error("Error fetching weather:", error);
            });
    } else {
        alert("Please enter a city!");
    }
});
