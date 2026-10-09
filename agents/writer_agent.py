from agents.base_agent import BaseAgent
from agents.prompts import WRITER_PROMPT
from utils.llm import call_llm

class WriterAgent(BaseAgent):

    def __init__(self):
        super().__init__("Writer Agent")

    def run(self, outline):
        self.log_start()

        prompt = WRITER_PROMPT.format(outline=outline)

        response = call_llm(prompt)

        self.log_end()

        return response