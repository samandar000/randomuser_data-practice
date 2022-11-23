def get_all_nats(data: dict) -> list[str]:
    '''get all nats from users data
    
    Args:
        data (dict): users data.
        
    Returns:
        list: list of nats.
    '''
    nats=[]
    nats_data=data['results']
    for s in nats_data:
        nats.append(s['nat'])
    return nats
