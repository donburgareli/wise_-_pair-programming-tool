from agents import Developer, DocumentationSpecialist, UserProxy, TeamLead, QAEngineer
import autogen
from config import settings

development_mode = True

if __name__ == '__main__':
    if(development_mode):
        from config.development_mode import delete_folder
        import os

        # Paths to the folders
        cache_folder = '.cache'
        pycache_folder = os.path.join('agents', '__pycache__')
        generated_folder = 'generated'

        print('Development mode active, deleting cache and generated folders\n')

        # Delete the .cache folder
        delete_folder(cache_folder)

        # Delete the __pycache__ folder inside the agents folder
        delete_folder(pycache_folder)

        # Delete the generated folder.
        delete_folder(generated_folder)

    while(True):
        task= input('>> ')

        workgroup = autogen.GroupChat(
            agents=[
                UserProxy._AGENT,
                TeamLead._AGENT,
                Developer._AGENT,
                QAEngineer._AGENT,
                DocumentationSpecialist._AGENT
            ],
            messages=[],
            max_round=12,
            speaker_selection_method='auto'
        )
        manager = autogen.GroupChatManager(
            groupchat=workgroup,
            llm_config=settings.llm_config,
            system_message="""
            Send the task for the agent who was nominated called by someone, except in the first call
            Follow the below rules while delegating
            
            1. the Team_Lead will always be the first, no matter what
            2. If a agent says "Reporting to [_AGENT] where [_AGENT] is the name of one agent, then this agent is the next one
            3. If no "Reporting to [_AGENT]" is present on the message, then let the current speaking agent continue.
            """
        )

        UserProxy._AGENT.initiate_chat(
            manager,

            message=task
        )