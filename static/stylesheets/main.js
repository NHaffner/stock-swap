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

  $(function() {
        /** This code runs when everything has been loaded on the page */
        /* Inline sparklines take their values from the contents of the tag */
        $('.inlinesparkline').sparkline();

        /* Sparklines can also take their values from the first argument
        passed to the sparkline() function */
        var myvalues = [10,8,5,7,4,4,1];
        $('.dynamicsparkline').sparkline(myvalues);

        /* The second argument gives options such as chart type */
        $('.dynamicbar').sparkline(myvalues, {type: 'bar', barColor: 'green'} );

        /* Use 'html' instead of an array of values to pass options
        to a sparkline with data in the tag */
        $('.inlinebar').sparkline('html', {type: 'bar', barColor: 'red'} );
    });

