from agents.base_agent import BaseAgent
from agents.prompts import ITINERARY_PROMPT
from utils.llm import call_llm


class ItineraryAgent(BaseAgent):

    def __init__(self):
        super().__init__("Itinerary Agent")

    def run(self, destination_info, budget_info, days):

        self.log_start()

        prompt = ITINERARY_PROMPT.format(
            destination_info=destination_info,
            budget_info=budget_info,
            days=days
        )

        response = call_llm(prompt)

        self.log_end()

        return response