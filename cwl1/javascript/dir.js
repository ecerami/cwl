// Create Directories
function createDirectories (inputs) {
	var dirs = [];
	for (var i=0; i< inputs.json.length; i++) {
		var dir = {
			"class": "Directory",
			"basename": "out/" + inputs.json[i].nameroot,
			"listing": [inputs.json[i], inputs.text_out[i]]
		}
		console.log(inputs);
		dirs.push(dir);
	} 
	return {"dirs": dirs};
}