var cube = document.getElementById('cube');

var min = 1;
var max = 24;
var step = 50;
var x = 75;

var pig_accumulated = 0;


cube.onclick = function() {
 
  var xRand = getRandom(max, min);
  var yRand = getRandom(max, min);
  var a = document.getElementById("1").innerHTML
  var b = 0;
 
  
  cube.style.webkitTransform = 'rotateX('+xRand+'deg) rotateY('+yRand+'deg)';
  cube.style.transform = 'rotateX('+xRand+'deg) rotateY('+yRand+'deg)';
  var str ="새로운 코드가 입력됩니다."
 
//   document.getElementById("aaa").innerHTML = cube.style.webkitTransform;
//   document.getElementById("bbb").innerHTML = xRand;
  
  if((xRand-90) % 360 == 0 ){
    // document.getElementById("1").innerHTML = "6A";
    b = 6;
  }
  
  else if((xRand-180) % 360 == 0 ){
    if((yRand - 90) % 360 == 0){
    //   document.getElementById("1").innerHTML = "3A";
      b = 3;
    }
    else if((yRand - 180) % 360 == 0){
    //   document.getElementById("1").innerHTML = "1A";
      b = 1;
    }
    else if((yRand - 270) % 360 == 0){
    //   document.getElementById("1").innerHTML = "4A";
      b = 4;
    }
    else if(yRand % 360 == 0){
    //   document.getElementById("1").innerHTML = "2A";
      b = 2;
    }
  }

  else if((xRand-270) % 360 == 0 ){
    // document.getElementById("1").innerHTML = "5A";
    b = 5;
  }
 
  else if(xRand % 360 == 0 ){
    if((yRand - 90) % 360 == 0){
    //   document.getElementById("1").innerHTML = "4A";
      b = 4;
    }
    else if((yRand - 180) % 360 == 0){
    //   document.getElementById("1").innerHTML = "2AA";
      b = 2;
    }
    else if((yRand - 270) % 360 == 0){
    //   document.getElementById("1").innerHTML = "3AAA";
      b = 3;
    }
    else if(yRand % 360 == 0){
    //   document.getElementById("1").innerHTML = "1AAAAA";
      b = 1;
    }
  }

  var number = b;
  document.getElementById("myInput").value = number;



  setTimeout(function(){
    // 6초 후 작동해야할 코드
        document.myForm.submit();
    }, 7000);
 
 
 출처: https://multifrontgarden.tistory.com/157 [우리집앞마당]

  if (pig_accumulated <= 10 ){document.getElementById("pig").style.left =  -c*x + "px";}
  //else if (pig_accumulated > 10 && pig_accumulated < 20)
  //document.getElementById("pig").style.top =  -c*x + "px";
}



function getRandom(max, min) {
  return (Math.floor(Math.random() * (max-min)) + min) * 90;
}
