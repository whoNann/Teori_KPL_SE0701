from enum import Enum
import time

class TransactionState(Enum):
    IDLE = "terdaftar"
    MENUNGGU_PRODUK = "menunggu Produk"
    MENGELUARKAN_PRODUK = "mengeluarkan Produk"
    SELESAI = "selesai"

class TriggerState(Enum):
   MASUKKAN_UANG = "Masukkan uang"
   PILIH_PRODUK = "Pilih Produk"
   KELUARKAN_PRODUK = "Keluarakan Produk"
   RESET = "Mengajukan reset"

state_transition = {
   TransactionState.IDLE: {
       TriggerState.MASUKKAN_UANG: TransactionState.MENUNGGU_PRODUK,
   },
   TransactionState.MENUNGGU_PRODUK: {
       TriggerState.PILIH_PRODUK: TransactionState.MENGELUARKAN_PRODUK,
   },
   TransactionState.MENGELUARKAN_PRODUK: {
       TriggerState.KELUARKAN_PRODUK: TransactionState.SELESAI
   },
   TransactionState.SELESAI: {
       TriggerState.RESET: TransactionState.IDLE
   }
}

# def change_state(current_state, triggerState):
#     IF(current_state)

# current_state = StudentStatusState.TERDAFTAR
# trigger_input = TriggerInputState.CETAK_KSM

# next_state = change_state(current_state, trigger_input)
# print(next_state) 

# print(change_state(StudentStatusState.TERDAFTAR, TriggerInputState.CETAK_KSM)) # AKTIF
# print(change_state(StudentStatusState.TERDAFTAR, TriggerInputState.MENGAJUKAN_CUTI)) # CUTI