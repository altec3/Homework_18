from project.setup.app_init import app_init
from project.setup.app_configure import configure_app
from project.setup.config import Config

app_config = Config()

app = app_init(app_config)
configure_app(app)


if __name__ == "__main__":
    app.run()
