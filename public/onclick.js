function hideShowAdmin() {
  var noselecta = document.getElementById("noselecta");
  var text = noselecta.textContent;
  var admin = document.getElementById("admin");
  var senior = document.getElementById("senior");
  if ( noselecta.textContent.includes("Show") ) {
    noselecta.textContent = text.replace("Show More","Hide");
    admin.style.display = "";
  } else if ( noselecta.textContent.includes("Hide") ) {
    noselecta.textContent = text.replace("Hide","Show More");
    admin.style.display = "none";
  }
}

function hideShowSenior() {
  const noselectb = document.getElementById("noselectb");
  var admin = document.getElementById("admin");
  var senior = document.getElementById("senior");
  if ( noselectb.innerText.includes("Show") ) {
    const text = noselectb.innerText;
    noselectb.innerText = text.replace("Show More","Hide");
    senior.style.display = "";
  } else if ( noselectb.textContent.includes("Hide") ) {
    const text = noselectb.textContent;
    noselectb.textContent = text.replace("Hide","Show More");
    senior.style.display = "none";
  }
}
