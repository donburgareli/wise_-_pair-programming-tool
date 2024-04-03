CONFIG_LIST = [
    {
        'model': 'mixtral-8x7b',
        'base_url': 'http://localhost:1337/v1',
        'api_type': 'openai',
        'api_key': 'NULL',
    }
]

global LLM_CONFIG 
LLM_CONFIG = { 
    'timeout': 600, 
    'seed': 42,
    'config_list': CONFIG_LIST,
    'temperature': 0,
}
