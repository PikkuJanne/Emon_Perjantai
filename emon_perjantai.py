# Emon Perjantai by PikkuJanne
print("EMON PERJANTAI")
print("Olet laittanut mustat kajalit ja ripsarit naaman, ängennyt itsesi tiukimpiin pillifarkkuihisi ja sx-koon 'girlie' t-paitaan ja lähtenyt ulos perjantai-iltama. Vaihtoehtosi ovat PUISTO/BAARI/KLUBI/KOTIBILEET/KESKUSTA")

flag=0
while (flag == 0):
    valinta=input("Minne suuntaat surullisen hahmon sankari? (PUISTO/BAARI/KLUBI/KOTIBILEET/KESKUSTA): ")

    if valinta == "PUISTO":
        print("\nPäivä on aurinkoinen ja puistossa on paljon porukkaa ja hyvä meno.")
        flag1=0
        while (flag1 == 0):
            puistovalinta = input("Halutako liittyä tuntemattomien PORUKKAAN, JUODA sivummalla yksin pusaria vai lähteä suoraan takaisin KOTIIN koska ei näy tuttuja? ")
            if puistovalinta == "PORUKKAAN":
                print("\nLähestyt vaikean oloisena tuntematonta porukkaa, joka kostautuu bensalenkkareiksi ja vittuilee sinulle homotellen ja neiditellen. Poistut itkien ja meikit sotkussa himaan.")
                flag1=1
            elif (puistovalinta == "JUODA"):
                print("\nHaet itsellesi paikan syrjemmältä puun alta varjossa ja alat kaataa väkevää viiniäsi. Ilta sujuu mukavasti musaa kuunnellen ja ihmisiä tarkkaillen. Kotimatkalla poikkeat vielä yksille ja sammut onnellisena sänkyysi muistisi pamahdettua.")
                flag1=1 
            elif (puistovalinta == "KOTIIN"):
                print("\nVieraiden seuraan tunkeminen tai yksin juoden ovat molemmat liian säälittäviä ja pelottavia vaihtoehtoja, jos teet kumman tahansa kaikki vihaavat sinua. Paniikkikohtauksen siivittämänä lähdet mahdollisimman nopeasti takaisin kotiin missä koitat itkeä itseäsi uneen ja mietit mikä vittu sinussa on vialla ja mikset voi vaan olla kuin muutkin.")
                flag1=1
            else:
                print("Väärin meni, koita rohkeasti uudestaan. Pystyt siihen kyllä.")
        flag=1

    elif valinta == "BAARI":
        print("\nKirkas aurinko häikäisee silmiäsi jopa Wayfarerien läpi ja pakenet ensimmäiseen eteen osuvaan räkälään")
        flag2=0
        while (flag2== 0):
            baarivalinta = input("Haluatko istua KANTISTEN pöytään, YKSIN baaritiskille vai lähteä takaisin KOTIIN koska tämä paikka on liian sketchy? ")
            if baarivalinta == "KANTISTEN":
                print("\nIstut alas kantisten pöytään ja puolen tunnin sisään nämä elämän koulun vikaluokkalaiset uhkaavat hakata ja puukottaa sinua. Lähdet paniikissa kotiin ja vannot ettet enää ikinä lähde sieltä")
                flag2=1
            elif (baarivalinta == "YKSIN"):
                print("\nIstut alas tyhjälle baaritiskille ja tilaat oluen. Joudut välillä harrastamaan small talkia kyypparin ja satunnaisten asiakkaiden kanssa, mutta ilta on mieluisa kun olut ja jallu virtaavat tasaisesti ja saat olla suurimmaksi osaksi omissa oloissasi. Vedät pitkän kaavan mukaan etkä muista miten helvetissä pääsit kotiin tai mitä illan aikana ylipäätään tapahtui.")
                flag2=1 
            elif (baarivalinta == "KOTIIN"):
                print("\nPorukka baarissa on niin vitun shadyn ja vaarallisen näköistä ettet uskalla ovea pidemmälle. Luovutat ja lähdet kotiin ja mietit miten vitun vaikeaa voi olla pitää edes vähän hauskaa ja miten taas yksi perjantai ilta menee hukkaan vitun yksinäisenä ja surullisena.")
                flag2=1 
            else:
                print("Väärin meni, koita rohkeasti uudestaan. Pystyt siihen kyllä.")
        flag=1

    elif valinta == "KLUBI":
        print("\nPikkuklubilla soittaa tänään joku neverhöörd punk bändi ja haluat paeta lentävää helvettiä kellarin viileyteen.")
        flag3=0
        while (flag3 == 0):
            klubivalinta = input("Haluatko käydä juttelemassa soundcheckkiä tekevälle BÄNDILLE, istua nurkkapöytään yksin DOKAAMAAN vai palata KOTIIN koska sisäänpääsymaksu on muka liian korkea? ")
            if klubivalinta == "BÄNDILLE":
                print("\nHivuttaudut nolona stagen läheisyyteen ja särkyvällä äänellä huikkaat moikat laulajalle. Juttelette hetken kaupungin skenen tilasta, jonka jälkeen haet juotavaa, vedät perseet ja riehut keikalla oikein kunnolla. Aamulla on häviksissä luuri ja lompakko, mutta ainakin oli hauskaa.")
                flag3=1
            elif (klubivalinta == "DOKAAMAAN"):
                print("\nEt välitä kovista hinnoista vaan tinaat yksin nurkassasi. Keikalla seisot musapoliisi-asennossa takarivissä ja tönit pittiä kauemmas. Takaisin kotona olet tyytyväinen että vaikka mitään mahtavaa ei tapahtunutkaan niin ainakaan muisti ei mennyt tällä kertaa.")
                flag3=1 
            elif (klubivalinta == "KOTIIN"):
                print("\nOvella tajuat että paikka on jo melko täynnä etkä tunne ketään. Paniikissa väität itsellesi että sisäänpääsymaksu on liian iso tälläisestä paskabändistä ja lähdet itkua pidätellen kotiin. Et vain pysty kuvittelemaan miten voisit mennä melkein selvinpäin täyteen klubiin jossa et tunne yhtään ketään. Kotona kadut koko elämääsi ja kaikkea mitä olet ikinä tehnyt.")
                flag3=1 
            else:
                print("Väärin meni, koita rohkeasti uudestaan. Pystyt siihen kyllä.")
        flag=1

    elif valinta == "KOTIBILEET":
        print("\nKaverisi lähettää sinulle viestiä ja vinkkaa menossa olevista kotibileistä joihin päätät lähteä kuokkimaan.")
        flag4=0
        while (flag4 == 0):
            bilevalinta = input("Halutako liittyä random BILETTÄJIEN seuraan, nussia jäkäristä muitten JUOMIA ja mennä tyhjään makkariin juomaan vai lähteä takaisin kotiin koska bilettäjät eivät olekaan sinun kaveripiiristäsi?  ")
            if bilevalinta == "BILETTÄJIEN":
                print("\nKoitat lähestyä party peopleja, mutta alfaurosten kovaääninen kirosanojen huutelu ahdistaa etkä tunne oloasi mukavaksi näiden tyyppien kanssa. Juot pari kaljaa ja koitat väkisin sietää näitä suuhengittäjiä ja heidän paskaa jumputusbailumusaansa, mutta joudut lopulta tunnustamaan tappiosi ja hiivit vähi äänin takavasemmalle ja poistut kotiin. Kotimatkalla ja kotona sängyssä mietit millaista olisi olla kuin kaikki muut, normaali ihminen, joka voi tehdä normaaleja asioita ja hengailla muidenj normaalien ihmisten kanssa. Et nuku silmäystäkään koko yönä.")
                flag4=1
            elif (bilevalinta == "JUOMIA"):
                print("\nPöllit jäkäristä repun täyteen viinaa ja sulkeudut bileiden järjestäjän pikkusiskon huoneseen. Laitat omat musat soimaan ja alat kaataa muiden viinoja. Välillä joku käy katsomassa mitä huoneessa tapahtuu, mutta et osaa aloittaa keskustelua ja porukka jatkaa matkaa. Myöhemmin järjestäjä tuleew huutamaan sinulle mitä vittua teet pikkusiskon huoneessa ja oletko varastanut kaikki viinasi muilta. Sinut heitetään pihalle bileistä, mutta olet aivan soosissa ja vain anurat asialle. Aamulla elämäsi kovin morkkis iskee ja rukoilet etttet olisi koskaan syntynytkään.")
                flag4=1 
            elif (bilevalinta == "KOTIIN"):
                print("\nOvella bileiden järjestäjä tervehtii sinua hölmistyneen oloisena koska ette tunne toisianne. Tunnet paniikkikohtauksen saapuvan ja mutiset että heität juomat kylmään ja pakenet keittiöön. Otat henkeä ja kuulet olohuoneesta vain tuntemattomien lätkäihmisten huutoa. Paniikkikohtaus alkaa kunnolla ja nappaat juomasi takaisin reppuun ja ryntäät ovelle, tykität portaat alas ja kävelet mahdollisimman nopeasti korttelin päähän ennen kuin uskallat edes hengittää. Pääsi tuntuu kuin se olisi täynnä pumpulia. Ei elämä voi olla tälläistä, nytkin varmaan makaat koomassa sairaalassa tai jotain, elämä ei vain voi olla tälläistä.")
                flag4=1 
            else:
                print("Väärin meni, koita rohkeasti uudestaan. Pystyt siihen kyllä.")
        flag=1

    elif valinta == "KESKUSTA":
        print("\nPäivä on nätti kuin morsian ja morsian nätti kuin leipä. Aina perjantaisin jengi lähtee keskustaan joten mitä turhia suunnittelemaan ja nokka kohti kapista.")
        flag5=0
        while (flag5 == 0):
            kapisvalinta = input("Haluatko lähteä KAPIKSELLE päättömästi pyörimään ja tsekkaamaan mikä meno ja ketä liikenteessä, tai ehkä haluat katsastaa sen tietyn tutun MESTAN johon sinä ja tuttusi aina päädytte vai haluatko kenties palata KOTIIN koska kenestäkään ei ole kuulunut tänään mitään?  ")
            if kapisvalinta == "KAPIKSELLE":
                print("\nHyppäät torilla pois bussista ja tajuat suunnistat hakemaan lähimmmältä kioskilta juomista. Avaat kylmän harmaan ja alat tsekkailla mihin suuntaan lähteä etsimään toimintaa. Tajuat nopeasti että on aivan liian aikaista eikä kaupungilla liiku ketään, vai onko tänään taas joku vitun kendomatsi. Kävelet useamman korttelin ympäri lonkkua hörppien ja tunnet miten kaikki ihmiset tölläävät sinua. Kolmen vartin jälkeen olet takaisin torilla etkä enää jaksa teeskennellä itsellesi että ilta voisi tarjota jotain. Lähdet bussilla kotiin ja tunnet suunnatonta toivottomuutta ja häpeää elämästäsi ja koko olennostasi")
                flag5=1
            elif (kapisvalinta == "MESTAN"):
                print("\nKenestäkään ei ole tänään kuulunut mitään etkä uskalla lähetellä mitään viestejä ettet vaikuttaisi epätoivoiselta ja vanne alkaa puristaa päätäsi ja rintakehää, mutta yksi paikka voi kaiken pelastaa. Joka helvetin viikonloppu sinä ja tuttusi päädytte hengaamaan siihen yhteen ja samaan paikkaan ja siihen panet nyt kaiken toivosi hauskasta illasta. Saavuttuasi paikalle ketään ei kuitenkaan näy. Hörpit hermostuneena mansikkasidukkaasi ja pälyilet ympärillesi huomaten miten kaikki tuntemattomat ihmiset vihaavat sinua eivätkä ymmärrä miksi vitussa olet siinä. Avaat vielä toisen sidukan ja hörpit sen turbona alas kunnes paine kasvaa liian suureksi etkä enää pysty jäämään tähän paikkaan kaikkien katseiden alle. Kiiruhdat bussiin ja vannot ettet kotimatkalla vilkaisekkaan puhelintasi. Dösässä istuen kuitenkin olet lukevinasi jotain ruudulta ja rukoilet että joku viestittäisi. Kukaan ei viestitä ja taas vietät yän miettien miksi vitussa sinulla ei voi olla ystäviä.")
                flag5=1 
            elif (kapisvalinta == "KOTIIN"):
                print("\nIstut bussissa matkalla kapikselle ja mietit ketä tutuistasi voisi tänään olla liikkeellä. Kenestäkään ei kuitenkaan kuulunut mitään ja alat hermostua, entä jos ketään ei olekaan liikkeellä ja jouduin pyörimään kaupungilla itsekseni kuin sekopää. Viestin lähettäminen jollekin kaverilla ja meininkien tiedustelu ei tule kuuloonkaan, miten vitun noloa se olisi. Hyppäät paniikissa pois dösästä, ylität kadun ja jäät masentuneena odottamaan bussia kotiin. Koko kotimatkan vielä rukoilet että joku viestittäisi, mutta kenestäkään ei kuulu. Vietät koko yön selälläsi sängyllä miettien onko sinulla ystäviä tai edes kavereita ollenkaan.")
                flag5=1 
            else:
                print("Väärin meni, koita rohkeasti uudestaan. Pystyt siihen kyllä.")
        flag=1

    else:
        print("Väärin meni, koita rohkeasti uudestaan. Pystyt siihen kyllä.")
        