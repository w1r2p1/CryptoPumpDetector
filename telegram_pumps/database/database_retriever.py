from common.database.database_connection import obtain_db_connection


def fetch_all_groups(fresh_state_needed):
    groups_list = []

    if fresh_state_needed:
        db_connection = obtain_db_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute('SELECT group_id, signal_type FROM pump_groups')
        groups_list = db_cursor.fetchall()
        db_connection.close()
    else:
        if not all_groups_list:
            groups_list = fetch_all_groups(True)
        else:
            groups_list = all_groups_list

    return groups_list


all_groups_list = fetch_all_groups(True)


def fetch_text_signal_groups():
    pass


def fetch_image_signal_groups():
    pass


def fetch_unknown_signal_type_groups():
    pass