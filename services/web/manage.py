from flask.cli import FlaskGroup
from project import app, db, Compound

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("get_compound")
def get_compound():
    usr_input = input("Enter the compound you're searching for: ")
    db.session.add(Compound(usr_input.upper()))
    db.session.commit()

@cli.command("get_db")
def get_db():
    for c in db.session.query(Compound).all():
        print(c)

if __name__ == "__main__":
    cli()
