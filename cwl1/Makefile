extract_tool:
	cwltool extract_tool.json inputs/input1.json
	echo "Output should be located at:  json_out.txt"

upper_tool:
	cwltool upper_tool.json inputs/input2.json
	echo "Output should be located at:  upper.txt"

workflow:
	cwltool workflow.json inputs/input1.json
	echo "Output should be located at:  upper.txt"

subdirs:
	cwltool subdirs.json inputs/input3.json
	echo "Output should be located in directory:  out"	

scatter:
	cwltool workflow_scatter.json inputs/input4.json
	echo "Output should be located in directory:  out"			

validate:
	cwltool --validate extract_tool.json
	cwltool --validate upper_tool.json
	cwltool --validate workflow.json
	cwltool --validate subdirs.json
	cwltool --validate workflow_scatter.json

pack:
	cwlpack workflow.json --json > workflow_complete.json
	cwlpack workflow.json > workflow_complete.cwl

clean:
	rm -rf *.txt
	rm -rf out/
	rm workflow_complete.cwl
	rm workflow_complete.json
