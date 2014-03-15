'use strict';

$(document).ready(function () {

  // Django CSRF middleware need it.
  var csrftoken = $.cookie('csrftoken');
  var csrfSafeMethod = function (method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  };
  $.ajaxSetup({
    crossDomain: false,
    beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type)) {
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
      }
    }
  });

  $('.up').click(function () {
    var $up = $(this);
    $.post($(this).attr('href'), function () {
    }, 'json')
    .done(function (data) {
      if (data.code === 0) {
        $up.hide();
        var $point = $('#id-point-' + data.result.id);
        var point = parseInt($point.text());
        $point.text(point + 1);
      }
    })
    .fail(function () {
    })
    .always(function () {
    });
    return false;
  });

});
