'use strict';

const botonCambio = document.querySelector('.btn');
const body = document.querySelector('#total')


botonCambio.onclick = cambiar_tema;

function cambiar_tema() {
    console.log('Voy a cambiar el tema');
    let textoActual = botonCambio.innerText;

    if (textoActual === 'Dark') {
        botonCambio.innerText = 'Light';
        body.className = 'light-theme';


    } else {
        botonCambio.innerText = 'Dark';
        body.className = 'dark-theme';
    }
}