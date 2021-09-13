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


  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#goodtable tbody").html(data.html_good_list);
          $("#modalgood").modal("hide");
        }
        else {
          $("#modalgood .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Подключение функций */

  $(".js-create-good").click(loadForm);
  $("#modal-good").on("submit", ".js-good-create-form", saveForm);

});