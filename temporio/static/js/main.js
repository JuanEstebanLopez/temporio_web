
$( document ).ready(function(){

  /*Set hora y fecha*/
  $('.datepicker').datepicker({
    format: 'dd/mm/yyyy',
    startDate: '-3d'
  });

  $('#hora').timepicker({

    minuteStep:5

  });

  $('#horaEdit').timepicker({

    minuteStep:5

  });




  /*Crear Tarea*/

  $('#crear-tarea').click(function(){
    titulo =$('#titulo').val();
    var comprobar = titulo.toLowerCase();
    var arreglo = comprobar.split(' ');
    console.log(arreglo);
    var compendio = ['parcial', 'taller', 'tarea','lectura', 'trabajo', 'exposicion', 'exposición', 'grupal'];
    var tipo = 0;

    //Permite comparar que datos tienen en comun el titulo y el compendio
    //retorna el index del compendio contando desde 0

    function comparar(a, b) {
      var matches;

      for ( var i = 0; i < a.length; i++ ) {
        for ( var e = 0; e < b.length; e++ ) {
          if ( a[i] === b[e] ) matches=a[i];
          var resultado = compendio.indexOf(matches);
        }
      }
      return resultado;
    }

    var tipo = comparar(arreglo, compendio);

    descripcion =$('#descripcion').val();
    fecha=$('#fecha').val();
    hora =$('#hora').val();
    grupo=$('#grupos').val();

    registroAjax(titulo, descripcion, fecha, hora, grupo, tipo);
    console.log("estos son los datos enviados:" + '\n' + titulo + '\n' +  descripcion + '\n'+  fecha + '\n'+  hora + '\n' + grupo + '\n' + tipo);

  });

  /*Registra la tarea nueva y la crea*/
  function registroAjax(tituloP, descripcionP, fechaP, horaP, grupoP, tipoP){
    var datos = {
      "titulo" : tituloP,
      "descripcion" : descripcionP,
      "fecha" : fechaP,
      "hora" : horaP,
      "grupo" : grupoP,
      "tipo": tipoP
    }


    if(tipoP<0){
      tipoP=1;
    }
    var hora=horaP.split(":");
    var h=parseInt(hora[0]);
    var m=hora[1].split(" ");
    if(m[1]=="PM"){
      h+=12;
      if(h==24){
        h=0;
      }
    }
    str_hora=h+"/"+m[0];
    var str_url='/crear_alarma/'+fechaP+"/"+str_hora+"/"+tipoP+"/"+tituloP+"/"+descripcionP+"/";
    if(grupoP!="none"){
      str_url+=grupoP+"/";
    }

    console.log("esto fue lo que obtuvo" + JSON.stringify(datos));
    // $('.muro').append("<div class='publicacion'>"+"<span class='glyphicon glyphicon-remove-circle editar' id='borrar' data-title='Borrar'>"+"</span>"+"<span class='glyphicon glyphicon-edit editar' id='editar' data-title='Editar'>"+"</span>"+"<span class='glyphicon glyphicon-ok-circle editar' id='completar' data-title='Marcar como Completo'>"+"</span>"+"<h3>"+tituloP+"</h3>"+"<div class='datos'>"+"<p class='fecha'>"+"<span> Fecha:"+"</span>"+fechaP+"</p>"+"<p class='hora'>"+"<span> Hora:"+"</span>"+horaP+"</p>"+"<p class='grupo'>"+"<span> Grupo:"+"</span>"+grupoP+"</p>"+"<p class='descripcion'>"+"<span> Descripcion:"+"</span>"+descripcionP+"</p>"+"</div>"+"</div>");
    $.ajax({
    data: datos,
    url: str_url,
    type: 'get',
    success: function(response){
        $('.muro').append("<div class='publicacion'>"+"<span class='glyphicon glyphicon-remove-circle editar' id='borrar' data-title='Borrar'>"+"</span>"+"<span class='glyphicon glyphicon-edit editar' id='editar' data-title='Editar'>"+"</span>"+"<span class='glyphicon glyphicon-ok-circle editar' id='completar' data-title='Marcar como Completo'>"+"</span>"+"<h3>"+tituloP+"</h3>"+"<div class='datos'>"+"<p class='fecha'>"+"<span> Fecha:"+"</span>"+fechaP+"</p>"+"<p class='hora'>"+"<span> Hora:"+"</span>"+horaP+"</p>"+"<p class='grupo'>"+"<span> Grupo:"+"</span>"+grupoP+"</p>"+"<p class='descripcion'>"+"<span> Descripcion:"+"</span>"+descripcionP+"</p>"+"</div>"+"</div>");
        console.log(response);
        alert("Se ha cread la nueva notificación exitosamente.");
        $('#titulo').val("");
        $('#descripcion').val("");
        // $('.muro').append(response);
    // alert(response);
  },
  error: function(){
  console.log("Error")
  alert("No se pudo crear la notificación.");
}
})
}


$(".publicacion").on('mouseenter',function(){

  //Borrar Publicacion
  $(this).find("#borrar").click(function(){

    console.log("presionado papu");
    $(this).parent(".publicacion").remove();
    //Esta funcion reocrre el arreglo y verifica si hay algun elemento con el mismo nombre
    // si existe lo elimina.
    /*  for (var i=jdatos.length-1; i>=0; i--) {
    if (jdatos[i].titulo === titulo) {
    jdatos.splice(i, 1);

    console.log("elminado con exito");
  }
}*/


});

//Editar Publicacion
$(this).find("#editar").click(function(){


  $("#editable").css("display", "block");

  console.log("presionado papu");
  //Revela la pantalla de edicion
  document.getElementById("myNav").style.width = "100%";
  /*Recupera los datos de la publicacion*/
  var nombre = $(this).parent(".publicacion").find("h3").text();
  var fecha= $(this).parent(".publicacion").find(".datos").find(".fecha").text();
  var fechaE = fecha.split(':');
  var hora= $(this).parent(".publicacion").find(".datos").find(".hora").text();
  var horaE = hora.split(':');
  var horaT = horaE[1]+":"+horaE[2];
  var grupo= $(this).parent(".publicacion").find(".datos").find(".grupo").text();
  var  grupoE = grupo.split(':');
  var descri= $(this).parent(".publicacion").find(".datos").find(".descripcion").text();
  var  descriE = descri.split(':');
  console.log("estos son los datos" + '\n' + nombre + '\n' + fechaE[1] + '\n' + horaT + '\n' + grupoE[1] + '\n' +descriE[1]);


  $("#tituloEdit").val(nombre);
  $("#descripcionEdit").val(descriE[1]);
  $("#fechaEdit").val(fechaE[1]);
  $("#horaEdit").val(horaT);

  /* $(this).parent(".publicacion").find("h3").attr('contenteditable', 'true');
  $(this).parent(".publicacion").find(".datos").find("p").attr('contenteditable' , 'true');*/
  //Esta funcion reocrre el arreglo y verifica si hay algun elemento con el mismo nombre


  $("#guardar-cambios").click(function(){
    document.getElementById("myNav").style.width = "0%";
    $("#editable").css("display", "none");

  });

});


//Marcar Progreso
$(this).find("#completar").click(function(){

  document.getElementById("myNav").style.width = "100%";
  $("#aprobar").css("display", "block");



  console.log("presionado papu");
  //Revela la pantalla de edicion
  document.getElementById("myNav").style.width = "100%";
  /*Recupera los datos de la publicacion*/
  var nombre = $(this).parent(".publicacion").find("h3").text();
  var fecha= $(this).parent(".publicacion").find(".datos").find(".fecha").text();
  var fechaE = fecha.split(':');
  var hora= $(this).parent(".publicacion").find(".datos").find(".hora").text();
  var horaE = hora.split(':');
  var horaT = horaE[1]+":"+horaE[2];
  var grupo= $(this).parent(".publicacion").find(".datos").find(".grupo").text();
  var  grupoE = grupo.split(':');
  var descri= $(this).parent(".publicacion").find(".datos").find(".descripcion").text();
  var  descriE = descri.split(':');
  console.log("estos son los datos" + '\n' + nombre + '\n' + fechaE[1] + '\n' + horaT + '\n' + grupoE[1] + '\n' +descriE[1]);


  $("#tituloEdit").val(nombre);
  $("#descripcionEdit").val(descriE[1]);
  $("#fechaEdit").val(fechaE[1]);
  $("#horaEdit").val(horaT);

  /* $(this).parent(".publicacion").find("h3").attr('contenteditable', 'true');
  $(this).parent(".publicacion").find(".datos").find("p").attr('contenteditable' , 'true');*/
  //Esta funcion reocrre el arreglo y verifica si hay algun elemento con el mismo nombre


  $("#guardar-cambios").click(function(){
    document.getElementById("myNav").style.width = "0%";
    $("#editable").css("display", "none");

  });

});

});

/*Efecto del menu de aprobados*/

$("ul > li").on("click", function(){

  $("#todos").css("background-color", "transparent");
  $("ul li").css("background-color", "transparent");
  $("ul li").css("color", "#000");
  $(this).css("background-color", "#5AAABF");
  $(this).css("color", "#fff");
  var nombre = $(this).html();
  console.log("este es el nombre del elemento" + nombre);

  switch(nombre){
    case "Todos":
    console.log("llego aqui");
    $(".grupo1").css("display", "block");
    $(".grupo2").css("display", "block");
    $(".grupo3").css("display", "block");

    break;


    case "Grupo 1":
    console.log("llego aqui2");
    $(".grupo1").css("display", "block");
    $(".grupo2").css("display", "none");
    $(".grupo3").css("display", "none");


    break;

    case "Grupo 2":
    console.log("llego aqui3");
    $(".grupo2").css("display", "block");
    $(".grupo1").css("display", "none");
    $(".grupo3").css("display", "none");

    break;

    case "Grupo 3":
    console.log("llego aqui4");
    $(".grupo3").css("display", "block");
    $(".grupo1").css("display", "none");
    $(".grupo2").css("display", "none");

    break;
  }

});



var aprobados = [];
var noAprobados = [];


//Aprueba Alumno

$( ".ok-criolloA" ).each(function(index) {
  $(this).on("click", function(){

    $(this).parent(".apru").parent(".alumno").find("h4").css("color", "#18F04B");

    var nombreAlumno  = $(this).parent(".apru").parent(".alumno").find("h4").text();

    var index = aprobados.indexOf(nombreAlumno+":"+"no-aprobado");

    if (index > -1) {
      console.log("parece que si esta asi que vamos a quitarlo");
      aprobados.splice(index, 1);
      var aprueba = "aprobado";
      aprobados.push(nombreAlumno+":"+aprueba);
    }else{
      var aprueba = "aprobado";
      aprobados.push(nombreAlumno+":"+aprueba);
    }

    console.log(JSON.stringify(aprobados));


  });
});

//Desaprueba Alumno

$( ".ok-criolloN" ).each(function(index) {
  $(this).on("click", function(){
    // For the boolean value
    $(this).parent(".apru").parent(".alumno").find("h4").css("color", "#E52929");
    var nombreAlumno  = $(this).parent(".apru").parent(".alumno").find("h4").text();


    var index = aprobados.indexOf(nombreAlumno+":"+"aprobado");

    if (index > -1) {
      console.log("parece que si esta asi que vamos a quitarlo 2 ");
      aprobados.splice(index, 1);
      var aprueba = "no-aprobado";
      aprobados.push(nombreAlumno+":"+aprueba);
    }else{
      var aprueba = "no-aprobado";
      aprobados.push(nombreAlumno+":"+aprueba);
    }

    console.log(JSON.stringify(aprobados));
  });
});


//enviar Formulario

$("#ok").click(function(){

  document.getElementById("myNav").style.width = "0%";


  enviarEvaluacion(aprobados);


});


//Envia la evaluacion de los datos obtenidos
function enviarEvaluacion(aprobados){

  var datos = {
    aprobados
  }

  console.log(JSON.stringify(datos));

  console.log("datos enviados");
}


});




function closeNav() {
  document.getElementById("myNav").style.width = "0%";
  $("#aprobar").css("display", "none");
  $("#editable").css("display", "none");

}
