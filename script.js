$(function(){
	var ws = new WebSocket('ws://localhost:8888/push')

	ws.onopen = function(){}
	ws.onmessage = function(evt){
		$("#content").append(parse(evt.data))
	}
	ws.onclose = function(){}	

	$('#reply').keypress(function (e) {
	 var key = e.which;
	 if(key == 13)  // the enter key code
	  {
	  	$("#content").append(parse($("#reply").val(),'self'))
	    ws.send($("#reply").val())
	    $("#reply").val('')
	    return false;  
	  }
	}); 
})

function parse(message, flag){
	if(flag == 'self'){
		return '<li><b style="color:blue">You: </b><span class="message">' + message + '</span></li>'
	}else{
		return '<li><b style="color:red">Captain Phasma: </b><span class="message">' + message + '</span></li>'
	}
	
}
