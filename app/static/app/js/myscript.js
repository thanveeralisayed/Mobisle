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
    // var eml = this.parentNode.children[2]


    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },

        success:function(data){
            // eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total").innerText = data.totalamount
            document.getElementById("quantity").innerText = data.quantity


        }
    })

})



$('.minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    console.log(id)
    // var eml = this.parentNode.children[2]


    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id
        },

        success:function(data){
            // eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total").innerText = data.totalamount
            document.getElementById("quantity").innerText = data.quantity


        }
    })

})


window.onload = function(){
    console.log("succesfully running")
    var btname = $("#addtocartbtn").innerText.toString()
    
    console.log(id)

    $.ajax({
        type:"GET",
        url:"/cup",
        success:function(data){
            console.log(data)
            document.getElementById("cartnum").innerText=data.count
        }


    })

    
    var id = $("#addtocartbtn").attr("pid").toString()

    $.ajax({
        
        type:"GET",
        url:"/ador",
        data:{
            prod_id:id
        },

        success:function(data){
            console.log(data)
            document.getElementById("addtocartbtn").className=data.classname
            document.getElementById("addtocartbtn").innerText=data.btnname
        }
        
    })

}


$("#addtocartbtn").click(function(){
    console.log("worked")
    var id = $(this).attr("pid").toString();
    document.getElementById("addtocartbtn").className="btn btn-secondary shadow px-5 py-2 mt-2"
    document.getElementById("addtocartbtn").innerText="Added to cart"


    

    $.ajax({
        type:"GET",
        url:"/add-to-cart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log(data)
            document.getElementById("cartnum").innerText=data.count
        }
    })




})