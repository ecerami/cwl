import json
import sys

# This is a toy Python script that reads in a JSON file,
# extracts a specific JSON Element, and then writes the
# text of that element to a json_out.txt file.
file_name = sys.argv[1]
json_element = sys.argv[2]
f = open(file_name)
  
data = json.load(f)
product = data[json_element]

out_fd = open("json_out.txt", "w")
out_fd.write(product + "\n")

f.close()
out_fd.close()