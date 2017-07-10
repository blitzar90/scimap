(function() {
	console.log('hello index script');

	$.ajax({
		method : 'GET',
		url : '/nodes',
		success : (data) => {
			console.log(data);
		}, 
		error : (error) => {
			console.log(error);
		}
	})
})();