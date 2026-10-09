from agents.base_agent import BaseAgent
from agents.prompts import LOCAL_GUIDE_PROMPT
from utils.llm import call_llm


class LocalGuideAgent(BaseAgent):

    def __init__(self):
        super().__init__("Local Guide Agent")

    def run(self, destination):

        self.log_start()

        prompt = LOCAL_GUIDE_PROMPT.format(destination=destination)

        response = call_llm(prompt)

        self.log_end()

        return response
