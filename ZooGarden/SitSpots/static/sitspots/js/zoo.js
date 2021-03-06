$('document').ready(function(){
    attach()
})

function attach(){
    $('.zones').click(function(link){
        link.preventDefault()
        let loc=$(this).attr('loclink')
        console.log(loc);
        let ifbit=($(this).attr('active')=='1')
        console.log(ifbit)
        if(!ifbit){
            $('.zones').attr('active','0')
            $('.zones').removeClass('active')
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
                    // console.log(result)
                    $('#animalsandplants').fadeOut(150)
                    setTimeout(function(){
                        $('#animalsandplants').html(result)
                    }, 150)
                    $('#animalsandplants').fadeIn(150)
                }, this)
            });
        }
    })
}