const btnCancel = document.querySelector('.btn-cancel');

btnCancel.addEventListener('click', function(){
    var url = "http://127.0.0.1:8000/"
    document.location.href = url;
});