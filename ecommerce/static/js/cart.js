//creating event handler for each button
//1)querrying all of the cart items by the classname
var updateButtons = document.getElementsByClassName('update-cart')
// looping through all buttons
for (var i = 0; i < updateButtons.length; i++) {
    updateButtons[i].addEventListener('click', function (){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)
    })
}
