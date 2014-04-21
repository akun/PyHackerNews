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

  var loginUrl = '/accounts/login/';

  $('.up').click(function () {
    var $up = $(this);
    $.post($(this).attr('href'), function (data) {
      if (data.code === 0) {
        $up.hide();
        var $point = $('#id-point-' + data.result.id);
        var point = parseInt($point.text());
        $point.text(point + 1);
      } else if (data.code === 100) {
        window.location.href = loginUrl;
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
        var $formGroup = $form.find('.form-group');
        var $helpBlock = $form.find('.help-block');
        if (data.code === 0) {
          $formGroup.removeClass('has-error');
          $helpBlock.text('');
          window.location.reload();
        } else if (data.code === 101) {
          $formGroup.addClass('has-error');
          $helpBlock.text(data.result.errors.content);
        } else if (data.code === 100) {
          window.location.href = loginUrl;
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

  $('.remove').click(function () {
    var $remove = $(this);
    $remove.scojs_confirm({
      action: function() {
        $.post($remove.attr('href'), function (data) {
          if (data.code === 0) {
            $.scojs_message('remove success', $.scojs_message.TYPE_OK);
            window.location.reload();
          } else {
            $.scojs_message('remove failed', $.scojs_message.TYPE_ERROR);
          }
        }, 'json')
        .done(function () {
        })
        .fail(function () {
            $.scojs_message('remove failed', $.scojs_message.TYPE_ERROR);
        })
        .always(function () {
        });
        this.close();
      }
    });
    return false;
  });

});
