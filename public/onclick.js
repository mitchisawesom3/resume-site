function hideShowAdmin() {
  var noselect = document.getElementById("noselection");
  var admin = document.getElementById("admin");
  var senior = document.getElementById("senior");
  if (noselect.style.display != "none") {
    noselect.style.display = "none";
  } else if ( ( admin.style.display === "" ) && ( senior.style.display === "none" ) ) {
    noselect.style.display = "";
  }
  if (admin.style.display === "none") {
    admin.style.display = "";
  } else {
    admin.style.display = "none";
  }
}

function hideShowSenior() {
  var noselect = document.getElementById("noselection");
  var admin = document.getElementById("admin");
  var senior = document.getElementById("senior");
  if (noselect.style.display != "none") {
    noselect.style.display = "none";
  } else if ( ( admin.style.display === "none" ) && ( senior.style.display === "" ) ) {
    noselect.style.display = "";
  }
  if (senior.style.display === "none") {
    senior.style.display = "";
  } else {
    senior.style.display = "none";
  }
}
