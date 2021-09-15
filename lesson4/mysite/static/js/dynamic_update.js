$(function () {

  /* Код функций */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modalgood").modal("show");
      },
      success: function (data) {
        $("#modalgood .modal-content").html(data.html_form);
      }
    });
  };


  var saveForm = function (evt) {
    // evt.preventDefault()
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $(".modal-content").modal("hide");
          $("#goodtable tbody").html(data.html_good_list);
          console.log('test1')
        }
        else {
          $("#modalgood .modal-content").html(data.html_form);
          console.log('test2')
        }
      }
    });
    form.trigger('reset');
    return false;
  };

  /* Подключение функций */

  $(".js-create-good").click(loadForm);
  $("#modalgood").on("submit", ".js-good-create-form", saveForm);

});