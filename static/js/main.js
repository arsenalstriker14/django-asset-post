function processJobNumber(){
    url = $('#qp_button').attr('href');
    var input = $('#job_id').val();
    var input = input.toUpperCase();
    if (input.length < 8 || input.length > 15) {
        alert ("Please input a valid job number");
    }else{
        var href = url + input;
        showQuickpost(href);
    }
}



function showQuickpost(url) {
    $('.shell').css('margin', '0');
    $('.stage').fadeOut( "fast", function() { });
    $('#inbox_frame').attr('src', url);
    $('#inbox_frame').fadeIn(4000, function() { })
}


function showDashboard() {
    url = $('#inbox_button').attr('href');
    $('.shell').css('margin', '0');
    $('.stage').fadeOut( "fast", function() { });
    $('iframe').fadeOut( "fast", function() { });
    $('#inbox_frame').attr('src', url);
    $('#inbox_frame').fadeIn(4000, function() { });
    
//  newwindow=window.open(url,'WRMS | Project Inbox','height=700, width=1200,top=20,left=0,resizable');
//  if (window.focus) {newwindow.focus()}
}


function addOnload(newFunction) {
    var oldOnload = window.onload;

    if (typeof oldOnload == "function") {
        window.onload = function() {
            if (oldOnload) {
                oldOnload();
            }
            newFunction();
        }
    }
    else {
        window.onload = newFunction;
    }

}

function addRow(){
    var hiddenrow = document.getElementsByClassName("postrequest_row");
console.log(hiddenrow);
    for(var i=0; i< hiddenrow.length; i++){
        console.log(hiddenrow[i].style);
        var styleDisplay = getStyle(hiddenrow[i], "display");

        if(styleDisplay  == "none"){
            hiddenrow[i].style.display = "block";
            break;
        }
    }
}
function addLink(){
    var hiddenrow = document.getElementsByClassName("request_row");
console.log(hiddenrow);
    for(var i=0; i< hiddenrow.length; i++){
        console.log(hiddenrow[i].style);
        var styleDisplay = getStyle(hiddenrow[i], "display");

        if(styleDisplay  == "none"){
            hiddenrow[i].style.display = "block";
            break;
        }
    }
}

function callTacticPage(){
    window.open ("../../newtacticpage", "Create New Tactic Page", "width=500", "height=400");
}
function getStyle(el, styleProp)
{
    if (el.currentStyle)
        var y = el.currentStyle[styleProp];
    else if (window.getComputedStyle)
        var y = document.defaultView.getComputedStyle(el,null).getPropertyValue(styleProp);
    return y;
}

//jQuery(document).ready(function() {
//  $("#accordion").accordion({
//  collapsible: true,
//  active: false
//  });
//});


//jQuery(document).ready(function() {
//  $("#apps_accordion").accordion({
//  collapsible: true,
//  active: false
//  });
//});
    
    

        
    jQuery(document).ready(function() {
        $('.newdialog').click(function(e) {
            e.preventDefault();
            var $this = $(this);
            var horizontalPadding = 15;
            var verticalPadding = 15;
            $('<iframe id="externalSite" class="externalSite" src="' + this.href + '" />').dialog({
                title: ($this.attr('title')) ? $this.attr('title') : 'WEdb Module: Contact',
                autoOpen: true,
                width: 1000,
                height: 600,
                modal: false,
                resizable: true,
                autoResize: true,
                scrolling: false,
                overlay: {
                    opacity: 0.3,
                    background: "black"
                }
            }).width(1000 - horizontalPadding).height(600 - verticalPadding);           
        });
    });
    
    jQuery(document).ready(function() {
        $('.studiodialog').click(function(e) {
            e.preventDefault();
            var $this = $(this);
            var horizontalPadding = 15;
            var verticalPadding = 15;
            $('<iframe id="externalSite" class="externalSite" src="' + this.href + '" />').dialog({
                title: ($this.attr('title')) ? $this.attr('title') : '',
                autoOpen: true,
                width: 1000,
                height: 600,
                modal: false,
                resizable: true,
                autoResize: true,
                scrolling: false,
                overlay: {
                    opacity: 0.3,
                    background: "black"
                }
            }).width(1000 - horizontalPadding).height(600 - verticalPadding);           
        });
    });
    
    jQuery(document).ready(function() {
        $('.filebrowser').click(function(e) {
            e.preventDefault();
            var $this = $(this);
            var horizontalPadding = 15;
            var verticalPadding = 15;
            $('<iframe id="externalSite" class="externalSite" src="' + this.href + '" />').dialog({
                title: ($this.attr('title')) ? $this.attr('title') : 'APPS Module: ArchiveBrowser',
                autoOpen: true,
                width: 1000,
                height: 500,
                modal: false,
                resizable: true,
                autoResize: true,
                scrolling: false,
                overlay: {
                    opacity: 0.3,
                    background: "black"
                }
            }).width(1000 - horizontalPadding).height(500 - verticalPadding);           
        });
    });
    

function showdiv(id){
    var postdiv_1 = document.getElementById('postdiv_1');
    var postdiv_2 = document.getElementById('postdiv_2');
    var postdiv_3 = document.getElementById('postdiv_3');
    var postdiv_4 = document.getElementById('postdiv_4');
    var postdiv_5 = document.getElementById('postdiv_5');
    var postdiv_6 = document.getElementById('postdiv_6');
    var postdiv_7 = document.getElementById('postdiv_7');
    var postdiv_8 = document.getElementById('postdiv_8');
    
    var node = document.getElementById( id );

      // Check to see if valid node and if node is a SELECT form control

      if( node &&
        node.tagName == "SELECT" ){
        postdiv_1.style.visibility = "hidden";
        postdiv_2.style.visibility = "hidden";
        postdiv_3.style.visibility = "hidden";
        document.getElementById('postdiv_' + node.options[node.selectedIndex].value).style.visibility = 'visible';
    }
    
}
    

//addOnload(checkHeaders_m1)
//addOnload(checkHeaders_m2)
//addOnload(checkHeaders_m3)
//addOnload(checkHeaders_m4)
//addOnload(checkHeaders_m5)
//addOnload(checkHeaders_cm1)
//addOnload(checkHeaders_cm2)
//addOnload(checkHeaders_cm3)
//addOnload(checkHeaders_cm4)
//addOnload(checkHeaders_cm5)
//addOnload(checkHeaders_ce1)
//addOnload(checkHeaders_ce2)
//addOnload(checkHeaders_ce3)
//addOnload(checkHeaders_ce4)
//addOnload(checkHeaders_ce5)
//addOnload(checkHeaders_cd1)
//addOnload(checkHeaders_cd2)
//addOnload(checkHeaders_cd3)
//addOnload(checkHeaders_cd4)
//addOnload(checkHeaders_cd5)

//function goHome(){
//  window.location = 'http://localhost:8000/main/';
//}

//function addEvent(obj, evt, fn, capture){
//  var anchor = document.getElementById("logo_temp");
    
//  if (onload.attachEvent){
//      obj.attachEvent("on" + evt, fn);
//  }
//  else{
//      if (!capture) capture = false;
//      obj.addEventListener(evt, fn, capture);
//  }
//}
//addEvent(anchor, "click", goHome);
    

    



