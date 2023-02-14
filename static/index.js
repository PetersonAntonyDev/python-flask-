/* import dataset from './dataset.js';
import foodsModel from './food.js'; */

// const formFood = document.querySelector('#formFood');

function loadFoods() {
    const request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var foods = JSON.parse(this.responseText);
            
            for (const item of foods) {
                const itensDiv = document.getElementById('itens');
                const cardHTML = addItem(item);
                itensDiv.insertAdjacentHTML('beforeend', cardHTML);
            }
        }
    }
    request.open("GET", "http://127.0.0.1:5000/projetoCafeteria");
    request.send();
}


function addItem(item) {
    let cardHTML = `
        <div class='food-div col my-3'>
          <div class='card' style='width: 18em;'>
            <img src='${item.image}' class='card-img-top'alt='...'>
              <div class='card-body'>
                <h5 class='card-title'>${item.name}</h5>
                <p class='card-text text-justify'>${item.description}</p>
                <p class='card-text text-justify'>R$${item.price}</p>
                <a href='#' class='btn btn-primary'>Adicionar <i class="fa-solid fa-cart-plus"></i></a>
              </div>
          </div>
        </div>`;
    return cardHTML;
}

document.getElementById("formSubmit").addEventListener("click", function() {
    var fd = new FormData();
    fd.append('name', document.getElementById('name').value);
    fd.append('image', document.getElementById('image').value);
    fd.append('description', document.getElementById('description').value);
    fd.append('price', document.getElementById('price').value);
    
    const request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var item = JSON.parse(this.responseText);
            const itensDiv = document.getElementById('itens');
            const cardHTML = addItem(item);
            itensDiv.insertAdjacentHTML('beforeend', cardHTML);
        }
    }
    request.open("POST", "http://127.0.0.1:5000/projetoCafeteria");
    request.send(fd);
});

loadFoods();