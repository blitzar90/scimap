angular.module('scimap', []).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[').endSymbol(']}');
})
.controller('Main', [ '$scope', '$http', function(scope, http) {
	console.log('hello');

	scope.nodes = [];

	var data = {
		nodes : [],
		links : []
	};

	var linkCounter = 0;
	var colorMap = {};

	scope.init = function() {
		getNodes();
	}

	scope.onSelect = function(el) {
		console.log(el);
	}

	function getNodes() {
		http.get('/nodes').then((data) => {
			scope.nodes = data.data;

			makeChart(prepareData(scope.nodes));

			// console.log(prepareData(scope.nodes));

		}, (error) => {
			console.log(error);
		});
	}

	function ChartLink(from, to) {
		this.id = linkCounter++;
		this.from = from;
		this.to = to;
		this.style = {
			toDecoration : 'arrow'
		}
	}

	function Node(data) {
		for (let i in data) {
			this[i] = data[i];
		}

		function ChartNode(data) {
			this.id = data.id;
			this.style = {
				label : data.title,
				fillColor : colorMap[data.area[0]]
			}
		}

		this.transform = () => {
			return new ChartNode(this);
		}
	}

	function prepareData(nodes) {

		nodes = nodes.map(el => new Node(el));
		_obj = {};
		links = [];

		for (let node1 of nodes) {
			if (node1.toNodes) {
				for (node1_out_id of node1.toNodes) {
					let str = node1.id + '::' + node1_out_id;
					_obj[str] = true;
				}
			}
		}

		for (let key in _obj) {
			let split = key.split('::');

			links.push(new ChartLink(split[0], split[1]));
		}

		makeColorMap(nodes);

		return {
			nodes : nodes.map(el => el.transform()), links
		}
	}

	function makeChart(data) {

		console.log(data);

		var t = new NetChart({
	        container: document.getElementById("demo"),
	        area: { height: $('body').height() - 5 },
	        data : {
				preloaded : data
	        },
	        // data: { url: "https://zoomcharts.com/dvsl/data/net-chart/discovery-example.json" },
	        // info:{
	        //     enabled: true,
	        //     nodeContentsFunction: function(itemData, item){
	        //         return "<div style='margin:auto; width:200px; height:100%; padding': 10px;>" +
	        //                     "<h3 style='font-weight: 300; font-size: 21px; color: #2f256e; padding-bottom: 3px; margin:0px'>"+ itemData.title +"</h3>" +
	        //                     "<p style='font-size: 13px;font-family: Arial, Helvetica, sans-serif;font-weight: 300;padding:5px'>" + itemData.description + "</p>" +
	        //                "</div>";
	        //   },
	        //     linkContentsFunction: function(itemData, item){
	        //         //console.log(item);
	        //         return  "<p style='padding-left:5px;padding-right:5px;'>" + " Walking time between " + item.from.data.title + " and " + item.to.data.title + " " + itemData.walkingtime + "</p></div>";
	        //     }
	        // },
	        // style:{
	        //     nodeLabel:{
	        //         backgroundStyle:{fillColor:"#93B17F", lineColor:"blue"}
	        //     },
	        //     linkLabel:{
	        //         backgroundStyle:{fillColor:"#93B17F", lineColor:"blue"}
	        //     },
	        //     nodeStyleFunction: nodeStyle,
	        //     link:{fillColor:"#93B17F"}
	        // }
	    });
	}

	function getRandomColor() {
		var letters = '0123456789ABCDEF';
		var color = '#';
		for (var i = 0; i < 6; i++) {
			color += letters[Math.floor(Math.random() * 16)];
		}
		return color;
	}

	function makeColorMap(nodes) {
		for (let node of nodes) {
			for (let key of node.area) {
				colorMap[key] = true;
			}
		}

		for (key in colorMap) {
			colorMap[key] = getRandomColor();
		}

		console.log(colorMap);
	}



    function nodeStyle(node){
        node.image = "https://zoomcharts.com/dvsl/data/net-chart/discovery-net/n" + node.id.split("n")[1] + ".jpg";
        node.label = node.data.title;
    }


}]);