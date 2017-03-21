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
// $(".column").click(function () {
//     $.ajax({
//         type: 'GET',
//         url: '/search',
//         dataType: "json",
//         $("")
//     how to get by id
//
//     })
//
// })


$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.industry%20where%20id%3D%22112%22&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys",
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

//
$("#image1").hover(function(){
    $('.content1').show();
},function(){
    $('.content1').hide();
});

$("#image2").hover(function(){
    $('.content2').show();
},function(){
    $('.content2').hide();
});

$("#image3").hover(function(){
    $('.content3').show();
},function(){
    $('.content3').hide();
});

$("#image4").hover(function(){
    $('.content4').show();
},function(){
    $('.content4').hide();
});

$("#image5").hover(function(){
    $('.content5').show();
},function(){
    $('.content5').hide();
});

$("#image6").hover(function(){
    $('.content6').show();
},function(){
    $('.content6').hide();
});

$("#image7").hover(function(){
    $('.content7').show();
},function(){
    $('.content7').hide();
});

$("#image8").hover(function(){
    $('.content8').show();
},function(){
    $('.content8').hide();
});

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


        $(".search").keypress(function(e) {
        if(e.which == 13) {
            console.log("aaaaaa");
            var searchstring = $('#searchfield');
            searchstring.focus();
            var xyz = searchstring.val();
            console.log(xyz);
            var url = "https://twitter.com/" + xyz;
            $(document).ready(function() {
                console.log("loopdeloop")
                $("#ourdiv").html("<a class=\"twitter-timeline\" data-width=\"500\" data-height=\"300\" id=\"twittersearcher\" href=\"" + url + "\" >Tweets by TwitterDev</a> <script async src=\"//platform.twitter.com/widgets.js\" charset=\"utf-8\"></script>")
                var n = $(document).height();
                $('html, body').animate({scrollTop: n}, 500);
                })
            }
        })


$(document).ready(function() {

	// $.get('/stock', function(result){
	// 	console.log(result);
	// 	var cool = result.language.confidence;
	// 	$("#searched").text(result.language.confidence);
	// 	//$("#hashtags").text(result.hastags.hashtags.0);
	// 	$("#polarity").text(result.sentiment.polarity);

	// },"json");

// var test = result;
// //document.write(result)
var search = function(){
	var input = $("#userInput").val()
	$.ajax({
             type:'POST',
             url:'/stock',
      		 data:{"input":input},
             success: function(response) {
             	console.log(response)

             $("#searched").html(response)
             $("#name").text(response.result.input1)
			 $("#result").text(response.result.sentiment.polarity)
			 $("#summary").text(response.result.summarize)
			 // $("#polarity").text(result.sentiment.polarity);
			  },
            error:function(response){
            	console.log("error"+response)
            }

});
}
$("#btn").on("click",search)

function userLink(){

var userInput = $("#stockInput").value;
console.log(userInput);
return userInput;

};

// $.post( "/search", {


//   //  javascript_data: userInput

// });

});












