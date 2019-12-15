import configparser
import os


SMTP_SERVER = "smtp_server"
PORT = "port"
SENDER_EMAIL = "sender_email"
SENDER_PASSWORD = "sender_password"
RECEIVER_EMAIL = "receiver_email"


SECTION_SETTINGS = "Settings"

base_path = os.path.dirname(os.path.realpath(__file__))
PATH = os.path.join(base_path, 'settings.ini')


def create_config(path=PATH):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "access_token", "")

    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path=PATH):
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(section, setting, path=PATH):
    config = get_config(path)
    value = config.get(section, setting)
    print
    "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value
    )
    return value


def update_setting(section, setting, value, path=PATH):
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)


def delete_setting(section, setting, path=PATH):
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)


def main():
    path = "settings-test.ini"
    update_setting("Settings", "test", "a", path)
    get_setting("Settings", "test", path)
    update_setting("Settings", "test", "a", path)
    delete_setting("Settings", "test", path)


if __name__ == "__main__":
    main()