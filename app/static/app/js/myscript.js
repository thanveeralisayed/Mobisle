$('#slider1, #slider2, #slider3, #slider4' ).owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 5,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})






$('.plus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    console.log(id)
    var eml = this.parentNode.children[2]


    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },

        success:function(data){
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = "   " + data.amount
            document.getElementById("total").innerText = data.totalamount
            


        }
    })

})



$('.minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    console.log(id)
    var eml = this.parentNode.children[2]


    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id
        },

        success:function(data){
            eml.innerText = data.quantity
            document.getElementById("amount").innerText ="   " + data.amount
            document.getElementById("total").innerText ="    " + data.totalamount
            


        }
    })

})



localStorage.setItem("btnstatus","enabled");


$('.addcart').click(function(){

    console.log("worked")
    stat = localStorage.btnstatus
    console.log(stat)



    var id = $("#prod_id").attr("value").toString()

    $.ajax({
        
        type:"GET",
        url:"/ador",
        data:{
            prod_id:id
        },

        success:function(data){
            console.log(data)
            console.log("fucntion data works")
            localStorage.btnstatus = data.lsstatus
            
            
        }
        
    })

    
    
    if(stat == "enabled")
    { 
    var id = $(this).attr("pid").toString();

    $.ajax({
        type:"GET",
        url:"/add-to-cart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log(data)
            document.getElementById("cartnum").innerText=data.count
            document.getElementById("addtocartbtn").innerText="Added to cart"
            document.getElementById("addtocartbtn").className="btn btn-secondary shadow px-5 py-2 mt-2"   
            localStorage.btnstatus = "disabled"   
            
        }
    })}




})






$('.rmcart').click(function(){

    
    console.log('working');
    var id = $(this).attr("pid").toString();
    var eml = this

    
    $.ajax({
        type:"GET",
        url:"/remove",
        data:{
            prod_id:id
        },

        success:function(data){
            console.log(data)
            document.getElementById("cartnum").innerText=data.count
            document.getElementById("amount").innerText = "   " + data.amount
            document.getElementById("total").innerText = data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
            
        }


    })
})


$('.setdefad').click(function(){
    console.log("working")
    var id = $(this).attr("pid").toString();
    console.log(id + " in js")

    $.ajax({
        type:"GET",
        url:"/setdefadd",
        data:{
            prod_id:id
        },

        success:function(data){
            console.log(data)
            $(".setdefad").show()
            $("#nm"+id).hide()
            
        }


    })

})


$('.adelbtn').click(function(){
    var id = $(this).attr("pid").toString();
    console.log(id);
    var eml = this

    $.ajax({
        type:"GET",
        url:"/deladd",
        data:{
            prod_id:id
        },

        success:function(data){
            console.log(data)
            eml.parentNode.parentNode.parentNode.remove()            

        }

    })

})



