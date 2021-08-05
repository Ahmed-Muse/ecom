
var updateBtns=document.getElementsByClassName('update-cart')
for (var i=0; i< updateBtns.length; i++ ) {
    updateBtns[i].addEventListener('click', function(){
        var productId=this.dataset.product
        var action=this.dataset.action
        console.log('productId:', productId, 'action:', action)
        console.log('USER:', user)
        if (user ==='AnonymousUser'){
            addCookieItem(productId, action)
        }else{
            updateUserOrder(productId, action)
        }
    })
}


function addCookieItem(productId, action){
    console.log('Not logged in ...')

    if (action=="add"){
        if (cart[productId] == undefined){
            cart[productId] ={"quantity" :1}
        }else{
            cart[productId]['quantity']+=1
        }
    }

    if (action=="remove"){
       
        cart[productId]['quantity']-=1
        if (cart[productId]['quantity'] <=0){
            console.log('Remove item')
            delete cart[productId];
            }
        }
        console.log('Cart:',cart)
        document.cookie='cart='+ JSON.stringify(cart) + ";domain=;path=/"
        location.reload()
  }

function updateUserOrder(productId, action){
    console.log('user logged in sending data')
    var url='/update_item/'//send data to this view template
    fetch(url, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        
        'X-CSRFToken':csrftoken,
    
    },
        
        body:JSON.stringify({'productId': productId, 'action': action})
        

    })
    .then((response) =>{
        return response.json()//this ensures that the page reloads when you click the button to add item... not efficient way.
        //he said that he figured out better way and he may add in the premium section...so check out there
    })

    .then((data) =>{
        console.log('data:',data)
        location.reload()

})

}
