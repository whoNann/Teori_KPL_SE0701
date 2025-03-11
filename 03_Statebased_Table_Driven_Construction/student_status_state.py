from enum import Enum

class StudentStatusState(Enum):
    TERDAFTAR = "terdaftar"
    CUTI = "cuti"
    AKTIF = "aktif"
    LULUS = "lulus"

class TriggerInputState(Enum):
   CETAK_KSM = "Cetak KSM"
   MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"
   LULUS = "Lulus"
   MENGAJUKAN_CUTI = "Mengajukan Cuti"

state_transition = {
    StudentStatusState.TERDAFTAR: {
        TriggerInputState.CETAK_KSM: StudentStatusState.AKTIF,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    },
    StudentStatusState.CUTI: {
        TriggerInputState.MENYELESAIKAN_CUTI: StudentStatusState.TERDAFTAR
    },
    StudentStatusState.AKTIF: {
        TriggerInputState.LULUS: StudentStatusState.LULUS,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    }
}

def change_state(current_state, triggerInput):
    cond_1 = current_state in state_transition # Return True or False
    cond_2 = triggerInput in state_transition[current_state] # Return True or False
    if cond_1 and cond_2:
        return state_transition[current_state][triggerInput].value
    return "Transisi Tidak Valid"

current_state = StudentStatusState.TERDAFTAR
trigger_input = TriggerInputState.CETAK_KSM

next_state = change_state(current_state, trigger_input)
print(next_state) 

# print(change_state(StudentStatusState.TERDAFTAR, TriggerInputState.CETAK_KSM)) # AKTIF
# print(change_state(StudentStatusState.TERDAFTAR, TriggerInputState.MENGAJUKAN_CUTI)) # CUTI