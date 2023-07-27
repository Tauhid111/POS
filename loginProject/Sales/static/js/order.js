var updateOrderBtns = document.getElementsByClassName('update-order')
for (i = 0; i<updateOrderBtns.length; i++){
    updateOrderBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)
    })
}