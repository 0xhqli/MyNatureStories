$('document').ready(function(){
    attach()
    reattach()
})

function attach(){
    $('#new_comment').submit(function(form){
        form.preventDefault()
        let data=$(this).serialize()
        console.log(data)
        $.ajax({
            type: "POST",
            url: '/naturestories/new_comment_ajax',
            data: data,
            success: $.proxy(function (result) {
                // console.log(result)
                $('.textarea').val('')
                $('.textinput').val('')
                $('#comment_list').html(result)
                reattach()
                // $('#comment_list').html(result)
                // reattach()
                // $('#posts').fadeOut(150)
                // setTimeout(function(){
                //     $('#comment_list').html(result)
                // }, 150)
                // $('#posts').fadeIn(150)
            }, this)
        });
    })
}

function reattach(){
    $('.reply_form_ajax').submit(function(form){
        form.preventDefault()
        let data=$(this).serialize()
        console.log(data)
        $.ajax({
            type: "POST",
            url: '/naturestories/new_reply_ajax',
            data: data,
            success: $.proxy(function (result) {
                // console.log(result)
                $('#comment_list').html(result)
                reattach()
                // $('#posts').fadeOut(150)
                // setTimeout(function(){
                //     $('#comment_list').html(result)
                // }, 150)
                // $('#posts').fadeIn(150)
            }, this)
        });
    })
}