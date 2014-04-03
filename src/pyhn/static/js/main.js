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
    $.post($(this).attr('href'), function (data) {
      if (data.code === 0) {
        $up.hide();
        var $point = $('#id-point-' + data.result.id);
        var point = parseInt($point.text());
        $point.text(point + 1);
      } else if (data.code === 100) {
        window.location.href = '/accounts/login/'
      }
    }, 'json')
    .done(function () {
    })
    .fail(function () {
    })
    .always(function () {
    });
    return false;
  });

  $('.reply').click(function () {
    var commentId = $(this).attr('data-id');
    var action = $(this).attr('data-action');
    var $form = $('#id_reply_form');

    $('#id_comment_' + commentId).append($form);

    $form.find('button').click(function () {
      var content = $form.find('#id_content').val();
      $.post(action, {'content': content}, function (data) {
        var $formGroup = $form.find('.form-group')
        var $helpBlock = $form.find('.help-block')
        if (data.code === 0) {
          $formGroup.removeClass('has-error');
          $helpBlock.text('');
          window.location.reload();
        } else if (data.code === 100) {
          $formGroup.addClass('has-error');
          $helpBlock.text(data.result.errors.content);
        }
      }, 'json')
      .done(function () {
      })
      .fail(function () {
      })
      .always(function () {
      });
      return false;
    });
  });

});
