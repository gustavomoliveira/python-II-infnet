agenda = {}
agenda = {
    'Maria': ['11111-1111']
}
agenda['André'] = ['22222-2222', '33333-3333']
agenda['Gustavo'] = ['44444-4444']

if 'Gustavo' in agenda:
   contato = agenda['Gustavo']
   contato.append('66666-6666')

print(agenda)
print(agenda['Gustavo'])
print(agenda.get('Gustavo'))

def exibir_agenda(agenda):
   for contato in agenda:
      print(contato, agenda[contato])

exibir_agenda(agenda)

if 'Maria' in agenda:
   agenda.pop('Maria')
   print(agenda)
else:
   print('ERRO: nome não existe.')

print(agenda.keys())
print(agenda.values())