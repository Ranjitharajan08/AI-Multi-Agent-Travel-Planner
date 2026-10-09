from abc import ABC, abstractmethod

class BaseAgent(ABC):

    def __init__(self, name):
        self.name = name

    def log_start(self):
        print(f"🚀 {self.name} Started")

    def log_end(self):
        print(f"✅ {self.name} Finished")

    @abstractmethod
    def run(self, input_text):
        pass