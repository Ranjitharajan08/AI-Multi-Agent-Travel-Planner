from agents.base_agent import BaseAgent
from agents.prompts import BUDGET_PROMPT
from utils.llm import call_llm


class BudgetAgent(BaseAgent):

    def __init__(self):
        super().__init__("Budget Agent")

    def run(self, destination, budget, days):

        self.log_start()

        prompt = BUDGET_PROMPT.format(
            destination=destination,
            budget=budget,
            days=days
        )

        response = call_llm(prompt)

        self.log_end()

        return response
