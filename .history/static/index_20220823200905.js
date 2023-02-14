import dataset from './dataset.js';
import foodsModel from './food.js';

const formFood = document.querySelector('#formFood');

function loadFoods() {

    if (localStorage.getItem('foods-app:loaded') !== 'ok') {

        localStorage.setItem('foods-app:loaded', 'ok');
    }
    else {
        foodsModel.load(dataset);
    };

    let foods = foodsModel.readAll();

    for (const item of foods) {

        const itensDiv = document.getElementById('itens');
        const cardHTML = addItem(item);
        itensDiv.insertAdjacentHTML('beforeend', cardHTML);
    }

}


function addItem(item) {
    let cardHTML = `
        <div class='food-div col my-3'>
          <div class='card' style='width: 18em;'>
            <img src='images/${item.image}' class='card-img-top'alt='...'>
              <div class='card-body'>
                <h5 class='card-title'>${item.name}</h5>
                <p class='card-text text-justify'>${item.description}</p>
                <p class='card-text text-justify'>R$${item.preco}</p>
                <a href='#' class='btn btn-primary'>Adicionar <i class="fa-solid fa-cart-plus"></i></a>
              </div>
          </div>
        </div>`;
    return cardHTML;
}



function loadFormValue(foodName, foodImage, foodDescription, foodPreco) {
    //const formLabel = document.querySelector('#formFoodLabel');
    const formNameInput = document.querySelector('#name');
    const formImageInput = document.querySelector('#image');
    const formPrecoInput = document.querySelector('#preco');
    const formDescriptionInput = document.querySelector('#description');

    //formLabel.innerHTML = title;
    formNameInput.value = foodName;
    formImageInput.value = foodImage;
    formPrecoInput.value = foodPreco;
    formDescriptionInput.value = foodDescription;

}

const foodForm = document.getElementById('formFood');
foodForm.onsubmit = (e) => {
    console.log("carai");
}

//const loadFormCreteFood = document.querySelector("#foodModal")
//loadFormCreteFood.addEventListener('click', function () {
   // console.log(foodForm);
    /*loadFormValue('Adicionar Comida', '', '', '', '');
    // Previnir que o modal fique abrindo em loop.
    foodForm.onsubmit = (e) => {
        e.preventDefault();

        // Montar o objeto food baseado nos dados do formulário.
        let food = Object.fromEntries(new FormData(formFood));

        // Adicionar o item (food) no LocalStorage.
        const newFood = foodsModel.create(food);
        console.log(newFood);
        const itensDiv = document.getElementById('itens');
        const cardHTML = addItem(newFood);
        itensDiv.insertAdjacentHTML('beforeend', cardHTML);

        // Fechar o foodModal
        var myModalEl = document.getElementById('foodModal');
        var foodModal = bootstrap.Modal.getInstance(myModalEl);
        foodModal.toggle();

    };*/
    
//})


//window.loadFormCreteFood = loadFormCreteFood;

loadFoods();