from agents.base_agent import BaseAgent
from agents.prompts import DESTINATION_PROMPT
from utils.llm import call_llm


class DestinationAgent(BaseAgent):

    def __init__(self):
        super().__init__("Destination Agent")

    def run(self, destination, days, travel_style):

        self.log_start()

        prompt = DESTINATION_PROMPT.format(
            destination=destination,
            days=days,
            travel_style=travel_style
        )

        response = call_llm(prompt)

        self.log_end()

        return response