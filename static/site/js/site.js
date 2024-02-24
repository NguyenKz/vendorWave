function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
}
function getAuthorization(){
    if (getCookie('access')==null){
        return null;
    }
    return 'Bearer ' + getCookie('access');
}

function makeHeader(){
    return {
        'X-CSRFToken': '{{ csrf_token }}',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'Authorization': getAuthorization(),
    }
}