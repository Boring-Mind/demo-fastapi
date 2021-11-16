from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from db.models.member import Member

class MemberDAL:
    def __init__(self, session: Session):
        self.session = session

    async def create_member(self, member: Member) -> Member:
        self.session.add(member)
        self.session.commit()
        return member

    async def get_member_by_id(self, member_id: int) -> Optional[Member]:
        return self.session.query(Member).filter(Member.id == member_id).first()

    async def update_member_by_id(self, member_id: int, member: Member) -> Member:
        self.session.query(Member).filter(Member.id == member_id).update(member)
        self.session.commit()
        return member
    
    async def delete_member_by_id(self, member_id: int) -> Member:
        member = self.session.query(Member).filter(Member.id == member_id).first()
        self.session.delete(member)
        self.session.commit()
        return member