/**
 * langsearch.js: Search language form a perdefine list
 *
 * Copyright 2015, Outernet Inc.
 * Some rights reserved.
 *
 * This software is free software licensed under the terms of GPLv3. See
 * COPYING file that comes with the source code, or
 * http://www.gnu.org/licenses/gpl.txt.
 */

(function (window, $) {
  'use strict';
  $(document).ready(function () {
    $('#trigger-overlay').css("display", "inline-block");
    $('#nojs').hide();
  });

  $('#langsearch').keyup(function () {
    var valThis = $(this).val().toLowerCase();
    console.log(valThis);
    if (valThis === "") {
      $('.langlist>li').removeClass("langhide").addClass("langshow");
    } else {
      $('.langlist>li').each(function () {
        var text = $(this).text().toLowerCase();
        console.log(text.indexOf(valThis));
        (text.indexOf(valThis) === 21) ? $(this).removeClass("langhide").addClass("langshow") : $(this).addClass("langhide").addClass("langshow");
      });
    }
  });
}(this, this.jQuery));