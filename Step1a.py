#_*_ coding: utf-8 _*_
print('To prosta gra liczbowa, musisz zgadnąć cyfrę od 0 do 10 masz tylo trzy pruby, Powodzenia !' )
zgadłeś = int('7')
for v in range(3):
    twoja_cyfra = int(input('Zgadnij cyfrę między od 0 do 10: '))
    if twoja_cyfra == zgadłeś:
        print('Bravo zgadłeś to cyfra ', zgadłeś)
        break
    elif twoja_cyfra != zgadłeś:
        print('Nie zgadłeś sprubuj jeszcze raz')
else:
    print('Przykro mi wykorzystałeś trzy szanse \nkoniec gry !')

