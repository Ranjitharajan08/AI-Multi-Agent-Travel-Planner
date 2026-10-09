from agents.base_agent import BaseAgent
from agents.prompts import TRAVEL_ADVISOR_PROMPT
from utils.llm import call_llm


class TravelAdvisorAgent(BaseAgent):

    def __init__(self):
        super().__init__("Travel Advisor Agent")

    def run(self, destination_info, budget_info, itinerary, local_guide):

        self.log_start()

        prompt = TRAVEL_ADVISOR_PROMPT.format(
            destination_info=destination_info,
            budget_info=budget_info,
            itinerary=itinerary,
            local_guide=local_guide
        )

        response = call_llm(prompt)

        self.log_end()

        return response
