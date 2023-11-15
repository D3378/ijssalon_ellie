from algemene_functies import mijn_functie_2
def aanbieding_1(smaak,prijs,korting):
    korting2 = korting * 30
    korting3 = int(korting2)
    korting4 = str(korting3) + ",60"
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting4} euro."
def inkomsten_totaal(inkomsten,btw):
    totaal = 0
    for nr in inkomsten:
        totaal += nr
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw} euro btw betaald dient te worden."
def laag_en_hoog(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)
def gemiddelde(mijn_lijst):
    totaal = 0
    for nr in mijn_lijst:
        totaal += nr
    gemid = totaal / 7
    return f"De gemiddelde inkomsten deze week zijn {gemid} euro."
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    nieuwe_getallen = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return nieuwe_getallen