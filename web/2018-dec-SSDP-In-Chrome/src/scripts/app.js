//see http://www.upnp.org/specs/arch/UPnP-arch-DeviceArchitecture-v1.0-20080424.pdf for more information
// on SSDP and UPNP

const SSDP_ADDRESS = '239.255.255.250';
const SSDP_PORT = 1900;
const SSDP_REQUEST_PAYLOAD =    "M-SEARCH * HTTP/1.1\r\n"+
                                "HOST: 239.255.255.250:1900\r\n"+
                                "MAN: \"ssdp:discover\"\r\n"+
                                "MX: 3\r\n"+
                                "ST: ssdp:all\r\n"+
                                "USER-AGENT: Joel's SSDP Implementation\r\n\r\n";

var searchSocket = null;

function beginSSDPDiscovery() { 
    if (searchSocket)
        return;
    $('.responseList').empty();
    searchSocket = new MulticastSocket({address:SSDP_ADDRESS, port:SSDP_PORT});
    searchSocket.onDiagram = function(arrayBuffer, remote_address, remote_port) {
        console.log('response from ', remote_address, " ", remote_port);
        var msg = searchSocket.arrayBufferToString8(arrayBuffer);
        console.log(msg);
        discoveryData = discoveryStringToDiscoveryDictionary(msg);
        console.log(discoveryData);

        var template = $('.palette').find('.ssdpDevice').clone();
        $(template).find('.ipAddress').text(remote_address);
        $(template).find('.location').text(discoveryData.location);
        //$(template).find('.location').attr('href', discoveryData.location);
        $(template).find('.server').text(discoveryData.server);
        $(template).find('.searchTarget').text(discoveryData.st)
        $('.responseList').append(template);
    }
    searchSocket.connect({call:function(c) {
        console.log('connect result',c);
        searchSocket.sendDiagram(SSDP_REQUEST_PAYLOAD,{call:()=>{console.log('success')}});
        setTimeout(endSSDPDiscovery, 5000);
    }});    
}

function endSSDPDiscovery() {
    if(searchSocket) {
        searchSocket.disconnect();
        searchSocket = null;
    }
}

function discoveryStringToDiscoveryDictionary(str) {
    var lines = str.split('\r');
    var retVal = {}
    lines.forEach((l) => {
        var del = l.indexOf(':');
        if(del>1) {
            var key = l.substring(0,del).trim().toLowerCase();
            var value = l.substring(del+1).trim();
            retVal[key]=value;
        }
    });
    return retVal;
}

function main() { 
    $('#scanNetworkButton').on('click', beginSSDPDiscovery);
}


$(document).ready(main);


if('serviceWorker' in navigator) {
    navigator.serviceWorker
             .register('./sw.js')
             .then(function() { console.log("Service Worker Registered"); });
  }