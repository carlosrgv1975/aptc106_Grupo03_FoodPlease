from ..extensions import db


class BaseRepository:
    model = None

    def get_all(self):
        return self.model.query.order_by(self.model.id.desc()).all()

    def get_by_id(self, entity_id: int):
        return self.model.query.get_or_404(entity_id)

    def create(self, **kwargs):
        entity = self.model(**kwargs)
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, entity, **kwargs):
        for key, value in kwargs.items():
            setattr(entity, key, value)
        db.session.commit()
        return entity

    def delete(self, entity):
        db.session.delete(entity)
        db.session.commit()
