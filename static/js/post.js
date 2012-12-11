
// When the DOM is ready...
$(function(){
	
	// Hide stuff with the JavaScript. If JS is disabled, the form will still be useable.
	// NOTE:
	// Sometimes using the .hide(); function isn't as ideal as it uses display: none; 
	// which has problems with some screen readers. Applying a CSS class to kick it off the
	// screen is usually prefered, but since we will be UNhiding these as well, this works.
	$(".name_wrap").hide();
	$(".name_wrap2").hide();
	
	/**
	var list = document.getElementById("Pos-icon").getElementsByTagName("img");
	for(i=0;i<list.length;i++) {
		list[i].style.display="none";
	}
	
	**/

	$("#opt_0").click(function(){
		//alert("hahaha");
		$(".name_wrap").slideUp().find("input").removeClass("active_name_field");
		$("#Mood").slideDown().find("input").addClass("active_name_field");
	});

	$("#opt_1").click(function(){
		//alert("hahaha");
		$(".name_wrap").slideUp().find("input").removeClass("active_name_field");
		$("#Post").slideDown().find("textarea").addClass("active_name_field");
		
	});
	$("#opt_2").click(function(){
		//alert("hahaha");
		$(".name_wrap").slideUp().find("input").removeClass("active_name_field");
		$("#Dietary").slideDown().find("input").addClass("active_name_field");
		
	});
	$("#Mood-Pos").click(function(){
		//alert("hahaha");
		$(".name_wrap2").slideUp().find("div").removeClass("active_name_field");
		$("#Pos-icon").slideDown().find("div").addClass("active_name_field");
		
	});
	$("#Mood-Neg").click(function(){
		//alert("hahaha");
		$(".name_wrap2").slideUp().find("div").removeClass("active_name_field");
		$("#Neg-icon").slideDown().find("div").addClass("active_name_field");
		
	});
	$("#Mood-Neu").click(function(){
		//alert("hahaha");
		$(".name_wrap2").slideUp().find("div").removeClass("active_name_field");
		$("#Neu-icon").slideDown().find("div").addClass("active_name_field");
		
	});	

	$(".mood-icon").click(function(){
		var imgid = String(this.id);
		var category = imgid.substring(0,3);
		if(this.alt==="false"){
			document.getElementById("choice").appendChild(this);
			this.setAttribute("alt","true");
		}else if(this.alt==="true"){
			if(category==="pos"){
				document.getElementById("Pos-icon").appendChild(this);
			}else if(category==="neg"){
				document.getElementById("Neg-icon").appendChild(this);
			}else if(category==="neu"){
				document.getElementById("Neu-icon").appendChild(this);
			}
			
			this.setAttribute("alt","false");
		}

		var tb = document.getElementById('mood_submit');
            if (tb.style.display == 'none') {
                tb.style.display = '';
        }
	});

});



