function getCookie(c_name) {
  var i,x,y,ARRcookies=document.cookie.split(";");
    for (i=0;i<ARRcookies.length;i++){
      x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
      y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
      x=x.replace(/^\s+|\s+$/g,"");
      if (x==c_name) {
        return unescape(y);
      }
  }
}

function setCookie(c_name,value,exdays) {
  var exdate=new Date();
  exdate.setDate(exdate.getDate() + exdays);
  var c_value=escape(value) + ((exdays==null) ? "" : ";expires="+exdate.toUTCString());
  document.cookie=c_name + "=" + c_value;
}

function checkForm(form) {
  // var idx = Math.floor(Math.random() * lenOfPlayers)

  // var search = form.children[]


  

  var search1 = form.children[1].value;
  console.log(search1);
  var search2 = form.children[3].value;

  if ((search1==null && search2==null)) {
    return false;
  }

  if (search1.toUpperCase()=="ELON MUSK") {
    alert("He's not here!");
  }

  return true;
}
