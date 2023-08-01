document.getElementById("fish-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const species = formData.get("species");
    const length1 = parseFloat(formData.get("length1"));
    const length2 = parseFloat(formData.get("length2"));
    const length3 = parseFloat(formData.get("length3"));
    const height = parseFloat(formData.get("height"));
    const width = parseFloat(formData.get("width"));

    // Encode the species input using one-hot encoding
    const speciesBream = species === "Bream" ? 1 : 0;
    const speciesParkki = species === "Parkki" ? 1 : 0;
    const speciesPerch = species === "Perch" ? 1 : 0;
    const speciesPike = species === "Pike" ? 1 : 0;
    const speciesRoach = species === "Roach" ? 1 : 0;
    const speciesSmelt = species === "Smelt" ? 1 : 0;
    const speciesWhitefish = species === "Whitefish" ? 1 : 0;

    const inputData = {
        "Length1": length1,
        "Length2": length2,
        "Length3": length3,
        "Height": height,
        "Width": width,
        "Species_Bream": speciesBream,
        "Species_Parkki": speciesParkki,
        "Species_Perch": speciesPerch,
        "Species_Pike": speciesPike,
        "Species_Roach": speciesRoach,
        "Species_Smelt": speciesSmelt,
        "Species_Whitefish": speciesWhitefish
    };

    // Send the input data to the Flask API for prediction
    fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(inputData)
    })
    .then(response => response.json())
    .then(data => {
        // Display the prediction result in the "prediction-result" div
        document.getElementById('prediction-result').textContent = "Predicted Weight: " + data.predicted_weight;
    })
    .catch(error => console.error('Error:', error));
});
