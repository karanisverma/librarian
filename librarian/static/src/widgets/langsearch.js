
(function (window, $) {
  'use strict';
  $('#langsearch').keyup(function () {
    var valThis = $(this).val().toLowerCase();
    console.log(valThis);
    if (valThis === "") {
      $('.langlist>li').removeClass("langhide").addClass("langshow");
    } else {
      $('.langlist>li').each(function () {
        var text = $(this).text().toLowerCase();
        console.log(text.indexOf(valThis));
        (text.indexOf(valThis) === 25) ? $(this).removeClass("langhide").addClass("langshow") : $(this).addClass("langhide").addClass("langshow");
      });
    }
  });
}(this, this.jQuery));