from datetime import datetime,timedelta

# data
hoje = datetime.now()
print(hoje)
print(hoje.date())
print(hoje.day)
print(hoje.mouth)
print(hoje.year)

amanha = hoje + timedelta