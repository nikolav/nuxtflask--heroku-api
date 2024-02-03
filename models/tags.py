from typing import List

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from . import tagsTable
from . import db
from . import ln_docs_tags


class Tags(db.Model):
  __tablename__ = tagsTable

  id:  Mapped[int] = mapped_column(primary_key = True)
  tag: Mapped[str] = mapped_column(unique = True)

  # virtual
  docs: Mapped[List['Docs']] = relationship(secondary      = ln_docs_tags, 
                                            back_populates = 'tags')

  # magic
  def __repr__(self):
    return f'Tags(id={self.id!r}, data={self.tag!r})'
  
  @staticmethod
  def by_name(tag_name, *, create = False):
    tag = db.session.scalar(
      db.select(Tags)
        .where(Tags.tag == tag_name)
    )

    if (not tag) and (True == create):
      tag = Tags(tag = tag_name)
      db.session.add(tag)
      db.session.commit()
    
    return tag
