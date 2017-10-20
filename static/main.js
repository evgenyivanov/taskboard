function Update(){

  var url = /task_list/;
  url +=  $("#id_status")[0].value+'/';
  url +=  $("#id_start_month")[0].value+'/';
  url +=  $("#id_start_day")[0].value+'/';
  url +=  $("#id_start_year")[0].value+'/';

  url +=  $("#id_finish_month")[0].value+'/';
  url +=  $("#id_finish_day")[0].value+'/';
  url +=  $("#id_finish_year")[0].value;

$.get(url, function( data ) {
$("#IFRAME")[0].src=url;
});
}


$( document ).ready(function() {

   Update();

   $("#id_status").change(function(){
       Update();
   });

    $("#id_start_day").change(function(){
       Update();
   });

   $("#id_start_month").change(function(){
       Update();
   });

    $("#id_start_year").change(function(){
       Update();
   });

    $("#id_finish_day").change(function(){
       Update();
   });

   $("#id_finish_month").change(function(){
       Update();
   });

   $("#id_finish_year").change(function(){
       Update();
   });

});