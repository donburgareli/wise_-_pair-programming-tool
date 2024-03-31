from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from config.settings import llm_config 

_AGENT = RetrieveUserProxyAgent(
    name='Client',
    
    code_execution_config={
        'work_dir':'generated',
        'use_docker': True,
        'timeout': 120,
        'last_n_messages': 1
        },
    llm_config=llm_config,
)