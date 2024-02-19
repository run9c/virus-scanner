import sys
import hashlib
import json
from virus_total_apis import PublicApi as public_api

# Determine the total number of arguments provided
number_of_arguments = len(sys.argv)

# Function to read files
def read_file(file_name):
    file = open(file_name, "rb")
    output = file.read()
    file.close()
    return output

# Check if the number of arguments is valid
if number_of_arguments == 1 or number_of_arguments > 2:
    print("[-] Invalid Syntax")
    print("Syntax: ./virus_total.py <file_name>")
else:
    # Replace "<your_api_key_here>" with your actual VirusTotal API key
    api_key = "your-api-key"
    
    # Read the content of the file
    file_content = read_file(sys.argv[1])
    
    # Calculate MD5 hash of the file content
    md5_hash = hashlib.md5()
    md5_hash.update(file_content)
    md5_digest = md5_hash.hexdigest()

    # Initialize VirusTotal API object
    vt = public_api(api_key)
    
    # Retrieve file report from VirusTotal
    response = vt.get_file_report(md5_digest)
    
    # Print the response in JSON format with proper indentation
    print(json.dumps(response, sort_keys=False, indent=4))
