
document.addEventListener('DOMContentLoaded',function() {
    console.log('started');
    var checkPageButton = document.getElementById('checkPage');
    var customPageButton = document.getElementById('customUrl');
    chrome.tabs.getSelected(null, function(tab) {
      document.getElementById("url").innerHTML = "URL : " + tab.url;
    });
    // tab url
    checkPageButton.addEventListener('click', function() {
  
      chrome.tabs.getSelected(null, function(tab) {
        d = document;
        console.log(tab);
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
         result = xhttp.responseText;
         if(result === "-1")
         {  
          document.getElementById("danger").innerHTML = ""; 
           document.getElementById("safe").innerHTML = "Not a phishing site"; 
          }
          else{
            document.getElementById("safe").innerHTML = ""; 
            document.getElementById("danger").innerHTML = "Phishing site! Closing in 3 seconds";
            setTimeout(()=>{
              chrome.tabs.getSelected(function(tab) {
                chrome.tabs.remove(tab.id, function() { });
            });
            },3000);
          }
      }else{
      }
      };
      xhttp.open("GET","http://localhost:5000/findout?url="+tab.url, true);
      xhttp.send();
      });
    }, false);

    // custom Url
    customPageButton.addEventListener('click', function() {
  
        var inputVal = document.getElementById("urlInput").value;
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
         result = xhttp.responseText;
         if(result === "-1")
         {  
          document.getElementById("danger").innerHTML = ""; 
           document.getElementById("safe").innerHTML = "Not a phishing site"; 
          }
          else{
            document.getElementById("safe").innerHTML = ""; 
            document.getElementById("danger").innerHTML = "Phishing site! Closing in 3 seconds";
            setTimeout(()=>{
              chrome.tabs.getSelected(function(tab) {
                chrome.tabs.remove(tab.id, function() { });
            });
            },3000);
          }
      }else{
      }
      };
      xhttp.open("GET","http://localhost:5000/findout?url="+inputVal, true);
      xhttp.send();
      
    }, false);


  }, false);