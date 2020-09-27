
$(document).ready(function(){


  $('#btnSend').click(function(){
  	
  	var errores = '';

		//validando nombre 

		if( $('#names').val() == '' ){
            errores += '<p>Escriba un nombre</p>';
 			 $('#names').css("border-bottom-color", "#F14B4B")
          
        } else{
            $('#names').css("border-bottom-color", "#d1d1d1")
        }
      


       //validando correo
		if( $('#email').val() == '' ){
            errores += '<p>Escriba un correo</p>';
             $('#email').css("border-bottom-color", "#F14B4B")
            
          
        }else{
            $('#email').css("border-bottom-color", "#d1d1d1")
        }



        //validando domicilio
        		if( $('#domicilio').val() == '' ){
            errores += '<p>Escriba un domicilio</p>';
             $('#domicilio').css("border-bottom-color", "#F14B4B")
            
        
        }else{
            $('#domicilio').css("border-bottom-color", "#d1d1d1")
        }

        //enviar domicilio 

           if( errores == '' == false){
            var mensajeModal = '<div class="modal_wrap">'+
                                    '<div class="mensaje_modal">'+
                                        '<h3>Por favor complete lo siguiente:</h3>'+
                                        errores+
                                        '<span id="btnClose">Cerrar</span>'+
                                    '</div>'+
                                '</div>'

            $('body').append(mensajeModal);
        }

//cerrar modal

 $('#btnClose').click(function(){
            $('.modal_wrap').remove();
        });











  	});





});
