function getBathValue(){
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms)
    {
        if(uiBathrooms[i].checked)
        {
            return parseInt(i)+1;
        }
    }
    return -1;//invalid value
}

function getBHKValue(){
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK)
    {
        if(uiBHK[i].checked)
        {
            return parseInt(i)+1;
        }
    }
    return -1;
}

function onClickedEstimatePrice(){
    console.log("Estimated price Button clicked successfully");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var site_location = document.getElementById("uiLocations");
    var estprice = document.getElementById("uiEstimatedPrice");
    var url="http://127.0.0.1:5000/predict_home_price";

    $.post(url, {
        total_sqft : parseFloat(sqft.value),
        bhk : bhk,
        bath : bathrooms,
        site_location: site_location.value
    },function(data,status){
        console.log(data.estimated_price);
        estprice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });


}
function onPageLoad()
{
    console.log("document loaded");
    var url="http://127.0.0.1:5000/get_site_location_names";
    $.get(url,function(data, status){
        console.log("got response for get_site_location_names request")
        if(data)
        {
            var  site_location= data.site_locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in site_location){
                var opt = new Option(site_location[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}
window.onload = onPageLoad;