/*
 *
 *	Carousel Class for Mootools 1.2
 *	Written by Andrew Plummer 9.17.2008
 *
 *	Usage: var x = new Carousel(id, options);
 *
 *	Options:
 *
 *		speed:number  - The speed for the thumbnails to move on scroll.
 *		scroll:number - Scroll offset on init.
 *		tips:boolean  - Add tooltips to the thumbnails (requires title element);
 *
 *
 *	HTML Required:
 *
 *	├ .stage
 *	│   │
 *	│   │ .item (one)
 *  |   └ .item (two)
 *	│
 *	├ .leftButton
 *	├ .rightButton
 *	└ .scroll
 *	    │
 *	    └ ul
 *        │
 *        │ li (one)
 *        └ li (two)
 *
 */

var Carousel = new Class({

	Implements: Options,

	options: {
		speed: 300,
		scroll: null,
		tips: false
	},


	initialize: function(id, options){
	
		this.setOptions(options);
		this.carousel = $(id);
		if(!this.carousel) return;
		
		this.stage = this.carousel.getElement(".stage");
		this.scroll = this.carousel.getElement(".scroll");
		this.ul = this.scroll.getElement("ul");
		
		this.leftButton = this.carousel.getElement(".leftButton");
		this.rightButton = this.carousel.getElement(".rightButton");
		
		this.scroll.setStyle("overflow", "hidden");
		this.stage.setStyle("overflow", "hidden");
	
		this.scrollEffect = new Fx.Scroll(this.scroll, {
			transition: Fx.Transitions.Expo.easeOut,
			duration: 2000,
			link: 'cancel',
			wheelStops: false
		});

		this.carousel.addEvent("keypress", function(event){
			if(event.key == "left" && this.currentIndex > 0){
				var prevIndex = this.currentIndex - 1;
				var prevThumbnail = this.thumbnails[prevIndex];
				this.highlight(prevThumbnail);
				this.show(prevIndex);
				this.scrollTo(prevThumbnail);
			}
			if(event.key == "right" && this.currentIndex < this.items.length - 1){
				var nextIndex = this.currentIndex + 1;
				var nextThumbnail = this.thumbnails[nextIndex];
				this.highlight(nextThumbnail);
				this.show(nextIndex);
				this.scrollTo(nextThumbnail);
			}
		}.bindWithEvent(this));
		
		this.scroll.addEvent("mousewheel", function(event){
			event.preventDefault();
			this.position -= event.wheel * 200;
			if(this.position < 0) this.position = 0;
			if(this.position > this.max) this.position = this.max;
			this.scrollTo(this.position);
		}.bindWithEvent(this));
		
		this.scrollWidth = this.scroll.getSize().x;
		this.max = this.ul.getSize().x - this.scroll.getSize().x;
		this.speed = this.options.speed;
		this.position = this.options.scroll || Math.round(this.max / 2);
		this.scrollEffect.set(this.position);
		

		this.leftButton.addEvent("click", function(){
			this.position -= (this.position > 0) ? this.speed : 0;
			this.scrollTo(this.position);
		}.bindWithEvent(this));

		this.rightButton.addEvent("click", function(){
			this.position += (this.position < this.max) ? this.speed : 0;
			this.scrollTo(this.position);
		}.bindWithEvent(this));

		this.thumbnails = this.scroll.getElements("li");
		this.thumbnails.each(function(el){

			el.linkedIndex = this.thumbnails.indexOf(el);
			el.setStyle("opacity", 0.3);
			el.set("tween", {duration: 200});
			el.addEvents({
				mouseover: function(event){ el.fade(1); },
				mouseout:  function(event){ if(!el.current) el.fade(0.3); },
				click: function(event, haha){
					this.highlight(el);
					this.scrollTo(el);
					if(this.currentIndex != el.linkedIndex){
						this.show(el.linkedIndex);
					}
					return false;
				}.bindWithEvent(this)
			});
			el.getElements("a").each(function(el){
				el.onclick = function(){ return false; }
			}.bind(this));
		}.bind(this));
		
		
		this.items = new Array();
		
		var itemArray = this.stage.getElements("div.item");
		
		// Set up a random thumbnail for init
		var rand = itemArray.getRandom();
		this.currentIndex = itemArray.indexOf(rand);
		var randThumb = this.thumbnails[this.currentIndex];
		
		randThumb.fade(1);
		randThumb.current = true;
		this.scrollTo(randThumb);
		
		itemArray.each(function(el){
		
			el.fadeOut = function(){
			
				this.get("tween").onComplete = this.dispose;
				this.fade("out");
			}
			el.fadeIn = function(){
			
				this.fade("hide");
				this.fade("in");
			}
			this.items.push(el);
			if(el != rand) el.dispose();
			else el.fadeIn();
		
		}, this);
		
		
		if(this.options.tips) new Tips(".hastip", {className:'tool-tip'});
	},
	
	scrollTo: function(destination){
	
		if($type(destination) == "number"){
			this.scrollEffect.start(destination);
		} else if($type(destination) == "element"){
			var x = destination.getPosition(this.scroll).x;
			x -= (this.scrollWidth - destination.getSize().x) / 2; // Line it up in the center
			this.scrollEffect.start(x);
			this.position = x;
		}	
	},
	
	show: function(index){
	
		var prevItem = this.items[this.currentIndex];
		var nextItem = this.items[index];
		nextItem.inject(this.stage);
		prevItem.setStyle("position", "absolute");
		prevItem.fadeOut();
		nextItem.fadeIn();
		this.currentIndex = index;
	},
	
	highlight: function(thumbnail){
	
		this.thumbnails.each(function(el){
			if(el == thumbnail){
				el.current = true;
				el.fireEvent("mouseover", {target: el});
			} else {
				el.current = false;
				el.fireEvent("mouseout", {target: el});
			}
		});
	}
});
