function comentar()
{
    nombre = document.getElementById("nombrep").value;
    if (nombre == null || nombre.length == 0 || /^\s+$/.test(nombre))
    {
        alert('[ERROR] Ponga su nombrecito');
        document.datos.generos.focus();
    }
    else
    {
        comentario = document.getElementById("comentariop").value;
        if (comentario == null || comentario.length == 0 || /^\s+$/.test(comentario))
        {
            alert('[ERROR] No comentó nada >:c');
            document.datos.generos.focus();
        }
        else
        {   
            nombretherial = document.getElementById("remitente");
            comentariotherial = document.getElementById("coment");

            nombretherial.innerHTML = "poto";
            comentariotherial.innerHTML = "comentario.value";
        }
    }

    
}