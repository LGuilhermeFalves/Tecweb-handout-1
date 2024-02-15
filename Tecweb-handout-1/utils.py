import json
def extract_route(request):
    first_space_index = request.find(' ')

    second_space_index = request.find(' ', first_space_index + 1)
    
    route = request[first_space_index + 1:second_space_index]
    
    if route.startswith('/'):
        route = route[1:]

    return route

def read_file(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
    return content

def load_data(filename):
    filepath = 'data/' + filename

    with open(filepath, 'r') as file:
        data = json.load(file)

    return data

def load_template(filename):
    filepath = 'templates/' + filename

    with open(filepath, 'r') as file:
        template = file.read()

    return template
