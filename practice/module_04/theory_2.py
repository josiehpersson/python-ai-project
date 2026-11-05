from dataclasses import dataclass

# an office has agents, the office keeps the agents as an attribute.
# that is called composition.

@dataclass
class EstateAgent:
    name: str
    phone: str


@dataclass
class Office:
    city: str
    agents: list[EstateAgent]


agents = [EstateAgent("Kim", "031-390 06 00"), EstateAgent("Alex", "031-390 06 02")]
office = Office("Gothenburg", agents)

# office.agents is a list of EstateAgent objects. The office uses them and inherits nothing.
for agent in office.agents:
    print(agent.name, agent.phone)

# Output:
# Kim 031-390 06 00
# Alex 031-390 06 02