dnl
dnl homepage - a default portal for your web browser
dnl
dnl Written in 2018 by Calvin Ardi <calvin@isi.edu>
dnl
dnl To the extent possible under law, the author(s) have dedicated all
dnl copyright and related and neighboring rights to this software to the
dnl public domain worldwide. This software is distributed without any
dnl warranty.
dnl
dnl You should have received a copy of the CC0 Public Domain Dedication
dnl along with this software. If not, see
dnl <http://creativecommons.org/publicdomain/zero/1.0/>.
dnl
<html>
<meta charset="UTF-8">
<meta name="referrer" content="no-referrer">
<style>
include(index.css)
</style>

<script>
// attach events to our "open all" links
window.onload = function(){
  elements = document.querySelectorAll("a[nohref]");
  for ( i = 0; i < elements.length; i++ ) {
    if(elements[i].addEventListener) {
      elements[i].addEventListener("click", openAll, false);
      elements[i].addEventListener("auxclick", openAll, false);
    } else {
      // we shouldn't get here, because we're not using legacy browsers
    }
  }
}

function openAll(ev, element, replace = false) {
  ev = ev || window.event;
  if (ev.which == 2) { ev.preventDefault(); }
  if (ev.which != 1 && ev.which != 2) { return false; }

  // get all the sibling elements
  element = element || ev.currentTarget;
  urls = (element.parentNode).getElementsByTagName('a');

  // open all links (except the first)
  for ( i = urls.length - 1; i > 0; i-- ) {
    url = urls[i].getAttribute('href');
    if (i == urls.length - 1 && replace == true) {
      location.assign(url);
    } else {
      window.open(url);
    }
  }
  return false;
}
</script>
<title>the portal</title>
<body>
<div class="outer">
<div class="middle">
<div class="inner">
_content
</div>
</div>
</div>
</body>
</html>
