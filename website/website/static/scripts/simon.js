function show_generated_model() {
    var image_field = document.getElementById("resnet50_generated_model");

    if (image_field.style.display === "none") {
        image_field.style.display = "block";
    } else {
        image_field.style.display = "none";
    }
}
