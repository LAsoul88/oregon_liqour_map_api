from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={"autoflush": False})

def initialize_db(app):
  app.app_context().push()
  db.init_app(app)
  db.create_all()
