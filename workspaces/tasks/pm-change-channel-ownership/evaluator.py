
from typing import List

from scoring import Result, Checkpoint, bonus_for_completing_final
from common import create_rocketchat_client, grader

# Create RocketChat instance
rocket = create_rocketchat_client()

@grader
def grade_checkpoint1(trajectory):
    return f"home" in trajectory

@grader
def grade_checkpoint2(trajectory):
    return f"channel/general" in trajectory

@grader
def check_user_role(username, role):
    roles = rocket.roles_get_users_in_role(role).json()
    users_list = roles.get("users", [])
    return any(user['username'] == username for user in users_list)


def grade_checkpoints(trajectory=""):
    checkpoints: List[Checkpoint] = []
    result = Result(checkpoints, bonus_for_completing_final)

    checkpoints.append(Checkpoint(1, int(grade_checkpoint1(trajectory))))

    checkpoints.append(Checkpoint(1, int(grade_checkpoint2(trajectory))))

    checkpoints.append(Checkpoint(1, int(check_user_role("theagentcompany", "owner"))))

    return result


