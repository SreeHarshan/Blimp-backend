from db.database import SessionLocal
from db.crud import create_note, get_all_notes, update_note, delete_note
from flask import Blueprint,request

notes_blueprint = Blueprint('notes', __name__)

@notes_blueprint.route("/getall",methods=["GET"])
def getall():
    db = SessionLocal()
    try:
        all_notes = get_all_notes(db)
        print(all_notes)
        return {"Value":[note.to_dict() for note in all_notes]}
    except Exception as e:
        return {"Value":[]} 
    finally:
        db.close()
    
    return {"Value":[]}


@notes_blueprint.route("/add",methods=["POST"])
def add():
    note = request.form['note']
    if(not note):
        return {"Value": "Missing ID", "ID": -1}, 400
    db = SessionLocal()
    try:
        new_note = create_note(db, note)
        db.commit()  
        return {"Value":"Success","ID":new_note.id}
    except Exception as e:
        db.rollback() 
        return {"Value":"Database error","ID":-1}, 500
    finally:
        db.close()
        
    return {"Value":"Failed","ID":-1}

@notes_blueprint.route("/delete", methods=["POST"])
def delete():
    note_id = request.form.get('id')
    
    if not note_id:
        return {"Value": "Missing ID", "ID": -1}, 400
    
    try:
        note_id = int(note_id)
    except ValueError:
        return {"Value": "Invalid ID format", "ID": note_id}, 400

    db = SessionLocal()
    try:
        note = delete_note(db,note_id)
        
        db.commit()
        return {"Value": "Success", "ID": note_id}
    
    except Exception as e:
        db.rollback()
        print(e)
        return {"Value": "Database error", "ID": note_id}, 500
    
    finally:
        db.close()
        
@notes_blueprint.route("/update", methods=["POST"])
def update():
    note_id = request.form.get('id')
    new_content = request.form.get('content', '').strip()
    
    if not note_id:
        return {"Value": "Missing ID", "ID": -1}, 400
        
    if not new_content:
        return {"Value": "Empty content", "ID": note_id}, 400
        
    if len(new_content) > 350:
        return {"Value": "Content too long", "ID": note_id}, 400

    try:
        note_id = int(note_id)
    except ValueError:
        return {"Value": "Invalid ID format", "ID": note_id}, 400

    db = SessionLocal()
    try:
        existing_note = update_note(db,note_id,new_content)
        db.commit()
        db.refresh(existing_note)
        return {"Value": "Success", "ID": note_id}
    
    except Exception as e:
        db.rollback()
        print(e)
        return {"Value": "Database error", "ID": note_id}, 500
    
    finally:
        db.close()