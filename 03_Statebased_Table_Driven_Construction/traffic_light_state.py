from enum import Enum
import time

# Automata => State
class TrafficLightState(Enum):
    MERAH = "merah"
    HIJAU = "hijau"
    KUNING = "kuning"

# Automata => State atau perubahan atau Transisi
state_transition = {
    TrafficLightState.MERAH: TrafficLightState.HIJAU,
    TrafficLightState.HIJAU: TrafficLightState.KUNING,
    TrafficLightState.KUNING: TrafficLightState.MERAH
}

state_durations = {
    TrafficLightState.MERAH: 6,
    TrafficLightState.HIJAU: 4,
    TrafficLightState.KUNING: 1
}

current_state = TrafficLightState.MERAH
while True:
    print(f"Traffic Light: {current_state.value}")
    time.sleep(state_durations[current_state])
    current_state = state_transition[current_state]
# next_state = state_transition[current_state]
# print(next_state.value) 


