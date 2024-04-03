from agents import Developer, DocumentationSpecialist, UserProxy, TeamLead, QAEngineer
from autogen import GroupChat, GroupChatManager
from autogen.graph_utils import visualize_speaker_transitions_dict
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

        workgroup = GroupChat(
            agents=[
                UserProxy._AGENT,
                TeamLead._AGENT,
                Developer._AGENT,
                QAEngineer._AGENT,
                DocumentationSpecialist._AGENT
            ],
            messages=[],
            max_round=12,
            allowed_or_disallowed_speaker_transitions= {
                UserProxy._AGENT: [TeamLead._AGENT, Developer._AGENT, QAEngineer._AGENT, DocumentationSpecialist._AGENT],
                TeamLead._AGENT: [UserProxy._AGENT, TeamLead._AGENT, Developer._AGENT, QAEngineer._AGENT, DocumentationSpecialist._AGENT],
                Developer._AGENT: [UserProxy._AGENT, Developer._AGENT, QAEngineer._AGENT],
                QAEngineer._AGENT: [UserProxy._AGENT, QAEngineer._AGENT, Developer._AGENT, DocumentationSpecialist._AGENT],
                DocumentationSpecialist._AGENT: [UserProxy._AGENT, DocumentationSpecialist._AGENT, TeamLead._AGENT]
            },
            speaker_transitions_type='allowed',
        )

        if(development_mode):
            visualize_speaker_transitions_dict(workgroup.allowed_or_disallowed_speaker_transitions, workgroup.agents)

        manager = GroupChatManager(
            groupchat=workgroup,
            llm_config=settings.LLM_CONFIG,
            system_message="""
            Send the task for the agent who was nominated called by someone, except in the first call
            Follow the below rules while delegating
            
            1. the Team_Lead will always be the first agent to speak, no matter what
            2. If a agent says "Reporting to [_AGENT] where [_AGENT] is the name of one agent, then this agent is the next one
            3. If no "Reporting to [_AGENT]" is present on the message, then let the current speaking agent continue.
            """
        )

        UserProxy._AGENT.initiate_chat(
            manager,
            message= task,            
        )