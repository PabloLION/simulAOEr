## Goal

- Simulator of AOE2:DE build for multiple players.
- Implement some algorithm to see the best strategy for each civ / civ group strategy.
  - Like what's the best civ combination for 2/3/4 players.
  - What's the best strategy for civ-s vs civ-s.
  - What's the best play style for certain civ-s on a certain map.
  - Maybe use AI, but need metrics (hard to evaluate).
  - Maybe more simulation for battle field simulation.

## Docs

- Design Docs
- How to use
- How to contribute
- CLI/API
- Tech Stack

### Design Docs

Classes:

- Map
  - Wood line distance
  - Gold pile distance
- Player
  - Resources
  - Technology (of class TechTree)
  - Civ (of class civ)
  - Bonus (from team)
- Civ
  - Civ Bonus
  - Tech Tree (of class TechTree)
- Tech Tree
  - Unit/tech availability (also add a researched for user)
- Build Order
  - Steps
  - Steps with text
  - Goal

### stack

- We are using Python / Flask now.

### CLI and API

- Current mature projects from [Siege Engineers](https://siegeengineers.org/projects)
- aoe2map.net for map scripts
- recs for training AI
- data mods [SiegeEngineers/auto-mods](https://github.com/SiegeEngineers/auto-mods)
- tech data [SiegeEngineers/halfon](https://github.com/SiegeEngineers/halfon/)
- more simulation with [openage](https://blog.openage.dev/), [repo](https://github.com/SFTtech/openage) or [CaptureAge](https://captureage.com/) for metrics for AI.
