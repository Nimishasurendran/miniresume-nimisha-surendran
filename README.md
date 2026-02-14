Mini Resume Management API

This project is a simple FastAPI application that allows uploading, viewing, filtering, and managing candidate resumes.


Technologies used :
Python 3.12.1
fastapi
uvicorn
pydantic
python-multipart

Installation:
pip install -r requirements.txt

Running the Project :
uvicorn main:app --reload

OPEN SWAGGER :
http://127.0.0.1:8000/docs

Core Functional Requirements
1. Resume Upload
POST /candidates
Uploads candidate details along with resume file.
Input Fields:
Full Name
Date of Birth
Contact Number
Contact Address
Education Qualification
Graduation Year
Years of Experience
Skill Set
Resume File

2. List Candidates
GET /candidates
Returns all candidates.
Optional Filters:
skill
experience
graduation_year

3. Get Candidate by ID
GET /candidates/{candidate_id}
Returns candidate details using unique ID.

4. Delete Candidate
DELETE /candidates/{candidate_id}
Deletes a candidate by ID.

Must add a candidate first, otherwise GET will fail.
Go to POST /candidates
Click Try it out
Fill the form + upload resume
Click Execute

NEXT
Get candidate by ID
Open GET /candidates/{candidate_id}
Click Try it out
enter candidate id
Click Execute

We can delete Candidate also