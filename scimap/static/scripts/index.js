angular.module('scimap', ['ngSanitize', 'ui.select']).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[').endSymbol(']}');
})
.controller('Main', ['$scope', '$http', function(scope, http) {
	console.log('hello');

	scope.nodes = [];

	var linkCounter = 0;
	var colorMap = {};
	var ALLNODES = {};
	var ALLLINKS = {};
	var currentGraph = null;
	var currentGraphData = {};

	scope.init = function() {
		getNodes();
	}

	scope.onSelect = function(item, model) {
		console.log(item, model);

		if (model.type == 'node') {
			getNode(model.id); 
		} else {
			getRoute(model.id);
		}

		currentGraphData = {};

	}

	function getNode(id) {
		http.post('/api/nodes/', { ids : [id], full: true }, {
			headers : { 'X-CSRFToken' : csrfmiddlewaretoken }
		}).then(response => {
			console.log(response.data);

			var data = [];
			var node = response.data[0];
			node.focus = true;

			for (let _node of node.toNodes.concat(node.fromNodes)) {
				data.push(_node);
			}

			node.toNodes = node.toNodes.map(el => el.id);
			node.fromNodes = node.fromNodes.map(el => el.id);

			data.push(node);

			makeChart(prepareData(data));

		}, error => {
			console.log(error);
		});
	}

	function getRoute(id) {
		http.get('/api/route/' + id, {
			headers : { 'X-CSRFToken' : csrfmiddlewaretoken }
		}).then(response => {
			console.log(response.data);

			data = response.data.nodes;

			makeChart(prepareData(data));
		}, error => {
			console.log(error);
		});	
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

	function ChartLink(from, to, primaryKey) {
		this.primaryKey = primaryKey;
		this.id = linkCounter++;
		this.from = from;
		this.to = to;
		this.style = {
			toDecoration : 'arrow',
			radius : 3,
			fillColor : '#444'
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
				fillColor : colorMap[data.area[0].id],
				aura : data.area.map(el => {
					// return {
					// 	id : el.id,
					// 	style : {
					// 		showInLegend : true,
					// 		legendGroupId : el.id
					// 	}
					// }
					return el.title;
				})
			}
			this.extra = data;
		}

		this.transform = () => {
			return new ChartNode(this);
		}
	}

	function prepareData(nodes) {

		console.log(nodes);

		nodes = nodes.map(el => new Node(el));

		for (let node of nodes) {
			ALLNODES[node.id] = node;
		}

		_obj = {};
		links = [];

		for (let node1 of nodes) {
			if (node1.toNodes) {
				for (node1_out_id of node1.toNodes) {
					let str = node1.id + '::' + node1_out_id;
					_obj[str] = true;
				}
			}
			if (node1.fromNodes) {
				for (node1_in_id of node1.fromNodes) {
					let str = node1_in_id + '::' + node1.id;
					_obj[str] = true;
				}
			}
		}

		for (let key in _obj) {

			let exactLinks = [];


			if (currentGraphData.links) {
				exactLinks = currentGraphData.links.map(el => el.primaryKey);
			}

			if (exactLinks.indexOf(key) == -1) {
				let split = key.split('::');
				let newLink = new ChartLink(split[0], split[1], key);
				links.push(newLink);

				console.log('add');
			} else {
				console.log('not add');
			}
		}

		makeColorMap(nodes);

		console.log(nodes, links);

		return {
			nodes : nodes.map(el => el.transform()), links
		}
	}

	function makeChart(data) {

		currentGraphData = data;

		let focusNode = data.nodes.filter(el => el.extra.focus)[0];

		let navigation;
		if (focusNode) {
			navigation = {
	        	initialNodes : [focusNode.id],
	        	mode : 'focusnodes',
	        	focusNodeExpansionRadius : 1
			}
		} else {
			navigation = {};
		}


		console.log('makeChart', data, data.nodes[0].id, navigation);

		currentGraph = new NetChart({
	        container: document.getElementById("demo"),
	        area: { height: $('body').height() - 5 },
	        data : {
				preloaded : data
	        },
	        navigation,
	        auras: { 
	        	overlap: true
	        },
	        legend : {
	        	enabled : true
	        },
	        events : {
		        onClick: function (event) {
	                if (event.clickNode) {
	                	console.log(event.clickNode.data);

	                	let exclude = currentGraph.nodes().map(el => el.data.extra.id);

	                	console.log(exclude);

	                	let nodes = $(event.clickNode.data.extra.toNodes.concat(event.clickNode.data.extra.fromNodes))
	                		.not($(exclude)).get();

	                	nodes = nodes.map(el => ALLNODES[el]);

	                	let preparedData = prepareData(nodes);

	                	console.log(preparedData);

	                	currentGraph.addData(preparedData);

	                	currentGraphData.nodes = currentGraphData.nodes.concat(preparedData.nodes);
	                	currentGraphData.links = currentGraphData.links.concat(preparedData.links);

	                	console.log(currentGraphData);
	                }
	            }
	        }

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
			if (node.area) {
				for (let key of node.area) {
					colorMap[key.id] = colorMap[key.id] || true;
				}
			}
		}

		for (key in colorMap) {
			if (colorMap[key] == true) {
				colorMap[key] = getRandomColor();
			}
		}

		console.log(colorMap);
	}



    function nodeStyle(node){
        node.image = "https://zoomcharts.com/dvsl/data/net-chart/discovery-net/n" + node.id.split("n")[1] + ".jpg";
        node.label = node.data.title;
    }


}]);