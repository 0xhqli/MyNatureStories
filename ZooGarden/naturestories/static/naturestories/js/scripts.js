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
                url: '/naturestories/ajax_zone_stories',
                data: form,
                success: $.proxy(function (result) {
                    // console.log(result)
                    $('#posts').fadeOut(150)
                    setTimeout(function(){
                        $('#posts').html(result)
                    }, 150)
                    $('#posts').fadeIn(150)
                }, this)
            });
        }
    })
    $('#search_button').click(function(but){
        but.preventDefault()
        let search=$("#search").val()
        console.log(search);
        let form={}
        form['csrfmiddlewaretoken']=csrf
        form['search']=search
        console.log(form);
        $('.zones').attr('active','0')
        $('.zones').removeClass('active')
        $.ajax({
            type: "POST",
            url: '/naturestories/ajax_search_stories',
            data: form,
            success: $.proxy(function (result) {
                // console.log(result)
                $('#posts').fadeOut(150)
                setTimeout(function(){
                    $('#posts').html(result)
                }, 150)
                $('#posts').fadeIn(150)
            }, this)
        });
    })
}