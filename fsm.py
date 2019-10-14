class State:
    def __init__(self, name, events, default_event='ERROR'):
        self.name = name
        self.events = events
        self.default_event = default_event

    def apply(self, event):
        return self.events.get(event, self.default_event)


class FSM:
    def __init__(self, states, start):
        self.states = {s.name: s for s in states}
        self.start_state = self.states[start]

    def get_state_by_events(self, lst):
        state = self.start_state
        for event in lst:
            next = state.apply(event)
            state = self.states[next]
        return state.name
