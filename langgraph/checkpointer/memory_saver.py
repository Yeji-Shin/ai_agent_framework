from langgraph.checkpoint.memory import MemorySaver

class ConditionalMemorySaver(MemorySaver):
    def __init__(self, condition_func):
        super().__init__()
        self.condition_func = condition_func

    def put(self, config, metadata, values):
        if self.condition_func(values):
            super().put(config, metadata, values)
