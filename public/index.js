var counterContainer = document.querySelector(".website-counter");
var resetButton = document.querySelector("#reset");
var visitCount = localStorage.getItem("page_view");

var request = new XMLHttpRequest()
request.open('GET', 'https://o1oiql6l851.execute-api.us-east-1.amazonaws.com/dev/add-visit', true)
request.send()

request = new XMLHttpRequest()
request.open('GET', 'https://o1oiql6l851.execute-api.us-east-1.amazonaws.com/dev/get-count', true)
request.onload = function () {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)
  if (request.status >= 200 && request.status < 400) {
   counterContainer.innerHTML = data;
  } else {
    const errorMessage = document.createElement('marquee')
    errorMessage.textContent = 'Failed to query database'
    document.body.appendChild(errorMessage)
  }
}

request.send()
