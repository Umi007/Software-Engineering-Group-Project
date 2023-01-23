function tabs(evt, slide) {
  var i, x, tablinks;
  /*Adds display none to all tabs*/
  x = document.getElementsByClassName("tab");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  /*Adds the class tab-selected to relevant tab*/
  for (i = 0; i < x.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" tab-selected", "");
  }
  /*Displays tab*/
  document.getElementById(selectedTab).style.display = "block";
  evt.currentTarget.className += " tab-selected";
}