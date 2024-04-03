#from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen import UserProxyAgent
from config import settings 

_AGENT = UserProxyAgent(
    name='Client',
    
    code_execution_config={
        'work_dir':'generated',
        'use_docker': "ubuntu",
        'timeout': 120,
        'last_n_messages': 1
        },
    llm_config=settings.LLM_CONFIG,
    system_message="""

    Uppon receiving markdown codeblocks, execute it then report back to the previous agent or the informed agent on
    "Reporting to ..." message.
    """
)