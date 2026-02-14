from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from typing import List, Optional
from datetime import date

app = FastAPI(title="Mini Resume Management API")

candidates = []
candidate_id_counter = 1

@app.get("/")
def root():
    return {"message": "Resume Management API is running"}

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/candidates", status_code=201)
def resume_upload(
    full_name: str = Form(...),
    dob: date = Form(...),
    contact_number: str = Form(...),
    contact_address: str = Form(...),
    qualification: str = Form(...),
    graduation_year: int = Form(...),
    experience_years: int = Form(...),
    skills: str = Form(...),
    resume: UploadFile = File(...)
):
    global candidate_id_counter

    candidate = {
        "id": candidate_id_counter,
        "full_name": full_name,
        "dob": dob,
        "contact_number": contact_number,
        "contact_address": contact_address,
        "qualification": qualification,
        "graduation_year": graduation_year,
        "experience_years": experience_years,
        "skills": [skill.strip() for skill in skills.split(",")],
        "resume_filename": resume.filename
    }

    candidates.append(candidate)
    candidate_id_counter += 1

    return {
        "message": "Candidate added successfully",
        "candidate_id": candidate["id"]
    }

@app.get("/candidates")
def list_candidates(
    skill: Optional[str] = None,
    experience: Optional[int] = None,
    graduation_year: Optional[int] = None
):
    result = candidates

    if skill:
        result = [c for c in result if skill in c["skills"]]

    if experience is not None:
        result = [c for c in result if c["experience_years"] >= experience]

    if graduation_year:
        result = [c for c in result if c["graduation_year"] == graduation_year]

    return result

@app.get("/candidates/{candidate_id}")
def get_candidate(candidate_id: int):
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate
    raise HTTPException(status_code=404, detail="Candidate not found")

@app.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: int):
    for index, candidate in enumerate(candidates):
        if candidate["id"] == candidate_id:
            candidates.pop(index)
            return {"message": "Candidate deleted successfully"}
    raise HTTPException(status_code=404, detail="Candidate not found")