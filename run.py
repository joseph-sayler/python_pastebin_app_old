from app import create_app, db
from config import Database_config

app = create_app()

if Database_config.DATABASE_TYPE == "SQLITE":
    from app.models import SQL_Pastes as Pastes

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'Pastes': Pastes}
