//This javascript should not be edited. Just use it.
//Nothing in this must be edited 
//
 var today = new Date();
 var dd = today.getDate();
 var mm = today.getMonth() + 1;
 var yy = today.getFullYear()


 var hours = today.getHours();
 var minutes = today.getMinutes();
 var date_today = dd + "-" + mm + "-" + yy
 var time_now = hours + ":" + minutes
 var long_usrid = "%%USER_ID%%"; //get the User ID as a string  

 var server_url = "http://analytics-api.vlabs.ac.in:4000/"

 var xhttp = new XMLHttpRequest();
 var urlstr = server_url + long_usrid + "," + courseid + "," + date_today + "," + time_now + "," + experiment_name + "," + lab_name
 xhttp.open("GET", urlstr, true);
 xhttp.send();
