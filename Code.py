import time
import os
import platform

Rosa = "\033[1;35m"
Cinza = "\033[1;30m"

def pausa(t):
    time.sleep(t)

# Esperança (dura mais)
print(Rosa + "Eu acredito em nós.")
pausa(2)

print(Rosa + "Mesmo quando cansa.")
pausa(2)

print(Rosa + "Mesmo quando dói.")
pausa(2)

print(Rosa + "Porque sentimento de verdade insiste.")
pausa(3)

print(Rosa + "Eu fiquei.")
pausa(2)

print(Rosa + "Esperei.")
pausa(2)

print(Rosa + "Dei tempo.")
pausa(2)

print(Rosa + "Dei espaço.")
pausa(2)

print(Rosa + "Dei chances.")
pausa(3)

print(Rosa + "Achei que você veria.")
pausa(3)

print(Rosa + "Achei que mudaria.")
pausa(3)

print(Rosa + "Achei que importava.")
pausa(4)

# Transição
print(Cinza + "Achei.")
pausa(4)

# Queda
print(Cinza + "Esperança não falha.")
pausa(3)

print(Cinza + "Ela só se esgota.")
pausa(4)

print(Cinza + "Enquanto eu acreditava, nada mudava.")
pausa(4)

print(Cinza + "Não houve confronto.")
pausa(3)

print(Cinza + "Só desgaste.")
pausa(4)

print(Cinza + "Caí antes de entender.")
pausa(4)

print(Cinza + "Sem defesa.")
pausa(3)

print(Cinza + "Sem resposta.")
pausa(4)

# Silêncio mortal
pausa(10)

# Desligar o PC
sistema = platform.system()

if sistema == "Windows":
    os.system("shutdown /s /t 0")
elif sistema == "Linux" or sistema == "Darwin":  # Linux / macOS
    os.system("shutdown -h now")
