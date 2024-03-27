from autogen import UserProxyAgent
from config.settings import llm_config 

_AGENT = UserProxyAgent(
    name='Client',
    
    code_execution_config={
        'work_dir':'generated',
        'use_docker': True,
        'timeout': 120,
        'last_n_messages': 1
        },
    llm_config=llm_config,
)