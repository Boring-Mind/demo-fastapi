from sqlalchemy.orm import Session
from db.models.member import Member
from db.models.team import Team

class TeamDAL:
    def __init__(self, session: Session):
        self.session = session

    #return a list of team sorted by average age of their members
    def get_teams_by_average_age(self):
        return self.session.query(Team).order_by(Member.average_age).all()

    

