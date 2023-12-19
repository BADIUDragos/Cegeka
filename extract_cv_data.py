import fitz


# this function can be improved, split, and reduced in size in many ways for generic reasons etc.
# since the assignment said I could hard code from start I see no need to do that momentarily

def extract_and_structure_cv_data(file_path):
    with fitz.open(file_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()

    lines = text.split('\n')
    personal_info = {'name': lines[0], 'location': lines[1], 'contact': lines[2:5]}

    experience_index = lines.index('Experience')
    experience = {'Rolls-Royce': lines[experience_index + 2: experience_index + 15],
                  'Annedora': lines[experience_index + 17: experience_index + 26],
                  'CAE': lines[experience_index + 27: experience_index + 35],
                  'Thales': lines[experience_index + 37: experience_index + 52]}

    # technical skills included for show-cv data purpose only since it wasn't a requirement
    technical_skills_index = lines.index('Technical Skills')
    technical_skills = lines[technical_skills_index + 1:technical_skills_index + 3]

    education = lines[-4:]

    cv_data = {
        'personal': personal_info,
        'experience': experience,
        'technical_skills': ' | '.join(technical_skills),
        'education': ' | '.join(education)
    }

    return cv_data
