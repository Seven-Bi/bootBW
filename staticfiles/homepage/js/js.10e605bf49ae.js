  $(function(){
   $(".hash1,.hash2,.hash3,.hash4,.hash5,.hash6,.c_hash2,.a_hash1,.a_hash2,.a_hash3").hashViewed({});
   $(".count_number1").hashViewed({displayClass:"count_number"});
     $("body").on('click','.animateTo',function(){
            var id = $(this).attr("go-to");
            $('html,body').animate({scrollTop:$('#'+id).offset().top}, 400);
        });
   function dw_tree_nodes() {
        $('.tree_node:not(:last-child) .toggle').each(function() {
            var w1 = $(this);
            var w2 = w1.parent().parent().next('.tree_node').find('.toggle');
            var even = w1.parent().parent().is(':nth-child(2n)');
            var dx = w2.offset().left - w1.offset().left - 35;
            var dy = w2.offset().top - w1.offset().top - 35;
            if (even) {
                dx += 70;
                dy += 0;
            }
            var c = Math.sqrt(Math.pow(dx, 2) + Math.pow(dy, 2));
            var angle = Math.atan(dy / dx);
            if (even) {
                angle += Math.PI;
            }
            if (w1.children('.tree_node_line').length === 0) {
                w1.append('<div class="tree_node_line" style="width:' + c + 'px; transform:rotate(' + angle + 'rad)"></div>');
            }
            w1.children('.tree_node_line').css({
                'width': c + 'px',
                'transform': 'rotate(' + angle + 'rad)'
            });
        });
    }
    $('.tree_node').each(function() {
        var text = $(this).children('.tree_text');
        var height = text.outerHeight() + 30;
        $(this).find('.toggle').attr('data-height', height);
        text.css({
            height: '10rem'
        })
    });
	
    $('.tree_node .toggle').click(function() {
        var tree_node = $(this).parent().parent('.tree_node');
        tree_node.toggleClass('expanded');
        if (tree_node.hasClass('expanded')) {
            var new_height = $(this).attr('data-height') + 'px';
        } else {
            var new_height = '10rem';
        }
        $(this).parent().next('.tree_text').animate({
            height: new_height
        }, {
            duration: 400,
            easing: 'swing',
            step: function() {
                dw_tree_nodes();
            }
        });
    });
  
    $('body').on("click", ".ScrollTopBtn",
            function() {
                $('html,body').animate({
                    scrollTop: '0px'
                },
                300);
            })
  
 
	var mainHeader = $('.auto_hide_header'),
		belowNavHeroContent = $('.main_content'),
		headerHeight = mainHeader.height();
	
	
	var scrolling = false,
		previousTop = 0,
		currentTop = 0,
		scrollDelta = 10,
		scrollOffset = 150;

  $(".menu_toggle").on("click",
    function() {
        if ($(this).hasClass('active')) {
            $(this).removeClass("active");
			$(".nav_overlay").css({opacity:0,visibility:"hidden"});
			 $(document.body).css({"overflow-y": "auto"});  	
        } else {
            $(this).addClass("active");
			mainHeader.removeClass('is-hidden');  
			mainHeader.addClass('header_nav_bg'); 
			$(".nav_overlay").css({opacity:1,visibility:"visible"});
			$(document.body).css({"overflow-y": "hidden"});  
        }
    });

	$(window).on('scroll', function(){
		if( !scrolling ) {
			scrolling = true;
			(!window.requestAnimationFrame)
				? setTimeout(autoHideHeader, 250)
				: requestAnimationFrame(autoHideHeader);
		}
	});

	$(window).on('resize', function(){
		headerHeight = mainHeader.height();
	});

	function autoHideHeader() {
		var currentTop = $(window).scrollTop();
checkStickyNavigation(currentTop) 
	   	previousTop = currentTop;
		scrolling = false;
	}


	function checkStickyNavigation(currentTop) {	
	var secondaryNavOffsetTop = belowNavHeroContent.offset().top - mainHeader.height();			
		if (previousTop >= currentTop ) {
	    	if( currentTop < secondaryNavOffsetTop ) {
	    		mainHeader.removeClass('is-hidden');  
				  	mainHeader.removeClass('header_nav_bg'); 
	    	} else if( previousTop - currentTop > scrollDelta ) {
	    		mainHeader.removeClass('is-hidden');  
				mainHeader.addClass('header_nav_bg'); 
	    	}
	    	
	    } else {
	 	  	if( currentTop > secondaryNavOffsetTop + scrollOffset ) {
	    		mainHeader.addClass('is-hidden');	  
	    	} else if( currentTop > secondaryNavOffsetTop ) {
	    		mainHeader.removeClass('is-hidden');  
	    	}

	    }
	}

     }); 
 //
  (function($) {
    $.fn.hashViewed = function(options) {
        var defaults = {
            hashDuring: 150,
            optionTop: 200,
            displayClass: "animated_top"
        };
        var options = $.extend(defaults, options || {});
        this.each(function() {
            var obj = $(this);
            $(window).scroll(function() {
                if (inView()) {
                    options.hashView = true;
				
                    hashDivDisplay();
                }
            });
            function inView() {
                var option = options.optionTop;
                var winTop = $(window).height();
                var winScrolled = $(window).scrollTop();
                var selectorTop = $(obj).offset().top;
                if (winScrolled + winTop > selectorTop + option) {
                    return true
                } else {
                    return false
                }
            }
            function hashDivDisplay() {
                $(obj).addClass(options.displayClass)
            }		
        })
    }
})(jQuery);

	$.fn.countTo = function (options) {
		options = options || {};		
		return $(this).each(function () {
			var settings = $.extend({}, $.fn.countTo.defaults, {
				from:            $(this).data('from'),
				to:              $(this).data('to'),
				speed:           $(this).data('speed'),
				refreshInterval: $(this).data('refresh-interval'),
				decimals:        $(this).data('decimals')
			}, options);
			
			var loops = Math.ceil(settings.speed / settings.refreshInterval),
				increment = (settings.to - settings.from) / loops;
			
			var self = this,
				$self = $(this),
				loopCount = 0,
				value = settings.from,
				data = $self.data('countTo') || {};			
			$self.data('countTo', data);			
			if (data.interval) {
				clearInterval(data.interval);
			}
			data.interval = setInterval(updateTimer, settings.refreshInterval);
			render(value);
			
			function updateTimer() {
				value += increment;
				loopCount++;				
				render(value);				
				if (typeof(settings.onUpdate) == 'function') {
					settings.onUpdate.call(self, value);
				}
				
				if (loopCount >= loops) {
					$self.removeData('countTo');
					clearInterval(data.interval);
					value = settings.to;
					
					if (typeof(settings.onComplete) == 'function') {
						settings.onComplete.call(self, value);
					}
				}
			}
			
			function render(value) {
				var formattedValue = settings.formatter.call(self, value, settings);
				$self.html(formattedValue);
			}
		});
	};
jQuery.divselect = function(divselectid,inputselectid) { 
	$("body").on("click",divselectid+" cite", function () {
    var ul = $(this).next("ul"); 
    if(ul.css("display")=="none"){ 
	$(this).addClass("active");
	$(".divselect_ul").hide(0);
    ul.slideDown(100); 
    }else{ 
    ul.slideUp(100); 
	$(this).removeClass("active");
    } 
	 $('body').one('click', function() {
			   ul.slideUp(100);
			   $(this).removeClass("active");
		});
		return false;
    }); 
	$("body").on("click",divselectid+" ul li a", function () {
    var txt = $(this).text(); 
	$(this).parent("li").addClass("active").siblings("li").removeClass("active");
	var cites = $(this).closest(divselectid).children("cite");
    $(cites).html(txt); 
	$(cites).removeClass("active").addClass("checked");
    var value = $(this).attr("selectid"); 
    $(this).closest(divselectid).children(inputselectid).val(value); 
	 var uls = cites.next("ul"); 
    $(uls).hide(); 
    }); 
    }; 
//select end	
	