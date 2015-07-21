(function (window, $) {
  'use strict';
  $('.md-trigger').click(function () {
    $('.md-modal').toggleClass('md-show'); 
  });
  $('.md-close').click(function () {
    $('.md-modal').removeClass('md-show');
  });
}(this, this.jQuery));