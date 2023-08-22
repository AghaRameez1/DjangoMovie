function signinForm() {
    let type = djangoNetworkModule.post();
    let url = '/signup/';
    let data = $('#signinForm').serialize();
    djangoNetworkModule.getData(url, type, data, function (response) {
        if (response.status == 401) {
            swal.fire('Error', 'User already exists', 'error');
            return;
        }
        if (!response.status) {
            $('#signinForm').html(response)
        } else {
            swal.fire({
                title: response.status,
                text: response.message,
                type: response.status,
                confirmButtonText: "OK",
            });
            $('#signinForm').trigger('reset');
        }
    });

}

function loginForm() {
    let type = djangoNetworkModule.post();
    let url = '/login/';
    let data = $('#loginForm').serialize();
    djangoNetworkModule.getData(url, type, data, function (response) {
        if (!response.status) {
            $('#loginForm').html(response)
        }else if (response.status == 401){
            swal.fire({
                title: 'Error',
                text: 'Invalid Credientials',
                icon: 'error',
                confirmButtonText: "OK",
            });
        }else if( response.status == 'error'){
            swal.fire({
                title: 'Error',
                text: 'User not found',
                icon: 'error',
                confirmButtonText: "OK",
            });
        } else {
            swal.fire({
                title: response.status,
                text: response.message,
                icon: response.status,
                confirmButtonText: "OK",
            });
            window.location.href = '/movies';
            $('#loginForm').trigger('reset');
        }
    });
}

function logout() {
    let type = djangoNetworkModule.get();
    let url = '/logout/';
    let data = '';
    djangoNetworkModule.getData(url, type, data, function (response) {
        if(response.status === 'success'){
            window.location.href = '/';
        }
    });
}

