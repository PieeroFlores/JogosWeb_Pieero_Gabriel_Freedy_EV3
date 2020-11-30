function validacion()
        {
            genero = document.getElementsByName("gender");
            var generoseleccionado = false;
            for(var i=0; i<genero.length; i++){
                if (genero[i].checked) {
                    generoseleccionado = true;
                    break;
                }
            }
            if (!generoseleccionado){
                alert('[ERROR] Devuélvase y seleccione un género');
                return false;
            }

            edad = document.getElementById("edad").value;
            if (isNaN(edad) || edad.length == 0) {
                alert('[ERROR] Ingrese una edad válida');
                document.datos.edad.focus();
                return false;
            }

            pais = document.getElementById("pais").selectedIndex;
            if (pais == null || indice == 0) {
                alert('[ERROR] Seleccione un país >:c');
                document.datos.pais.focus();
                return false;
            }

            generos = document.getElementById("generos").value;
            if (generos == null || generos.length == 0 || /^\s+$/.test(generos)) {
                alert('[ERROR] Ingrese al menos un género de videojuego');
                document.datos.generos.focus();
                return false;
            }

            descripcion = document.getElementById("descripcion").value;
            if (descripcion == null || descripcion.length == 0 || /^\s+$/.test(descripcion)) {
                alert('[ERROR] Si quieres puedes poner una carita :) y con eso basta');
                document.datos.descripcion.focus();
                return false;
            }
        }