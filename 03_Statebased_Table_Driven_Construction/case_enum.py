from enum import Enum

class JenisKelamin(Enum):
    LAKI_LAKI = 1
    PEREMPUAN = 2

print(JenisKelamin.LAKI_LAKI) ## Value of Enum => JenisKelamin.LAKI_LAKI
print(JenisKelamin.LAKI_LAKI.value) ## Value dari LAKI_LAKI => 1
print(JenisKelamin.LAKI_LAKI.name) ##nama Enum => LAKI_LAKI