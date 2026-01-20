


def is_registered(registered: bool) -> bool:

    #Check if the student is registered online.

    #param registered: True if student is registered, False otherwise
    #return: Boolean result

    if registered:
        return True
    else:
        return False


def has_medical_clearance(cleared: bool) -> bool:

    #Check if the student has medical clearance.

    #param cleared: True if student has medical clearance, False otherwise
    #return: Boolean result

    if cleared:
        return True
    else:
        return False


def is_valid_grade(grade: int) -> bool:

    #Check if the student is in Grades 7 to 10.

    #param grade: Student grade level
    #return: True if grade is between 7 and 10, False otherwise

    if 7 <= grade <= 10:
        return True
    else:
        return False


def assign_team(section: str) -> str:

    #Assign Intramurals team based on section.

    #Section-Team Mapping:
    #Emerald   -> Red Bulldogs
    #Ruby      -> Yellow Tigers
    #Topaz     -> Green Hornets
    #sSapphire  -> Blue Bears

    #param section: Student section
    #return: Assigned team

    section = section.lower()

    if section == "emerald":
        return "Red Bulldogs"
    elif section == "ruby":
        return "Yellow Tigers"
    elif section == "topaz":
        return "Green Hornets"
    elif section == "sapphire":
        return "Blue Bears"
    else:
        return "No Team Assigned"


def check_eligibility(registered: bool, cleared: bool, grade: int, section: str) -> dict:

    #Main function that determines eligibility and assigns team.

    #param registered: Online registration status
    #param cleared: Medical clearance status
    #param grade: Grade level
    #param section: Section name
    #return: Dictionary containing eligibility result and message

    if not is_registered(registered):
        return {
            "eligible": False,
            "message": "You must register online before joining the Intramurals."
        }

    if not has_medical_clearance(cleared):
        return {
            "eligible": False,
            "message": "You must secure a medical clearance from the clinic."
        }

    if not is_valid_grade(grade):
        return {
            "eligible": False,
            "message": "Only students from Grades 7 to 10 are allowed to join."
        }

    team = assign_team(section)

    return {
        "eligible": True,
        "message": "Congratulations! You are eligible to join the Intramurals!",
        "team": team
    }


if __name__ == "__main__":
    app.run(debug=True)

