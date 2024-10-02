from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Definir o fuso horário
timezone = pytz.timezone('America/Sao_Paulo')

# Criar um novo calendário
cal = Calendar()

# Definir as datas de início das semanas
# Ano, Mes, Dia, Hora, Minuto, Segundo
start_date = datetime(2024, 9, 23, 9, 0, 0, tzinfo=timezone)

# Matérias para cada dia da semana
schedule = {
    "Segunda-feira": [
        ("Q: Requisitos", start_date),
        ("Q: Matemática", start_date + timedelta(hours=2)),
        ("Q: Matemática", start_date + timedelta(hours=4)),
        ("Q: Estatística", start_date + timedelta(hours=7)),
        ("XXX Português", start_date + timedelta(hours=11)),
    ],
    "Terça-feira": [
        ("E: Web Services", start_date + timedelta(days=1)),
        ("Q: Teste de Software", start_date + timedelta(days=1, hours=2)),
        ("Q: SQL", start_date + timedelta(days=1, hours=4)),
        ("Q: Big Data", start_date + timedelta(days=1, hours=7)),
        ("XXX Inglês", start_date + timedelta(days=1, hours=11)),
    ],
    "Quarta-feira": [
        ("E: Web Services", start_date + timedelta(days=2)),
        ("Q: Java", start_date + timedelta(days=2, hours=2)),
        ("Q: UML", start_date + timedelta(days=2, hours=4)),
        ("Q: Data Warehouse", start_date + timedelta(days=2, hours=7)),
        ("XXX", start_date + timedelta(days=2, hours=11)),
    ],
    "Quinta-feira": [
        ("E: RUP", start_date + timedelta(days=3)),
        ("Q: Endereçamento", start_date + timedelta(days=3, hours=2)),
        ("Q: Algoritmos", start_date + timedelta(days=3, hours=4)),
        ("Q: Pilha/Fila", start_date + timedelta(days=3, hours=7)),
        ("XXX", start_date + timedelta(days=3, hours=11)),
    ],
    "Sexta-feira": [
        ("Q: XXX", start_date + timedelta(days=4)),
        ("Q: XXX", start_date + timedelta(days=4, hours=2)),
        ("Q: XXX", start_date + timedelta(days=4, hours=4)),
        ("Q: XXX", start_date + timedelta(days=4, hours=7)),
    ],
}

# Adicionar eventos ao calendário
for day, tasks in schedule.items():
    for task, start_time in tasks:
        event = Event()
        event.add('summary', task)
        event.add('dtstart', start_time)
        event.add('dtend', start_time + timedelta(hours=1))
        event.add('dtstamp', datetime.now(tz=timezone))
        event.add('description', f'Estudo de {task}')
        cal.add_component(event)

# Salvar o calendário em um arquivo .ics
with open('/Users/gabrielgarcia/Downloads/calendario_estudos.ics', 'wb') as f:
    f.write(cal.to_ical())
