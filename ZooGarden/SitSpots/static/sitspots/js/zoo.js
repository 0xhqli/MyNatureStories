$('document').ready(function(){
    attach()
})

function attach(){
    $('.nav-link').click(function(link){
        link.preventDefault()
        let loc=$(this).attr('loclink')
        console.log(loc);
        let ifbit=($(this).attr('active')=='1')
        console.log(ifbit)
        if(!ifbit){
            $('.nav-link').attr('active','0')
            $('.nav-link').removeClass('active')
            $(this).attr('active','1')
            $(this).addClass('active')
            let form={}
            form['csrfmiddlewaretoken']=csrf
            form['zone']=loc
            console.log(form);
            $.ajax({
                type: "POST",
                url: '/sitspots/zoogarden/ajax',
                data: form,
                success: $.proxy(function (result) {
                    console.log(result)
                    // $('#posts').fadeOut(150)
                    // setTimeout(function(){
                    //     $('#posts').html(result)
                    // }, 150)
                    // $('#posts').fadeIn(150)
                }, this)
            });
        }
    })
}