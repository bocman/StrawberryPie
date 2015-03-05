$(document).ready(function () {

    //call the blink function on the element you want to blink
    blink(".myDiv", 100, 1200); //blink a div with the ID of myDiv
    blink("input[type='submit']", 3, 1000); //blink a submit button
    //blink("ol > li:first", -1, 100); //blink the first element in an ordered list (infinite times)
    blink(".myClass", 25, 5000); //blink anything that has a myClass on it
});

/**
 * Purpose: blink a page element
 * Preconditions: the element you want to apply the blink to, the number of times to blink the element (or -1 for infinite times), the speed of the blink
 **/
function blink(elem, times, speed) {
    if (times > 0 || times < 0) {
        if ($(elem).hasClass("blink")) 
            $(elem).removeClass("blink");
        else
            $(elem).addClass("blink");
    }

    clearTimeout(function () {
        blink(elem, times, speed);
    });

    if (times > 0 || times < 0) {
        setTimeout(function () {
            blink(elem, times, speed);
        }, speed);
        times -= .5;
    }
}