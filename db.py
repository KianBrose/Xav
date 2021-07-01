import sqlite3
import os


_keys = ('id', 'name', 'roles', 'karma')

def _request(command: str, parameters=()) -> str:
    """
    Execute a SQL request and returns the output
    :param command: the sql command
    :param parameters: the sql parameters (HAS TO BE A LIST OF STR)
    """
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()
    output = cursor.execute(command, parameters).fetchall()

    conn.commit()
    conn.close()
    return output


def init():
    with open("database.sqlite", "w") as db:
        pass # Just checking if the database exists

    _request("CREATE TABLE Users (id, name, roles, karma)")


def add_member(member_id: int, member_name: str, member_roles_id: list) -> bool:
    """
    Add a member to the database
    :param member_id: the id of the member
    :param member_name: the name (not the nickname) of the member
    :param member_roles_id: the lists of the roles id the member currently has
    :return: if the member is registered correctly
    """
    roles = "-".join(list(map(lambda el: str(el), member_roles_id)))
    try:
        _request("INSERT INTO Users VALUES (?, ?, ?, 0)", (member_id, member_name, roles))
        return True
    except sqlite3.Error as err:
        print(err)
        return False


def get_member(member_id: int) -> dict:
    """
    Extract data of a specific member
    :param member_id: the id of the targeted member
    :return: a dict containing "id", "name", "roles", "karma"
    """
    try:
        member_info = _request("SELECT * FROM Users WHERE id = ?", (member_id,))[0]
    except IndexError:  # if no member exists, we return None
        return None
    
    member_data = {}
    for key, value in zip(_keys, member_info):  # using zip to flex 
        member_data[key] = value
    
    member_data['roles'] = member_data['roles'].split("-")
    
    return member_data


def update_member_karma(member_id: int, add_value: int) -> bool:
    """
    Add value to the current amount of karma a member has
    :param member_id: the id of the member
    :param add_value: the value to add_member
    :return: if it succeed or not
    """

    if (member_data := get_member(member_id)) is None:
        return False
    
    if add_value == 0:
        return True

    current_level = int(member_data["karma"])
    next_level = current_level + add_value

    _request("UPDATE Users SET 'karma' = ? WHERE id = ?", (next_level, member_id))
    return True


def update_member_roles(member_id: int, new_role_id: int) -> bool:
    """
    Add role to a member
    new_role_id = None will do nothing
    :param member_id: the id of the member
    :param new_role_id: the id of the role to add
    :return: if it succeed or not
    """
    if (member_data := get_member(member_id)) is None:
        return False
    
    if new_role_id is None:
        return True

    roles = member_data["roles"]
    _request("UPDATE Users SET 'roles' = ? WHERE id = ?", (f"{roles}-{new_role_id}", member_id))
    return True


def update_member_name(member_id: int, new_name: str) -> bool:
    """
    Update the name of a member if new_name is None, nothing will change
    :param member_id: the id of the member
    :param new_name: the name
    :return: if it succeed or not
    """
    if (member_data := get_member(member_id)) is None:
        return False
    
    if new_name is None:
        return True

    _request("UPDATE Users SET 'name' = ? WHERE id = ?", (new_name, member_id))
    return True

