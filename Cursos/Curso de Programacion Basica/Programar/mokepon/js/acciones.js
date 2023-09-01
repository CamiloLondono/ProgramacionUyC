function seleccionarMascotaJugador(){
    //dentro de la funcion seleccionar Mascota creamos una decision para saber que tipo de mascota selecciono y aparezca el nombre de dicha mascota
    //es mejor guardar los elementos a preguntar en variables para preguntar por ellas o usarlar en algun momento
    let inputHipoGear = document.getElementById("HipoGear")
    let inputPhoenixFlare = document.getElementById("PhoenixFlare")
    let inputTorMetal = document.getElementById("TorMetal")
    let inputGojira = document.getElementById("Gojira")
    let inputHanzSalaman = document.getElementById("HanzSalaman")
    let inputPain = document.getElementById("Pain")
    let spanMascotaJugador = document.getElementById('mascota-jugador')
    //tambien se creo una variable que contenia el id mascota jugador para poder modificar en dicho lugar el nombre a seleccionar
    //se uso la funcion innerHTML que hace que podamos mandarle valores a un campo de texto dinamico para cambiarlo por algun otro valor
    if (inputHipoGear.checked){
        alert('Usted ha seleccionado a HipoGear')
        spanMascotaJugador.innerHTML = 'Hipogear'
    } else if (inputPhoenixFlare.checked){
        alert('Usted ha seleccionado a PhoenixFlare')
        spanMascotaJugador.innerHTML = 'PhoenixFlare'
    } else if (inputTorMetal.checked){
        alert('Usted ha seleccionado a TorMetal')
        spanMascotaJugador.innerHTML = 'TorMetal'
    } else if (inputGojira.checked){
        alert('Usted ha seleccionado a Gojira')
        spanMascotaJugador.innerHTML = 'Gojira'
    } else if (inputHanzSalaman.checked){
        alert('Usted ha seleccionado a HanzSalaman')
        spanMascotaJugador.innerHTML = 'HanzSalaman'
    } else if (inputPain.checked){
        alert('Usted ha seleccionado a Pain')
        spanMascotaJugador.innerHTML = 'Pain'
    } else {
        alert('No seleccionas ningun Mokepon 😔')
    }
    seleccionarMascotaEnemigo()
}
function seleccionarMascotaEnemigo(){
    let ataqueAleatorio = aleatorio(1,6) //usamos la funcion aleatorio que tenemos abajo para seleccionar de manera aleatoria nuestro mokepon
    let spanMascotaEnemigo = document.getElementById('mascota-enemigo')
    if (ataqueAleatorio == 1){
        spanMascotaEnemigo.innerHTML = 'PhoenixFlare'
    } else if (ataqueAleatorio == 2){
        spanMascotaEnemigo.innerHTML = 'HipoGear'
    } else if (ataqueAleatorio == 3){
        spanMascotaEnemigo.innerHTML = 'TorMetal'
    } else if (ataqueAleatorio == 4){
        spanMascotaEnemigo.innerHTML = 'Gojira'
    } else if (ataqueAleatorio == 5){
        spanMascotaEnemigo.innerHTML = 'HanzSalaman'
    } else {
        spanMascotaEnemigo.innerHTML = 'Pain'
    }
}

function seleccionarAtaqueFuego(){
    ataqueJugador = 'FUEGO'
    alert(ataqueJugador)
}
function seleccionarAtaqueAgua(){
    ataqueJugador = 'AGUA'
    alert(ataqueJugador)
}
function seleccionarAtaqueTierra(){
    ataqueJugador = 'TIERRA'
    alert(ataqueJugador)
}
function aleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}
//Boton para seleccionar mascota
let botonMascota = document.getElementById('boton-mascota') //let me sirve para crear variables el javascript
botonMascota.addEventListener('click', seleccionarMascotaJugador)
//Botones para seleccionar los ataques
let ataqueJugador //Variable global para usarla en el dom y cambiarla dentro de las funciones
let botonAtaqueFuego = document.getElementById('boton-Fuego') //con el getElementById selecciono un boton por 
botonAtaqueFuego.addEventListener('click', seleccionarAtaqueFuego) //parte de su id
let botonAtaqueAgua = document.getElementById('boton-Agua')
botonAtaqueAgua.addEventListener('click', seleccionarAtaqueAgua)
let botonAtaqueTierra = document.getElementById('boton-Tierra')
botonAtaqueTierra.addEventListener('click', seleccionarAtaqueTierra)
