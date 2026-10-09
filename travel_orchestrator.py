from agents.destination_agent import DestinationAgent
from agents.budget_agent import BudgetAgent
from agents.itinerary_agent import ItineraryAgent
from agents.local_guide_agent import LocalGuideAgent
from agents.travel_advisor_agent import TravelAdvisorAgent

from utils.file_handler import save_output
from export_utils import export_travel_plan


def run_travel_pipeline(destination, budget, days, travel_style):

    destination_agent = DestinationAgent()
    budget_agent = BudgetAgent()
    itinerary_agent = ItineraryAgent()
    local_guide_agent = LocalGuideAgent()
    travel_advisor_agent = TravelAdvisorAgent()

    # ---------------- STEP 1: DESTINATION ----------------
    destination_info = destination_agent.run(
        destination,
        days,
        travel_style
    )
    save_output("destination.md", destination_info)

    # ---------------- STEP 2: BUDGET ----------------
    budget_info = budget_agent.run(
        destination,
        budget,
        days
    )
    save_output("budget.md", budget_info)

    # ---------------- STEP 3: ITINERARY ----------------
    itinerary = itinerary_agent.run(
        destination_info,
        budget_info,
        days
    )
    save_output("itinerary.md", itinerary)

    # ---------------- STEP 4: LOCAL GUIDE ----------------
    local_guide = local_guide_agent.run(destination)
    save_output("local_guide.md", local_guide)

    # ---------------- STEP 5: FINAL PLAN ----------------
    final_plan = travel_advisor_agent.run(
        destination_info,
        budget_info,
        itinerary,
        local_guide
    )
    save_output("final_travel_plan.md", final_plan)

    return {
        "destination_info": destination_info,
        "budget_info": budget_info,
        "itinerary": itinerary,
        "local_guide": local_guide,
        "final_plan": final_plan
    }


# ---------------- EXPORT FUNCTION ----------------
def generate_and_export(final_plan):
    return export_travel_plan(final_plan)