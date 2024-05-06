import json

def node_exists(nw_node, json_data):
    if nw_node in json_data['nodes']:
        return True
    
    else:
        return False

def logged_in(username, password):
    with open('.database.json', 'r') as f:
        d = json.load(f)
        node = {"username": username, "password": password}

        if node_exists(node, d):
            return True
        
        else:
            return False

def register(username, password):
    new_node = {
        "username": username,
        "password": password
    }

    with open('.database.json', 'r') as fr:
        json_data = json.load(fr)

    if node_exists(new_node, json_data):
        return False
    
    else:
        json_data["nodes"].append(new_node)

        with open('.database.json', 'w') as fw:
            json.dump(json_data, fw, indent=4)
        
        return True
