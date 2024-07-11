function saveComm(obj, id) {
    let comment = $("#id_text").val()
    if (comment != '') {
        $.ajax({
            url: '/cAdd/',
            type: 'POST',
            data: {
                'text': comment,
                'id': id
                },
            success: function (response) {
                alert('Добавленный комментарий: '+response['text'])
                $('#id_text').val('')
                }
            })
        }
    }