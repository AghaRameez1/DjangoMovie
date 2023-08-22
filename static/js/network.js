var djangoNetworkModule = {

    post: function () {
        return 'POST';
    },

    get: function () {
        return 'GET';
    },

    put: function () {
        return 'PUT';
    },

    delete: function () {
        return 'DELETE';
    },

    _getCookies: function _getCookies(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;

    },

    getTemplate: function _getTemplate(url, type, success) {
        return $.ajax({
            url: url,
            type: type,
            success: success,
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", djangoNetworkModule._getCookies('csrftoken'));
            },
            error: function (xhr, textStatus, errorThrown) {
                console.log('error');
            }
        });
    },


    getData: function _getData(url, type, data, success, error) {
        return $.ajax({
            url: url,
            type: type,
            data: data,
            success: success,
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", djangoNetworkModule._getCookies('csrftoken'));
            },
            error: error
        });
    },

    multiUploadData: function _getData(url, type, data, success) {
        return $.ajax({
            url: url,
            type: type,
            data: data,
            success: success,
            processData: false,
            contentType: false,
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", djangoNetworkModule._getCookies('csrftoken'));
            },
            error: function (xhr, textStatus, errorThrown) {
                console.log(xhr);
                console.log(textStatus);
                console.log(errorThrown);
            }
        });
    },

    init: function () {
        this.getData();
        this.multiUploadData();
        this.getTemplate();
        this.post();
        this.get();
        this.put();
        this.delete();
    }

};


function ajax_get_request(url) {
    var mes = "";
    mes = $.ajax(
        {
            url: url,
            type: 'GET',
            success: function (response) {

                return response;
            },
            error: function (error) {
                return error;
            }
        });
    return mes;

}

function ajax_post_request(url, data) {
    $.ajax({
        url: url,
        type: 'post',
        data: data,
        success: function (response) {
            return response
        },
        error: function (error) {
            return error
        }
    });
}