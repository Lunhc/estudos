import time
from datetime import datetime

hora_alarme = input('Que horas voce quer o alarme? (Fromato HH:MM) ')

print('Alarme definido para', hora_alarme)

while True:
    agora = datetime.now() .strftime('%H:%M')
    
    if agora == hora_alarme:
        print('Alarme! Hora de acordar!')
        break

    time.sleep(30)

