$(document).ready(function() {

var search = function(){
    $("#theResults").show();
    var input = $("#searchfield").val()
    $("#name").text(input+" : Should I invest?")
    $.ajax({
             type:'POST',
             url:'/stock',
             data:{"input":input},
             success: function(response) {
                console.log(response)

             $("#searched").html(response)
             $("#result").text("Overall review:  " +response.result.sentiment.polarity)
             $("#summary").text("What's in the News?  "+response.result.summarize.sentences)
             $("#hashtags").text(response.result.hashtags.hashtags)
             // $("#polarity").text(result.sentiment.polarity);
              },
            error:function(response){
                console.log("error"+response)
            }

});
}

var searchClick = function(input){
    $("#theResults").show();
    var input = input;
    $("#name").text(input+" : Should I invest?")
    $.ajax({
             type:'POST',
             url:'/stock',
             data:{"input":input},
             success: function(response) {
                console.log(response)

             $("#searched").html(response)
             $("#result").text("Overall review:  " +response.result.sentiment.polarity)
             $("#summary").text("What's in the News?  "+response.result.summarize.sentences)
             $("#hashtags").text(response.result.hashtags.hashtags)
             // $("#polarity").text(result.sentiment.polarity);
              },
            error:function(response){
                console.log("error"+response)
            }

});
}

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

$("#image1").on('click', function(){
    var input = 'Intel';
    searchClick(input);
    $(document).ready(function() {
    $("#ourdiv").html("<a class=\"twitter-timeline\" data-width=\"500\" data-height=\"300\" id=\"twittersearcher\" href=\"" + url + "\" >Tweets by TwitterDev</a> <script async src=\"//platform.twitter.com/widgets.js\" charset=\"utf-8\"></script>")
    var position = $("#theResults").position();
    scroll(0,position.top);
     })
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



function formatMonthlyData(data) {
  var monthlyData = [];

  for (var i = 0; i < data.length; i++) {
    monthlyData.push({x: data[i].Month, y: +data[i].Data});
  }

  return monthlyData;
}


$(".search").keypress(function(e) {
if(e.which == 13) {

    search();

    
    var searchstring = $('#searchfield');
    searchstring.focus();
    var xyz = searchstring.val();
    console.log(xyz);
    var url = "https://twitter.com/" + xyz;
    $(document).ready(function() {
        
        $("#ourdiv").html("<a class=\"twitter-timeline\" data-width=\"500\" data-height=\"300\" id=\"twittersearcher\" href=\"" + url + "\" >Tweets by TwitterDev</a> <script async src=\"//platform.twitter.com/widgets.js\" charset=\"utf-8\"></script>")
        var position = $("#theResults").position();
        scroll(0,position.top);
        })

    }
})

// $body = $("#theResults");

$(document).on({
    ajaxStart: function() { $("#theResults").addClass("loading");    },
    ajaxStop: function() { $("#theResults").removeClass("loading"); }    
});

});


