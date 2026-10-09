function showDetails() {
    var details = document.getElementById("additionalDetails");
    var button = document.getElementById("detailsButton");

    // Check if the element is currently hidden
    if (details.style.display === "none" || details.style.display === "") {
        details.style.display = "block";
        button.innerHTML = "Hide Details"; 
    } else {
        details.style.display = "none";
        button.innerHTML = "Show Details"; 
    }
}