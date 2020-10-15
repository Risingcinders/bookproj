function validateForm() {
    var x = document.forms["register"]["first_name"].value;
    if (x == "") {
        alert("First Name must be filled out");
        return false;
    }
    var y = document.forms["register"]["last_name"].value;
    if (y == "") {
        alert("Last Name must be filled out");
        return false;
    }
}
