class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
        self.prev_state = None
        
    def get_state(self):
        return self.currentState
    
    def set_state(self, state):
        self.currentState = state
        
    
    
    # def enter_state(self):
        # if len(self.main.state_stack) > 1:
            # self.prev_state = self.main.state_stack[-1]
        # self.main.state_stack.append(self)
        # 
        # 
    # def exit_state(self):
        # self.main.state_stack.pop()