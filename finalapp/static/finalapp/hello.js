// var cube = document.getElementById('cube');

// var min = 1;
// var max = 24;
// var step = 50;
// var x = 75;
// var pig;
// var c = 0;

// var pig_accumulated = 0;

/*
cube.onclick = function() {
 
  var xRand = getRandom(max, min);
  var yRand = getRandom(max, min);
  var a = document.getElementById("1").innerHTML
  var b = 0;
 
  
  cube.style.webkitTransform = 'rotateX('+xRand+'deg) rotateY('+yRand+'deg)';
  cube.style.transform = 'rotateX('+xRand+'deg) rotateY('+yRand+'deg)';
  var str ="새로운 코드가 입력됩니다."
 
  document.getElementById("aaa").innerHTML = cube.style.webkitTransform;
  document.getElementById("bbb").innerHTML = xRand;
  
  if((xRand-90) % 360 == 0 ){
    document.getElementById("1").innerHTML = "6A";
    b = 6;
  }
  
  else if((xRand-180) % 360 == 0 ){
    if((yRand - 90) % 360 == 0){
      document.getElementById("1").innerHTML = "3A";
      b = 3;
    }
    else if((yRand - 180) % 360 == 0){
      document.getElementById("1").innerHTML = "1A";
      b = 1;
    }
    else if((yRand - 270) % 360 == 0){
      document.getElementById("1").innerHTML = "4A";
      b = 4;
    }
    else if(yRand % 360 == 0){
      document.getElementById("1").innerHTML = "2A";
      b = 2;
    }
  }

  else if((xRand-270) % 360 == 0 ){
    document.getElementById("1").innerHTML = "5A";
    b = 5;
  }
 
  else if(xRand % 360 == 0 ){
    if((yRand - 90) % 360 == 0){
      document.getElementById("1").innerHTML = "4A";
      b = 4;
    }
    else if((yRand - 180) % 360 == 0){
      document.getElementById("1").innerHTML = "2AA";
      b = 2;
    }
    else if((yRand - 270) % 360 == 0){
      document.getElementById("1").innerHTML = "3AAA";
      b = 3;
    }
    else if(yRand % 360 == 0){
      document.getElementById("1").innerHTML = "1AAAAA";
      b = 1;
    }
  }
  c = c + b;

  var number = a;
  document.getElementById("myInput").value = number;


  pig_accumulated = pig_accumulated + c;
  if (pig_accumulated <= 10 ){document.getElementById("pig").style.left =  -c*x + "px";}
  //else if (pig_accumulated > 10 && pig_accumulated < 20)
  //document.getElementById("pig").style.top =  -c*x + "px";
}
*/

/*
function getRandom(max, min) {
  return (Math.floor(Math.random() * (max-min)) + min) * 90;
}
*/