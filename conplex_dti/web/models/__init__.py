import flask

from .base import Model as Model
from .base import db_engine as db_engine
from .base import db_session as db_session

# All models (for imports and Alembic).
from .users import User as User
from .sets import Set as Set
from .sets import DrugSet as DrugSet
from .sets import TargetSet as TargetSet
from .pairings import Pairing as Pairing


def register_models(app: flask.Flask) -> None:
    """
    Register the application's models.
    """

    @app.teardown_appcontext
    def remove_db_session(_=None):
        """
        Remove the database session after a request.
        See https://docs.sqlalchemy.org/en/20/orm/contextual.html.
        """
        db_session.remove()
