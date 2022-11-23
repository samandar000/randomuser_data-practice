import json

def read_data(file_path: str) -> dict:
    '''read data from a file
    
    Args: 
        file_path (str): file path
        
    Returns:
        dict: dict data from file
    '''
    # open file 
    data_str = open(file_path).read()
    # convert json to dict
    data_dict = json.loads(data_str)
    return data_dict