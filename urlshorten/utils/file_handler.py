import json
import os
# get the data from the file and check if the code is already present or not.

def check_code(code, value, file_name):
    '''
    code: str 
    value: str
    file_name: str
    
    returns -> Tuple(bool,str)
    
    checks if the short name (code) is already mapped with other url or not. 
    
    '''
    urls = {}
    if os.path.exists(file_name):
        with open(file_name, 'r') as file_input:
            urls = json.load(file_input)
            if code in urls.keys():
                return False, ""
    urls[code] = {'url': value}
    with open(file_name, 'w') as file_output:
        json.dump(urls, file_output)
    return True, f'http://localhost:5000/{code}'


def get_url(code, file_name):
    '''
    code: str
    file_name: str

    returns -> Tuple(bool,str)

    returns the real url corresponding to the code provided 
    '''
    if os.path.exists(file_name):
        with open(file_name, 'r') as file_input:
            urls = json.load(file_input)
            if code in urls.keys():
                return True, urls[code]['url']
            return False, "No Such Code"
    return False, "Zero Records"
