//
//function showAlert()
//{
//
//var username=document.getElementById('username').value;
//var first_name=document.getElementById('first_name').value;
//var last_name=document.getElementById('last_name').value;
//var email=document.getElementById('email').value;
//var password=document.getElementById('password').value;
//var password1=document.getElementById('password1').value;
//
//if(!username || !first_name || !last_name || !email || !password || !password)
//{
//alert('Please fillout the required fields')
//}
//else
//{
//alert('Registration successfull, now you can login');
//}
//
//}
//
//function loginAlert()
//{
//var username=document.getElementById('username').value;
//var password=document.getElementById('password').value;
//
//if(!username || !password)
//{
//alert('Please fillout the fields')
//}
//else
//{
//alert('Login successfull..');
//}
//
//}


function registerAlert()
{

var username=document.getElementById('username').value;
var password=document.getElementById('password').value;
var password2=document.getElementById('password2').value;


if(!username || !password || !password2)
{
alert('Please fillout the required fields')
}
else
{
alert('Registration successfull, now you can login');
}

}

function loginAlert()
{
var username=document.getElementById('username').value;
var password=document.getElementById('password').value;

if(!username || !password)
{
alert('Please fillout the fields')
}
else
{
alert('Login successfull..');
}

}