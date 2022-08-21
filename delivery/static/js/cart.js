const updateBtns=document.querySelectorAll(".update-cart");
for (btn of updateBtns){
    btn.addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action
        console.log('productId: ', productId, "action: ", action)
        console.log("user: ", user)
        if(user==="AnonymousUser"){
            console.log("not logged in")

        }else{
            updateUserOrder(productId, action)
        }

    })
}

function updateUserOrder(productId, action){
    console.log('user us logged in, sending data....')
    var url = '/update_item'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content_Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data: ',data)
    })

}