from agents import Developer, DocumentationSpecialist, UserProxy, TeamLead, QAEngineer
import autogen
from config import settings

if __name__ == '__main__':

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
            speaker_selection_method='round_robin'
        )
        manager = autogen.GroupChatManager(groupchat=workgroup, llm_config=settings.llm_config)

        UserProxy._AGENT.initiate_chat(
            manager,

            message=task
        )