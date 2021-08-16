$(document).ready(function () {

  $("#datatable").DataTable();

  
  $("#datatable2").DataTable();
  $("#datatable3").DataTable();

  $("#datatable-buttons")
    .DataTable({
      lengthChange: !1,
      buttons: ["pdf",],
    })
    .buttons()
    .container()
    .appendTo("#datatable-buttons_wrapper .col-md-6:eq(0)");

});
