from enum import Enum

class JenisKelamin(Enum):
    PRIA = 1
    WANITA = 2

patients = []

def add_patient(name: str, gender: JenisKelamin):
    if not isinstance(gender, JenisKelamin):
        raise ValueError("Jenis kelamin harus Pria atau Wanita")
    
    patients.append({
        'nama': name,
        "gender": gender.name
    })

add_patient("Ardhian", JenisKelamin.PRIA)
add_patient("Taylor", JenisKelamin.WANITA)

print(patients)