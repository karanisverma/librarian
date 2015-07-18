/**
 * overlay.js: For animation of overlay popup window.
 *
 * Copyright 2015, Outernet Inc.
 * Some rights reserved.
 *
 * This software is free software licensed under the terms of GPLv3. See
 * COPYING file that comes with the source code, or
 * http://www.gnu.org/licenses/gpl.txt.
 */
(function () {
  var overlay = document.querySelector('div.overlay'),
    s = Snap(overlay.querySelector('svg')),
    path = s.select('path'),
    pathConfig = {
      from : path.attr('d'),
      to : overlay.getAttribute('data-path-to')
    };
  function toggleOverlay() {
    if ($('.overlay').hasClass("open")) {
      $('.overlay').removeClass("open");
      $('.overlay').addClass("close");
      var onEndTransitionFn = function () {
          $('.overlay').removeClass("close");
        };
      path.animate({ 'path' : pathConfig.from }, 400, mina.linear, onEndTransitionFn);
    } else {
      $('.overlay').removeClass("close");
      $('.overlay').addClass("open");
      path.animate({ 'path' : pathConfig.to }, 400, mina.linear);
    }
  }
  $('#trigger-overlay').click(function () {toggleOverlay(); });
  $('.overlay-close').click(function () {toggleOverlay(); });
}(this, this.jQuery));