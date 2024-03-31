config_list = [
    {
        'model': 'mixtral-8x7b',
        'base_url': 'http://localhost:1337/v1',
        'api_type': 'openai',
        'api_key': 'NULL',
    }
]

global llm_config 
llm_config = { 
    'timeout': 600, 
    'seed': 42,
    'config_list': config_list,
    'temperature': 0
}   