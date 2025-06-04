from sqlalchemy.orm import Session
from db.model import Note

def create_note(db: Session, content: str):
    db_note = Note(content=content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_note(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()

def get_all_notes(db: Session, limit: int = 100):
    return db.query(Note).limit(limit).all()

def update_note(db: Session, note_id: int, new_content: str):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        db_note.content = new_content
        db.commit()
        db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
    return db_note