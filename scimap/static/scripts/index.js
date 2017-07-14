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

	scope.init = function() {
		getNodes();
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
	}

	function Node(data) {
		for (let i in data) {
			this[i] = data[i];
		}

		function ChartNode(data) {
			this.id = data.id;
			this.style = {
				label : data.title
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
			if (node1.out) {
				for (node1_out_id of node1.out) {
					let str = node1.id + '::' + node1_out_id;
					_obj[str] = true;
				}
			}
		}

		console.log(_obj);

		for (let key in _obj) {
			let split = key.split('::');

			links.push(new ChartLink(split[0], split[1]));
		}

		return {
			nodes : nodes.map(el => el.transform()), links
		}
	}

	function makeChart(data) {

		console.log(data);

		var t = new NetChart({
	        container: document.getElementById("demo"),
	        area: { height: null },
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



    function nodeStyle(node){
        node.image = "https://zoomcharts.com/dvsl/data/net-chart/discovery-net/n" + node.id.split("n")[1] + ".jpg";
        node.label = node.data.title;
    }


}]);

// (function() {
// })();