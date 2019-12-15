import os

from utils.constants import FULL_PATH_ENV_FILE, FULL_PATH_ENV_FILE_TEMPLATE


def check_exist_env_file():
    """
    Check exist .env file
    :return: bool (True/False)
    """
    return os.path.isfile(FULL_PATH_ENV_FILE)


def parse():
    parse_result = {}

    with open(FULL_PATH_ENV_FILE_TEMPLATE) as env_template_file:
        for line in env_template_file:
            line = line.strip()

            if not line or line.startswith('#') or '=' not in line:
                # Ignore comments and lines without assignment.
                continue

            # Remove whitespaces and quotes:
            env_name, env_value = line.split('=', 1)
            env_name = env_name.strip()
            env_value = env_value.strip().strip('\'"')

            parse_result[env_name] = env_value
    return parse_result


def dump(parse_data, **kwargs):
    parse_data.update(set_options(parse_data, **kwargs))

    with open(FULL_PATH_ENV_FILE, 'w') as env_file:
        for key, value in parse_data.items():
            if value:
                env_file.write(
                    f"{key}={value}\n"
                )


def set_options(result, **kwargs):
    """
    To set custom options from command line
    :param result: dict (env.template) with env variables
    :param kwargs: parameters from command line
    :return: update dict
    """
    for env_key in result:
        result[env_key] = kwargs[env_key.lower()]

    return result
