from autogen import UserProxyAgent
from config.settings import LLM_CONFIG 

_AGENT = UserProxyAgent(
    name='Q.A Engineer',
    human_input_mode='NEVER',
    llm_config=LLM_CONFIG,
    description="Q.A Engineer of the Development Team",
    system_message="""
    
    Given the previously generated codes from Developer, you will write the tests for the project

    Do not write code as following

    ```python
    code
    ```

    make sure to always include the command to put it inside a file

    ```bash
    echo "code" >> file
    ```

    Report to Client to execute the markdown blocks.
    """
)