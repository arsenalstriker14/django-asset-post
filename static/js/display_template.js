addOnload(checkHeaders_fr)
addOnload(checkContent_cd)
addOnload(checkContent_ce)
addOnload(checkContent_cm)
addOnload(checkContent_m)
addOnload(checkContent_fr)

for (var i = 1; i < 21; i++) {
    addOnload(window['checkHeaders_m' + i]);
}

for (var i = 1; i < 21; i++) {
    addOnload(window['checkHeaders_cm' + i]);
}

for (var i = 1; i < 21; i++) {
    addOnload(window['checkHeaders_ce' + i]);
}

for (var i = 1; i < 21; i++) {
    addOnload(window['checkHeaders_cd' + i]);
}




function addOnload(newFunction){
    var oldOnload = window.onload;
    
    if (typeof oldOnload == "function"){
        window.onload = function(){
            if(oldOnload){
                oldOnload();
            }
            newFunction();
        }
    }
    else{
        window.onload = newFunction;
    }
    
}

function displayLink(){
    var displaylinks = document.getElementsByClassName('showlink');
    for(var i=0; i < displaylinks.length; i++){
        var linklength = displaylinks[i].getAttribute('href').length;
        var linkvalue = displaylinks[i].getAttribute('href').toString();
        if ( linklength > 18 || linkvalue.indexOf('http') > -1 ){
            displaylinks[i].parentNode.style.display = "inline";
            displaylinks[i].parentNode.style.float = "left";
            displaylinks[i].parentNode.style.borderRight = "1px solid #000";
            displaylinks[i].parentNode.style.textAlign = "center";
            displaylinks[i].parentNode.style.padding = "0 5px";
        }

    }
        
}

function checkContent_cd(){
    var cdItems = $('[id^="cd_round"]');
    
    if (cdItems.length > 0){
        document.getElementById('cd_div').style.display = "block"; 
    }
    else{
        document.getElementById('cd_div').style.display = "none";
    }
}

function checkContent_ce(){
    var ceItems = $('[id^="ce_round"]');
    
    if (ceItems.length > 0){
        document.getElementById('ce_div').style.display = "block"; 
    }
    else{
        document.getElementById('ce_div').style.display = "none";
    }
}

function checkContent_cm(){
    var cmItems = $('[id^="cm_round"]');
    
    if (cmItems.length > 0){
        document.getElementById('cm_div').style.display = "block"; 
    }
    else{
        document.getElementById('cm_div').style.display = "none";
    }
}

function checkContent_m(){
    var mItems = $('[id^="m_round"]');
    
    if (mItems.length > 0){
        document.getElementById('m_div').style.display = "block"; 
    }
    else{
        document.getElementById('m_div').style.display = "none";
    }
}

function checkContent_fr(){
    var frItems = document.getElementById('FinalRelease');
    
    if (! frItems){
        document.getElementById('fr_div').style.display = "none";
    }
    else{
        document.getElementById('fr_div').style.display = "block";
    }
}
    
function checkHeaders_m1(){
    var hdrSet = document.getElementsByClassName("m_round1");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m2(){
    var hdrSet = document.getElementsByClassName("m_round2");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m3(){
    var hdrSet = document.getElementsByClassName("m_round3");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m4(){
    var hdrSet = document.getElementsByClassName("m_round4");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m5(){
    var hdrSet = document.getElementsByClassName("m_round5");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m6(){
    var hdrSet = document.getElementsByClassName("m_round6");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m7(){
    var hdrSet = document.getElementsByClassName("m_round7");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m8(){
    var hdrSet = document.getElementsByClassName("m_round8");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m9(){
    var hdrSet = document.getElementsByClassName("m_round9");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m10(){
    var hdrSet = document.getElementsByClassName("m_round10");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m11(){
    var hdrSet = document.getElementsByClassName("m_round11");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m12(){
    var hdrSet = document.getElementsByClassName("m_round12");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m13(){
    var hdrSet = document.getElementsByClassName("m_round13");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m14(){
    var hdrSet = document.getElementsByClassName("m_round14");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m15(){
    var hdrSet = document.getElementsByClassName("m_round15");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m16(){
    var hdrSet = document.getElementsByClassName("m_round16");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m17(){
    var hdrSet = document.getElementsByClassName("m_round17");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m18(){
    var hdrSet = document.getElementsByClassName("m_round18");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m19(){
    var hdrSet = document.getElementsByClassName("m_round19");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_m20(){
    var hdrSet = document.getElementsByClassName("m_round20");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}


function checkHeaders_cm1(){
    var hdrSet = document.getElementsByClassName("cm_round1");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm2(){
    var hdrSet = document.getElementsByClassName("cm_round2");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm3(){
    var hdrSet = document.getElementsByClassName("cm_round3");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm4(){
    var hdrSet = document.getElementsByClassName("cm_round4");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm5(){
    var hdrSet = document.getElementsByClassName("cm_round5");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm6(){
    var hdrSet = document.getElementsByClassName("cm_round6");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm7(){
    var hdrSet = document.getElementsByClassName("cm_round7");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm8(){
    var hdrSet = document.getElementsByClassName("cm_round8");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm9(){
    var hdrSet = document.getElementsByClassName("cm_round9");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm10(){
    var hdrSet = document.getElementsByClassName("cm_round10");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm11(){
    var hdrSet = document.getElementsByClassName("cm_round11");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm12(){
    var hdrSet = document.getElementsByClassName("cm_round12");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm13(){
    var hdrSet = document.getElementsByClassName("cm_round13");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm14(){
    var hdrSet = document.getElementsByClassName("cm_round14");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm15(){
    var hdrSet = document.getElementsByClassName("cm_round15");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm16(){
    var hdrSet = document.getElementsByClassName("cm_round16");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm17(){
    var hdrSet = document.getElementsByClassName("cm_round17");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm18(){
    var hdrSet = document.getElementsByClassName("cm_round18");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm19(){
    var hdrSet = document.getElementsByClassName("cm_round19");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cm20(){
    var hdrSet = document.getElementsByClassName("cm_round20");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce1(){
    var hdrSet = document.getElementsByClassName("ce_round1");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce2(){
    var hdrSet = document.getElementsByClassName("ce_round2");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce3(){
    var hdrSet = document.getElementsByClassName("ce_round3");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce4(){
    var hdrSet = document.getElementsByClassName("ce_round4");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce5(){
    var hdrSet = document.getElementsByClassName("ce_round5");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce6(){
    var hdrSet = document.getElementsByClassName("ce_round6");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce7(){
    var hdrSet = document.getElementsByClassName("ce_round7");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce8(){
    var hdrSet = document.getElementsByClassName("ce_round8");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce9(){
    var hdrSet = document.getElementsByClassName("ce_round9");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce10(){
    var hdrSet = document.getElementsByClassName("ce_round10");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce11(){
    var hdrSet = document.getElementsByClassName("ce_round11");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce12(){
    var hdrSet = document.getElementsByClassName("ce_round12");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce13(){
    var hdrSet = document.getElementsByClassName("ce_round13");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce14(){
    var hdrSet = document.getElementsByClassName("ce_round14");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce15(){
    var hdrSet = document.getElementsByClassName("ce_round15");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce16(){
    var hdrSet = document.getElementsByClassName("ce_round16");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce17(){
    var hdrSet = document.getElementsByClassName("ce_round17");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce18(){
    var hdrSet = document.getElementsByClassName("ce_round18");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce19(){
    var hdrSet = document.getElementsByClassName("ce_round19");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_ce20(){
    var hdrSet = document.getElementsByClassName("ce_round20");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd1(){
    var hdrSet = document.getElementsByClassName("cd_round1");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd2(){
    var hdrSet = document.getElementsByClassName("cd_round2");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd3(){
    var hdrSet = document.getElementsByClassName("cd_round3");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd4(){
    var hdrSet = document.getElementsByClassName("cd_round4");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd5(){
    var hdrSet = document.getElementsByClassName("cd_round5");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd6(){
    var hdrSet = document.getElementsByClassName("cd_round6");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd7(){
    var hdrSet = document.getElementsByClassName("cd_round7");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd8(){
    var hdrSet = document.getElementsByClassName("cd_round8");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd9(){
    var hdrSet = document.getElementsByClassName("cd_round9");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd10(){
    var hdrSet = document.getElementsByClassName("cd_round10");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd11(){
    var hdrSet = document.getElementsByClassName("cd_round11");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd12(){
    var hdrSet = document.getElementsByClassName("cd_round12");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd13(){
    var hdrSet = document.getElementsByClassName("cd_round13");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd14(){
    var hdrSet = document.getElementsByClassName("cd_round14");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd15(){
    var hdrSet = document.getElementsByClassName("cd_round15");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd16(){
    var hdrSet = document.getElementsByClassName("cd_round16");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd17(){
    var hdrSet = document.getElementsByClassName("cd_round17");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd18(){
    var hdrSet = document.getElementsByClassName("cd_round18");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd19(){
    var hdrSet = document.getElementsByClassName("cd_round19");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_cd20(){
    var hdrSet = document.getElementsByClassName("cd_round20");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}

function checkHeaders_fr(){
    var hdrSet = document.getElementsByClassName("FinalRelease");
    var titles = {};

    for (var i=0; i<hdrSet.length; i++){
        if ( !titles[ hdrSet[i].title ] )  {
            titles[ hdrSet[i].title ] = true;
            hdrSet[i].style.display = "table-row";
        }
    }
}