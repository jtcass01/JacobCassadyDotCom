function show_nasa_cas_certification() {
    var image_field = document.getElementById("nasa-cas-certificate");

    if (image_field.style.display === "none") {
        image_field.style.display = "block";
    } else {
        image_field.style.display = "none";
    }
}