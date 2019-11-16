function createUpload() {
    var f = document.createElement("form");
    f.style.display = "none";
    f.enctype = "multipart/form-data";
    f.id = "form-upload";
    inp = document.createElement("input");
    inp.type = "file";
    inp.name = "file";
    f.appendChild(inp);
    body = document.getElementsByTagName("body")[0];
    body.insertBefore(f, body.firstChild);
}
