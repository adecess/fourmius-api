from fastapi import Depends
from sqlalchemy.orm import Session

from ..config.database import get_db


class DBSessionContext(object):
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db


class AppService(DBSessionContext):
    pass


class AppCRUD(DBSessionContext):
    pass
