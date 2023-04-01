segundos1 = input("Por favor, entre com o número de segundos que deseja converter:")

dias = int(segundos1) // 86400
segundos2 = int(segundos1) % 86400
horas = segundos2 // 3600
segundos3 = segundos2 % 3600
minutos = segundos3 // 60
segundos4 = segundos3 % 60
print(dias, "dias e", horas, "horas e", minutos, "minutos e", segundos4, "segundos.")
