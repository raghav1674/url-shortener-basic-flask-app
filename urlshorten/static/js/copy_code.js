const urlValue = document.getElementById("url").value;
console.log(urlValue);
function getURL() {
  //   urlValue.focus();
  //   urlValue.select(); // select the text
  navigator.clipboard.writeText(urlValue);
  //   document.execCommand("copy");
}
