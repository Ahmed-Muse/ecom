
var updateBtns=document.getElementsByClassName('update-cart')
for (var i=0; i< updateBtns.length; i++ ) {
    updateBtns[i].addEventListener('click', function(){
        var productId=this.dataset.product
        var action=this.dataset.action
        console.log('productId:', productId, 'action:', action)
        console.log('USER:', user)
        if (user ==='AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })
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
