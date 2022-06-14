// create product
//save localstorage
//read 
//count
//delete
//update

let image = document.getElementById('img');
let title = document.getElementById('title');
let price = document.getElementById('price');
let total = document.getElementById('total');
let submit = document.getElementById('submit');
console.log(title,price,total,image,submit);
function getTotal(i)
{ 
    while(clicked){

    }

total.innerHTML = result;
}
//create product

let dataPro = [];

submit.onclick = function()
{
     let newpro = 
     {
         image:image.innerHTML.value,
         title:title.innerHTML.value,
         price:price.innerHTML.value,
     }
     dataPro.push(newpro);
     console.log(newpro);
}