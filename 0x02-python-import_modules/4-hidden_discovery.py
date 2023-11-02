#!/usr/bin/python3
import dis
if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        bytecode = file.read()
        instructions = dis.get_instructions(bytecode)
        names = set()
        for instr in instructions:
            if instr.opname == "LOAD_CONST":
                const = instr.argval
                if isinstance(const, str) and not const.startswith("__"):
                    names.add(const)
        for name in sorted(names):
            print(name)
