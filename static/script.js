function uploadFile() {
    let file = document.getElementById("fileInput").files[0];

    let formData = new FormData();
    formData.append("file", file);

    fetch("/upload", { method: "POST", body: formData })
    .then(res => res.json())
    .then(data => alert(data.message));
}


function trainModel() {
    let target = document.getElementById("target").value;

    fetch("/train", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ target: target })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}


function simulate() {
    let f1 = document.getElementById("feature1").value;
    let f2 = document.getElementById("feature2").value;

    fetch("/simulate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            input: {
                feature1: parseFloat(f1),
                feature2: parseFloat(f2)
            }
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerHTML =
            "Prediction: " + data.prediction;
    });
}