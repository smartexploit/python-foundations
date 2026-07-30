"""Skill Matrix & Team Matcher
Demonstrates Sets, Set Operations (union, intersection, difference, symmetric_difference).
"""

from typing import Dict, Set

# Type alias
SkillSet = Set[str]
TeamRoster = Dict[str, SkillSet]


def analyze_skill_overlap(person1: str, skills1: SkillSet, person2: str, skills2: SkillSet) -> None:
    """Demonstrates set operations between two individuals."""
    print(f"\n[ Skill Comparison: {person1} vs {person2} ]")
    
    # Intersection: Shared skills
    shared = skills1 & skills2
    print(f" • Shared Skills (&): {shared if shared else 'None'}")

    # Difference: Unique to person1
    only_p1 = skills1 - skills2
    print(f" • Skills {person1} has but {person2} lacks (-): {only_p1}")

    # Difference: Unique to person2
    only_p2 = skills2 - skills1
    print(f" • Skills {person2} has but {person1} lacks (-): {only_p2}")

    # Symmetric Difference: Skills only one of them has
    unique_either = skills1 ^ skills2
    print(f" • Skills exclusive to either person (^): {unique_either}")


def generate_team_master_skills(roster: TeamRoster) -> SkillSet:
    """Demonstrates Set Union across multiple team members."""
    master_skills: SkillSet = set()
    for member_skills in roster.values():
        master_skills |= member_skills  # In-place union update
    return master_skills


def main():
    # Define team members and their skill sets
    team: TeamRoster = {
        "Alice": {"Python", "Linux", "Git", "SQL"},
        "Bob": {"Python", "Go", "Docker", "Linux"},
        "Charlie": {"JavaScript", "HTML", "CSS", "Python"}
    }

    print("--- Team Skill Roster ---")
    for name, skills in team.items():
        print(f" • {name}: {skills}")

    # Compare Alice and Bob
    analyze_skill_overlap("Alice", team["Alice"], "Bob", team["Bob"])

    # Master list of all skills across team (Union)
    all_skills = generate_team_master_skills(team)
    print("\n--- Master Team Capability List (Union) ---")
    print(f"Total Unique Skills ({len(all_skills)}): {sorted(all_skills)}")


if __name__ == "__main__":
    main()
