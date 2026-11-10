
class TuringMachine:

    def __init__(self, tape, transitions, start_state, halt_state):
        self.tape = {}
        for i, symbol in enumerate(tape):
            self.tape[i] = symbol

        self.head = 0
        self.state = start_state
        self.transitions = transitions
        self.halt_state = halt_state

    def read_symbol(self):
        return self.tape.get(self.head, "_")

    def step(self):
        symbol = self.read_symbol()
        key = (self.state, symbol)

        if key not in self.transitions:
            return False

        new_state, write_symbol, move = self.transitions[key]

        self.tape[self.head] = write_symbol
        self.state = new_state

        if move == "R":
            self.head += 1
        elif move == "L":
            self.head -= 1

        return True

    def run(self, max_steps=1000):
        visited = set()

        for step_number in range(max_steps + 1):

            if self.state == self.halt_state:
                return "HALTED", step_number

            configuration = (
                self.state,
                self.head,
                tuple(sorted(self.tape.items()))
            )

            if configuration in visited:
                return "POSSIBLE INFINITE LOOP", step_number

            visited.add(configuration)

            if step_number == max_steps:
                return "STEP LIMIT REACHED", step_number

            if not self.step():
                return "HALTED (NO TRANSITION)", step_number

        return "STEP LIMIT REACHED", max_steps


# Example Turing Machine
if __name__ == "__main__":

    transitions = {
        ("q0", "1"): ("q0", "1", "R"),
        ("q0", "_"): ("qhalt", "_", "S")
    }

    machine = TuringMachine(
        tape="111",
        transitions=transitions,
        start_state="q0",
        halt_state="qhalt"
    )

    result, steps = machine.run()

    print("TURING MACHINE SIMULATION")
    print("-------------------------")
    print("Result:", result)
    print("Steps:", steps)
