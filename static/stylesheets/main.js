// /**
//  * Created by natalie on 13/03/2017.
//  */


// $(".secondpage").hide()

// $(".world").hover(function world() {
//     $(".world").fadeTo("slow", 0.4);
// })
//
// $.when(world()).done(function mainDiv() {
//     $(".world").hide()
// })
$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "http://finance.yahoo.com/d/quotes.csv?s=GOOGL,AAPL,MSFT,FB,FTR,BAC,F,CHK,GE,DNR &f=sl1d1t1c1ohgv&e=.csv",
        dataType: "text",
        success: function(data) {spark(data);}
     });
});

/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "main") {
        x.className += " responsive";
    } else {
        x.className = "main";
    }
}

$(".column").hover(function about(){

})


$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
})


// $('.mouseoverdemo').sparkline();
// $('.mouseoverdemo').bind('sparklineRegionChange', function(ev) {
//     var sparkline = ev.sparklines[0],
//         region = sparkline.getCurrentRegionFields(),
//         value = region.y;
//     $('.mouseoverregion').text("x="+region.x+" y="+region.y);
// }).bind('mouseleave', function() {
//     $('.mouseoverregion').text('');
// });

  $(function spark(data) {


        /* Sparklines can also take their values from the first argument
        passed to the sparkline() function */
        var myvalues = [10,8,5,7,4,4,1];
        $('.dynamicsparkline').sparkline(data);

    });

function formatMonthlyData(data) {
  var monthlyData = [];

  for (var i = 0; i < data.length; i++) {
    monthlyData.push({x: data[i].Month, y: +data[i].Data});
  }

  return monthlyData;
}