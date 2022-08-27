const updateBtns=document.querySelectorAll(".update-cart");
const updateCtmr=document.querySelectorAll(".update_customer");

console.log(updateCtmr)

for (btn of updateCtmr){
    btn.addEventListener('click', function(){
        var clienteId = this.dataset.cliente;
        var action = this.dataset.action
        console.log('clienteId: ', clienteId, "action: ", action)
        console.log("user: ", user)
        if(user==="AnonymousUser"){
            console.log("not logged in")
            updateCustomerOrder(clienteId, action)

        }else{
            updateCustomerOrder(clienteId, action)
        }

    })
}

function updateCustomerOrder(clienteId, action){
    console.log('user us logged in, sending data....')
    var url = '/update_order_customer'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content_Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'clienteId':clienteId, 'action':action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data: ',data)
        location.reload()

    })
}






for (btn of updateBtns){
    btn.addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action
        console.log('productId: ', productId, "action: ", action)
        console.log("user: ", user)
        if(user==="AnonymousUser"){
            console.log("not logged in")
            updateUserOrder(productId, action)

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
        location.reload()

    })
}