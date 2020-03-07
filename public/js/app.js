$(document).ready(function () {
  var TotalPages = 1
  var Imgs = []
  var CurrentPage = 0
  $("#version").html("v0.14");

  $("#searchbutton").click(function (e) {
    displayModal();
  });

  $("#searchfield").keydown(function (e) {
    if (e.keyCode == 13) {
      displayModal();
    }
  });

  function displayModal() {
    $("#myModal").modal('show');


    $("#status").html("Searching...");
    $("#dialogtitle").html("Search for: " + $("#searchfield").val());
    $("#previous").hide();
    $("#next").hide();
    $.getJSON('/search/' + $("#searchfield").val(), function (data) {
      renderQueryResults(data);
    });
  }

  $("#next").click(function (e) {
    if (CurrentPage+1 < TotalPages) {
      CurrentPage += 1;
      Images();
    }
  });

  $("#previous").click(function (e) {
    if (CurrentPage-1 >= 0) {
      CurrentPage -= 1;
      Images();
    }
  });

  function renderQueryResults(data) {
    if (data.error != undefined) {
      $("#status").html("Error: " + data.error);
    } else {
      CurrentPage = 0;
      Imgs = []
      $("#status").html("" + data.num_results + " result(s)");
      Imgs = data.results
      Images();
      TotalPages = (data.num_results / 4)
      if (data.num_results > 4) {
        $("#next").show();
        $("#previous").show();
      }
    }
  }


  function Images() {
    let Showimg = Imgs.slice(CurrentPage * 4, (CurrentPage + 1) * 4)
    let htmlimg = ""
    let imgPos = 0
    Showimg.forEach(element => {
      htmlimg = document.createElement("img");
      htmlimg.src = element
      htmlimg.width = 220;
      htmlimg.height = 220;
      $('#photo' + imgPos).html(htmlimg)
      imgPos += 1
    });
    if(imgPos < 3){
      for (i=imgPos;i<4;i++)
      $('#photo' + i).html('')
    }
  }
});
