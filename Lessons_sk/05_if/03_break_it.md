# 💥 Pokazte to!

Napíšte také konštrukcie `if`, ktoré Python odmietne s chybou alebo ktoré **nerobia to, čo očakávame**.

~~~python
vek = 17

if vek >= 18:
    print("Môžeš vstúpiť.")
else:
    print("Ešte nemôžeš vstúpiť.")
~~~

Skúste napríklad:
- vynechať dvojbodku: `if vek >= 18`
- neodsadiť príkaz pod `if`
- použiť v jednom bloku rozdielne odsadenie
- napísať `=` namiesto `==`: `if vek = 18:`
- pridať podmienku za `else`: `else vek < 18:`
- umiestniť `elif` pred `if`
- vytvoriť vždy pravdivú podmienku: `if znamka == 1 or znamka == 2 or True:`

Prečítajte si chybové hlásenie:
- Ako sa chyba volá a na ktorý riadok ukazuje?
- Ktorú chybu Python oznámi okamžite?
- Ktorá chyba nespôsobí chybové hlásenie, ale dá nesprávny výsledok?
