/*
    Canvas
*/

//T// find canvas document.querySelector('canvas')
var canvasModif = document.querySelector('canvas');

//T// choose 2D or 3D context with getContext()
var cnvDraw = canvasModif.getContext('2d');

var drawFnc = function()
{
    var pos,vel;
    pos =
    {
        x:10,y:10
    };
    vel =
    {
        x:1.5,y:1.5
    };

    var loopFnc = function()
    {
//T// clear the canvas with clearRect()
        cnvDraw.clearRect(0,0,canvasModif.width,canvasModif.height);
        pos.x += vel.x;
        pos.y += vel.y;
        if(pos.x < 5 || pos.x > (canvasModif.width - 5)) {vel.x *= -1;}
        if(pos.y < 5 || pos.y > (canvasModif.height - 5)) {vel.y *= -1;}

//T// draw square with fillRect()
        cnvDraw.fillRect(pos.x - 5, pos.y - 5, 10, 10);
    };
//T// redraw at 40 FPS with setInterval()
    setInterval(loopFnc,1000/40);
};

window.addEventListener('load',drawFnc);