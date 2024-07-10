from integration_template.configurations.environment import Environment


class Configuration:

    @classmethod
    def start_url(cls):
        return Environment.current_environment().get("https://userinyerface.com/")

    @classmethod
    def api_url(cls):
        return Environment.current_environment().get("apiUrl")

