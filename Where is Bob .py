#prøve på spill

import time 
import sys 

ord0 = ["\nVelkommen til 'Bob is gone'! \n\nMålet med spillet er å komme seg ut av situasjonen du befinner deg i før du går tom for energi. Det er opp til deg om du er oppmerksom nok til å legge merke til detaljene som kan redde deg. \n\nLykke til!"]

for typing in ord0[0]: #loop
    time.sleep(0.03) #time of typing
    sys.stdout.write(typing)
    sys.stdout.flush()
#Det er en loop som gjør slik at teksten blir printet som en skrivemaskin 

navn = input("\nHva vil du karakteren din skal hete? \n\nSvar: ")   

#Inputen gir deg valget av hva du vil karakteren din skal hete, noe spm kommer i bruk senere i spillet
#Hvis personen heter Bob, vil spillet avsluttes, det er i en if-statement på slutten av programmet

bok = []

nokler = []

#Disse tomme listene blir fylt etterhvert som du får tak i de ulike objektene i spillet

#Alle de ulike funksjonene som blir brukt i løpet av spillet er definert her 

def skrive (x, y):
    for typing in x[0]: #loop
        time.sleep(y) #time of typing
        sys.stdout.write(typing)
        sys.stdout.flush()
#For å gjøre skrivemaskin-effekten lettere, har jeg sefinert den som en funksjon som jeg bruker i løpet av resten av spillet

def vaken():
    print("\nENERGI : * * * \n")
    ord1 = ["Du våkner. Du kjenner at du er veldig svimmel og har en kul i hodet. Du ser deg rundt. Rommet du befinner deg i er stort og mørkt. På gulvet ved siden av deg ligger dine to venner som også er bevisstløse, Mikkel og Annabelle. Hva har skjedd? "]
    skrive(ord1, 0.005)
    input()
    choice1 = input("Vil du: \n A. Undersøke rommet du befinner deg i \n B. Prøve å vekke vennene dine \n\nSvar:  ")
    if choice1.lower() == "a":
        undersoke()
    elif choice1.lower() == "b": 
        vekkedeandre()
        
def undersoke():
    ord2 = ["\nDu ser en bokhylle og en kiste i et hjørnet. Det kalde og harde gulvet presser seg mot kroppen din, og du sliter med å komme deg opp på starten... Hvordan havnet du i denne situasjonen? \n"]
    skrive(ord2, 0.005)
    input()
    choice2 = input("Hvilken gjenstand vil du undersøke først? \n A. Bokhyllen  \n B. Kisten \n\nSvar: ")
    if choice2.lower() == "a":
        bokhylle()
    elif choice2.lower() == "b":
        kiste()
        
def vekkedeandre():
    ord3 = ["\nMikkel og Annabelle ligger på det kalde gulvet på hver sin side av deg. Det ser ut som om de sover, men begge er ganske rufsete. Rommet er kaldt og kledd med nakne mursteinsvegger, det er ingen vinduer der, kun en dør."]
    skrive(ord3,0.005)
    input()
    ord4 = ["\nDu dulter forsiktig borti Mikkel. Han har på seg favoritttrøya si og et par slitte jeans. Du rister i skulderen hans og han åpner øynene forsiktig. Blikket hans er like forvirret som ditt."]
    skrive(ord4,0.005)
    input()
    ord5 = ["\nAnnabelle er ganske så irriterende så du gidder ikke å prøve å vekke henne. Mikkel har alltid vært bestevennen din. Men det som er merkelig, er at Bob ikke er med dere. Hvor har han blitt av? Hva har skjedd?"]
    skrive(ord5,0.005)
    input()
    ord6 = ["\nMikkel kommer sakte men sikkert til seg selv. Han virker redd. Annabelle er også i gang med å våkne. \n\n'Hva har skjedd?' spør du forsiktig \n\n'Jeg har ingen anelse' svarer Mikkel med en skjelvende stemme \n\n'Vi ble kidnappet' hvisket Annabelle stille. Hun satt oppreist nå og så seg forsiktig rundt. \n"]
    skrive(ord6,0.005)
    input()
    print("'",navn, ",hvor er Bob? Han var jo med oss igår?'")
    input()
    choice3 = input("Hva gjør du nå? \n A. Prøver å åpne døra \n B. Prøver å finne mobilen din \n\nSvar: ")
    if choice3.lower() == "a":
        dor()
    elif choice3.lower() == "b":
        ord7 = ["\nMobilen din er ikke i lommen din hvor du la den sist. Den må nok ha falt ut eller så har noen andre tatt den..."]
        skrive(ord7,0.005)
        dor()
            
def bokhylle():
    ord8 = ["\nDu går forsiktig mot bokhyllen. Den er veldig støvete og inneholder cirka 20 bøker. Det ser ut som om ingen har vært borti denne på flere år..."]
    skrive(ord8,0.005)
    input()
    ord85 =["\nDu tar opp en den første boken du ser - en bok om psykologi. Det er ikke noe spesielt med den, så du setter den tilbake igjen. Du snur deg og ser utover rommet igjen."]
    skrive(ord85, 0.005)
    bok.append(1)
    input()
    choice4 = input("\nVil du: \n A. Undersøke kisten \n B. Prøve å vekke de andre \n\nSvar: ")
    if choice4.lower() == "a":
        kiste()
    elif choice4.lower()== "b":
        vekkedeandre()
            
def kiste():
    ord9 = ["\nKisten er ganske stor. Den likner på en skattekiste. Du åpner den forsiktig og den gir fra seg et høyt knirk. Det første du ser når du åpner den, er et bilde av psykologen Erik Erikson. I psykologitimen forrige uke hadde en i klassen en presentasjon om han. Han var kjent for sin teori om psykologisk utvikling av mennesker. Hvem har bilder av psykologer liggende rundt?"]
    skrive(ord9, 0.005)
    input()
    choice5 = input("\nVil du: \n A. Undersøke bokhyllen \n B. Prøve å vekke de andre \n\nSvar: ")
    if choice5.lower()== "a":
        bokhylle()
    elif choice5.lower()== "b":
        vekkedeandre()
            
def dor():
    print("\nENERGI : * * ")
    input()
    ord10 = ["\nDu og Mikkel reiser dere forsiktig opp. Annabelle ser ut som om hun er i sin egen verden. Dere går mot døra og prøver å åpne den. Den er låst. \n\n'Den er låst' påpeker Annabelle. Hun trasket sakte bak dere. "] 
    skrive(ord10,0.005)
    input()
    ord101 = ["'WOw viRKeLIg?'svarte Mikkel sarkastisk. Han var heller ikke så stor fan av Annabelle. Den eneste grunnen til at hun fulgte etter dere var Bob, men uten han, var det bare rart at hun ville tilbringe tid med dere. Bob var limet som holdt dere sammen.\n\n'Men det er tre nøkkelhull'"]
    skrive (ord101, 0.005)
    input()
    choice6 = input("Du foreslår at dere leter etter nøklene for å låse opp døra i håp om at de befinner seg i dette rommet. \n\nSkal du: \n A. Undersøke bokhyllen nærmere \n B. Se under senga som befinner seg i hjørnet \n\nSvar: ")
    if choice6.lower() == "a":
        bokhyller()
    elif choice6.lower() == "b": 
        seng()
  
def bokhyller():
    if sum(bok) > 0: #Hvis du allerede har gått gjennom funksjonen "bokhylle" vil du ha et element i bok-listen, og hoppe over delen hvor du tar opp den samme boken igjen
        ord11 = ["\nBokhyllen virker plutselig litt annerledes enn da du så på den tidligere. Det virker som om det er andre bøker der nå. Du tar en nærmere kikk på bøkene som befinner seg på hyllen."]
        skrive(ord11,0.005)
        input()
        choice7 = input("\nHvilken bok vil du undersøke nærmere? \n A. En bok om ensomhet \n B. En krimbok \n\nSvar: ")
        if choice7.lower() == "a" or "b":
            bok.append(1)
            choice8 = input("Den boken var ikke noe spesielt, du setter den tilbake. Det er to andre bøker som fanger oppmerksomheten din. \n A. En bok om tidsreiser \n B. En bok om kidnapping \n\nSvar: ")
            if choice8.lower() == "a":
                vaken()
            elif choice8.lower() == "b":
                bok.append(1)
                choice9 = input("Det virker som om du begynner å forstå personen som kidnappet deg litt mer. Det virker som om denne kidnappingen var planlagt, ikke tilfeldig. Neste bøker: \n A. En krimbok av Jo Nesbø \n B. En grøsser av Stephen King \n\nSvar: ")
                if choice9.lower() == "a" or "b":
                    choice10 = input("Ok. Hvordan tror du kidnapperen din er basert på kunnskapen du nå har fått? \n A. En person som er glag i mennesker og regnbuer \n B. En person som har planlagt dette veldig lenge \n C. En person som vil gjøre dere noe vondt \n\nSvar: ")
                    if choice10.lower() == "a": 
                        print("'Dere, hva skal vi gjøre nå?' spurte Annabelle plutselig. Hun satt på gulvet og stirret på en vegg. Både Mikkel og du har gått rundt i rommet og prøvd å undersøke ting nærmere, mens hun bare har sittet der. Du og Mikkel gir hverandre et blikk og fortsetter letingen.")
                        annabelle()
                    if choice10.lower() == "b" or "c":
                        nokkel()
    else: #Hvis personen ikke har gått gjennom funksjonen "bokhylle", vil de allikevel få sjansen til å se på samme bok
        bok.append(1)
        ord12 = ["\nDu går forsiktig mot bokhyllen. Den er veldig støvete og inneholder cirka 20 bøker. Det ser ut som om ingen har vært borti denne på flere år...\n\nDu tar opp en den første boken du ser - en bok om psykologi. Det er ikke noe spesielt med den, så du setter den tilbake igjen. Du snur og ser deg rundt om i rommet igjen.\n"]
        skrive(ord12, 0.005)
        bokhyller()
    
def seng():
    ord13 = ["\nDu går forsiktig mot sengen i det tomme hjørnet. Det er ingenting på veggen bak den. Sengetøyet er hvitt, eller, var hvitt. Det ser ut som om det har ligget der i flere år og har gulnet med årene. Det her også noen mystiske flekker som du ikke ønsker å tenke mer på. Lukten av svette treffer deg når du ankommer sengen. Du rister forsiktig på det motbydelige sengetrekket i håp om å finne en nøkkel som kan få dere ut herfra, men det eneste som har ligget i den sengen de siste par årene, er kakkerlakker og støv. Du grøsser på tanken."]
    skrive(ord13, 0.005)
    input()    
    ord131 = ["\nDu kneler forsiktig ned ved sengerammen. Kankje det er noe som befinner seg under sengen? Blikket ditt legger seg på en firkantet svart gjendstand som kontrasterer mot det bleke og støvete gulvet. Gjenstanden har ikke like mye støv på seg som alt annet rundt. Armen din er akkurat ikke lang nok, så du må legge deg på det møkkete gulvet. Fingrene dine låser seg rundt gjenstanden, og du kan ikke ignorere følelsen av at dette er noe du er kjent med fra før av. Armen din er full av støv når du drar den ut fra under sengen."]
    skrive(ord131, 0.005)
    input()   
    ord132 = ["\nGjenstanden som nå befinner seg i din hånd, er en mobil, men ikke en hvilken som helst mobil. \n\n'Mikkel!' roper du ut i glede. 'Se hva jeg fant!' \n\nMikkel og Annabelle snur seg forsiktig mot deg. Deres fjes lyser opp med det første. "]
    skrive(ord132, 0.005)
    input()
    print("\n'",navn,"er det det jeg tror det er?' svarer Mikkel før hans ansiktsuttrykk blir mørkt. \n\n'Det er Bobs mobiltelefon'")
    input()
    choice12 = input(" A. Prøv å skru på mobiltelefonen \n B. Se om det er noe mer under sengen \n\nSvar: ")
    if choice12.lower() == "a":
        ord121 = ["\nMobilen er kledd i Bob sitt slitte, velkjente deksel. Du holder inne på-knappen til du ser at skjermer lyser opp. \n\n'Den fungerer fortsatt!'roper du ut av glede, 'den har fortsatt strøm!' \n\n'Hæ? Virkelig?' reagerer Mikkel litt forvirret 'Det er fantastisk.'"]
        skrive(ord121, 0.005)
        input()
        ord122 = ["\nDu ser ned på mobilen og blir møtt av et velkjent bakgrunnsbilde. Bob's bakgrunn er et bilde av hele gjengen deres på en pizzarestaurant et par måneder siden. Dessverre ser du at du ikke er noe dekning, det er ikke noe vits i å prøve å ringe engang.\n\nDu viser mobiltelefonen til de andre, som for å bevise at den faktisk er på. Helt utrolig! \n\n'Det betyr at Bob har vært her' sier Mikkel.\n\nShit. Det tenkte du ikke på. Lysten til å gjennom mobilen hans tar over."]
        skrive(ord122, 0.005)
        input()
        choice14 = input("\n A. Se gjennom hans meldinger \n B. Se gjennom hans bilder \n\nSvar: ")
        if choice14.lower() == "a" :
            meldinger()
        elif choice14.lower() == "b":
            plante()
    elif choice12.lower() == "b":
        ord14 = ["\nDu dukker under sengen for andre gang. Håpet om å finne noe som kan hjelpe dere komme dere ut herfra er stort. Du har nettopp funnet Bobs mobilltelefon! Det er fantastik! Du kjenner etter noe med hånden. Det tykke laget av støv begynner å samle seg under neglene dine. Du fortsetter å føle etter med hånden, men det virker som om det ikke er noe der. \n\n'Det er ikke noe mer der' sier du til de andre med et hint av skuffelse. \n\n'La meg sjekke' sier Annabelle og legger seg ned på bakken før du kan protestere. \n\n'Ok, du hadde rett. Det er ikke noe mer der.'\n"]
        skrive(ord14, 0.005)
        annabelle()
            
def nokkel():
    ord15 = ["\nPlutselig legger du merke til en bok du ikke så før. Noe som egentlig er litt rart siden den ser helt ny ut. Det er den største boken på hyllen, og bokryggen har små gulldetaljer som glinser i lyset til den stusselige lyspæren hengede fra taket. Du tar opp boken og blir overrasket over hvor lett den er. På forsiden er det avbildet en stor sølvnøkkel. Du åpner den forsiktig og hinner ut at den er hul. Det er en falsk bok! I beholderen kamuflert som en bok finner du akkurat det du lette etter - en nøkkel!\n"]
    skrive(ord15, 0.005)
    input()
    if sum(nokler) < 2 :
        nokler.append(1)
    print("\nANTALL NØKLER: ", sum(nokler))
    input()
    choice13 = input("Du har nå funnet en nøkkel som muligens vil få dere ut av dette dystre rommet. \n A. Fortell de andre og se om den låser opp døra \n B. Du stoler ikke helt på Annabelle, du velger å holde dette for deg selv \n\nSvar: ")
    if choice13.lower() == "a":
        samarbeid()
    elif choice13.lower() == "b" : 
        annabelle()
            
def annabelle():
    ord16 = ["\nDu har lenge syntes det var noe rart med Annabelle. Det har alltid virket som om hun visste litt for mye, eller i visse situasjoner, litt for lite. Spesielt nå som Bob ikke var her, var det enda mer tydelig å se hvor rar hun egentlig var"]
    skrive(ord16, 0.005)
    input()
    choice14 = input("\nHva skal du gjøre med Annabelle? \n A. Ignorere henne, hun er sikkert bare forvirret \n B. Press henne til å si hvorfor hun vet så mye om dette stedet \n\nSvar: ")   
    if choice14.lower() == "a":
        bob()
    elif choice14.lower() == "b":
        ord165 = ["\n'Du, Annabelle?' \n\n'Ja?' hun snur hodet sitt mot deg. \n\n'Kan du sånn seriøst fortelle hvorfor det virker som om du vet så utrloig mye om dette stedet?' \n\nHun blir stum og rødmer. Blikket hennes er festet på gulvet. Hun prøver å unngå øyekontakt. Mikkel ser forvirret fra deg til henne, og tilbake. \n\n'Skal du bare ignorere meg, eller?'\n\n'Hva er det du tror om meg?'sier hun stille tilbake. Hun ser fortsatt ned i gulvet, men hun rødmer ikke lenger. \n\n'Jeg synes du vet litt mye om dette stedet til å bare havne her tilfeldigvis sammen med oss', sier du. 'Hvordan visste du at vi var kidnappet? Verken jeg eller Mikkel husket det. Eller hvorfor virker det som om du ikke stoler på noen av oss' sier du anklagende. Du er bare helt sikker på at hun er med på dette på et eller annet vis. \n\n'Synes du dette virkelig er en god ide?' hun ser direkte på deg. Du ser at hun knytter kjeven. Hun blunker så vidt. \n\n'Synes du dette virkelig er en god ide?' hun sier det høyere denne gangen. 'Det å vende seg mot hverandre når vi er innelåst i et rom uten å vite hvordan vi skal komme oss ut? Er det en god ide?' Hennes blikk skiftes fra deg til Mikkel. \n\n'Jeg vet at dere to ikke liker meg så godt, men å anklage meg for å være en del av dette? Det er bare helt absurd!' Fjeset hennes er helt rødt nå. \n\n'Hvordan vet du så mye da?' spør Mikkel forsiktig. Han skammer seg. \n\n'Hvis dere hadde giddet å bli litt kjent med meg, hadde dere visst det. Jeg har fotografisk hukommelse' \n\nShit. Det er noe du burde nok ha visst etter å ha kjent henne i fire år. Du ser på Mikkel, han ser flau ut. Annabelle ser derimot utrolig sur ut. \n\n'Dere kommer ikke til å klare å komme dere ut uten meg, jeg bryr meg ikke lenger.' sier Annabelle stille. Hun går mot senga i hjørnet og legger seg forsiktig ned. Hun hjelper ikke lenger med jakten på nøklene. Det du ikke vet ennå, er at hun er en esensiell del av rømningsplanen..."]
        skrive(ord165,0.05)
        print("\nDERE KLARER IKKE Å KOMME DERE UT UTEN ANNABELLE\n")
        time.sleep(5)
        sys.exit()
       
def plante():
    ord17 = ["\nBlant bildene på kamerarulen til Bob ser du mange bilder av dere, noen screenshots av samtaler, og noen teite selfies. Du blar gjennom bildene og kjenner på hvor mye du savner Bob. Hvor mye du savner familen din og de andre vennen dine. Hvordan havnet du her igjen? "]
    skrive(ord17, 0.005)
    input()
    ord171 =["Et av bildene passer ikke inn i kategoriene. Det er et bilde av en stusselig potteplante. Bildet ble tatt et par uker siden. \n\n'Det er potteplanten som er her i hjørnet jo!' roper Mikkel over skulderen din. Han så på bildene sammen med deg. \n\nHan hadde rett, pottplanten på kamerarullen er lik potteplanten som er til høyre for døren.\n\nMikkel beveger seg mot planten og løfter den opp. Det er en inntrket solsikke. På bildet til Bob var den fullstendig frisk. Mikkel løfter potten, og undersøker den. Det er ingenting under den."] 
    skrive(ord171, 0.005)
    input()
    ord172 =["\n'Se om det er noe i jorden' sier Annabelle. Hun holder en distanse til dere og observerer bare. Mikkel ser opp på henne med et mistenktsomt blikk og gjør som hun sier. Han graver fingrene sine i jorden og rører om. Blikket hans er konsentrert i en god stund, før det endres til overrasket. Hans skitne fingre løftes forsiktig opp med en gjenstand låst i grepet. \n\n'Det er en nøkkel'"]
    skrive(ord172, 0.005)
    input()
    if sum(nokler) < 2: 
        nokler.append(1)
    input()
    print("\nANTALL NØKLER: ", sum(nokler))
    input()
    choice15 = input("Vil du: \n A. Prøve den i døra \n B. Se om det er flere spor på mobilen til Bob \n\nSvar: ")
    if choice15.lower() == "a":
        ord18 = ["\nMikkel børster av overflødig jord fra nøkkelen. Han reiser seg, og tar korte skritt mot døra. Det er tydelig at han er litt nervøs. Han stikker ut nøkkelen han nettopp fant, og plasserer den forsiktig i nøkkelhullet. Han snur seg spent tilbake med det samme han inser den passer perfekt i det første nøkkelhullet. Han vrir nøkkelen om, og det lyder et høyt klikk fra døren. \n\n'Den passer!' roper han nærmest ut av glede. 'Bare to nøkler igjen, så kommer vi oss ut herfra'"]
        skrive(ord18, 0.005)
        input()
        sult()
        """
        if sum(nokler) == 2: 
            choice16 = input("Vil du fortelle de andre om den andre nøkkelen du fant? \n\nSvar: ")
            if choice16.lower() == "ja" or "yup" or "jupp" or "je" or "jee" or "jeee" or "sure" or "yes" or "ok" or "greit" or "jes" :
                samarbeid()
            if choice16.lower() == "nei" or "no" or "nop" or "nope" or "neeei" or "neei" or "neii" :
                print("\nSamabeid er viktigst! Dere klarer ikke å komme dere ut dersom dere ikke samarbeider.")
                print("\nTHE END\n")
                print(exit)
        else: 
            choice17 = input("Hvor vil du lete etter de andre nøklene? \n A. Bokhyllen \n B. Kjenn etter i veggene \n\nSvar: ")
            if choice17.lower() == "a":
                bokhyller()
            elif choice17.lower() == "b":
                vegger()
        """        
    elif choice15.lower() == "b":
        meldinger()
  
def meldinger():
    ord19 = ["\nDu åpner meldign-appen på mobilen til Bob. Du går kjapt inn på samtalen mellom dere to, kun for minnenes skyld. De siste meldingene handlet bare om når og hvor dere skulle møtes igår. Eller var det igår? Hvor lenge har dere egentlig vært i dette rommet? Hva om det egentlig har gått flere uker? Hva om dere har vært fanget her i flere måneder, men det er først nå dere har fått bevisstheten tilbake? Hva om dere fikk amnesia? \n"]
    skrive(ord19, 0.005)
    input()    
    ord191 = ["\nBob har hatt samtaler med mange. Du kjenner igjen de fleste, moren hans, Annabelle, en annen fra klassen. Men det er et nummer som ikke er lagret engang. Du går inn på samtalen. Den inneholder kun to meldinger, den ene er fra Bob. \n\n'Bertil Holberg smørefilmen' var meldingen fra Bob \n\n'splay tachyons'lød svaret."]
    skrive(ord191, 0.005)
    input()
    choice16 = input("\n A. Spør de andre om de vet hvem Bertil Holberg er \n B. La dem få lese meldingene selv \n\nSvar: ")
    if choice16.lower() == "a" or "b" : 
        ord20 = ["\nDu gir telefonen til Mikkel. \n\n'Vet dere hvem Bertil Holberg er?' spør du. \n\n'Hvem?' spør Annabelle som ikke har fått se på samtalen ennå. \n\n'Jeg har ingen anelse' svarer Mikkel når han gir fra seg mobilen over til Annabelle. Hun tar den ivrig imot og leser samtalen nøye. \n\n'Hva skal dette bety? Jeg forstår ingenting' spør du. \n\n'Han var sikkert full da han skrev det' svarer Mikkel kjapt."]
        skrive(ord20, 0.005)
        input()
        choice17 = input("\n A. Undersøk dette nærmere \n B. Prøv å lete etter nøkkelen et annet sted \n\nSvar: ")
        if choice17.lower() == "a":
            ord21 = ["\n'Dere? Hva om det betyr noe annet enn det vi tror?' sier Annabelle tankefullt. 'Jeg har lest en del om ulike koder, og disse frasene gir tilsynelatende ikke noe mening' \n\nMikkel kikker på deg forvirret. Annabelle har alltid vært utrolig smart, det visste du, men du forventet ikke at hun skulle være den beste personenå være låst i et ukjent rom med."]
            skrive(ord21, 0.005)
            kode()
        elif choice17.lower() == "b":
            plante()
            
def kode():
    choice18 = input("\nHva slags kode tror du er brukt for å skrive disse meldingene? \n A. Caesars cipher \n B. Et anagram \n C. Skrevet baklengs \n\nSvar: ")
    if choice18.lower() == "b" :
        print("\nHvis meldingene er anagrammer, har du flere muligheter til hvordan de kan lyde: \n'BHer billeier Golfstrømmen' og 'analyst psycho' \n'bortførelsen blir hemmelig' og 'psychoanalyst ' \n'Bill bortføre himmelsenger' og 'hasty syncopal'")
        input()
        print("\nDet er dessverre alt du får vite så langt.")
        bob()
    elif choice18.lower() == "a" : 
        print("\nMed denne koden lyder meldingene sik: 'Ehuwlo Kroehuj vpbuhilophq' og 'vsodø wdfkørqv'\nDet høres ikke helt riktig ut.")
        input()
        kode()
    elif choice18.lower() == "c" :
        print("\nMed denne koden lyder meldingene sik: 'snoyhcat yalps' og 'nemliferøms grebloH litreB'\nDet høres ikke helt riktig ut.")
        input()
        kode()     
            
def samarbeid():
    ord23 = ["\nDu forteller de andre om nøkkelen du fant, og dere ser om den passer i døra med det første. Den passer i det andre nøkkelhullet! Mikkel foreslår at alle samarbeider for å finne de siste nøklene.\n"]
    skrive(ord23, 0.005)
    if sum(nokler) < 2 : 
        seng()
    if sum(nokler) == 2 : 
        sult()

def vegger():
    ord24 = ["\nDu går bort til den lite belyste veggen, og plasserer hendene dine på de kalde mursteinene. Du føler etter med fingrene for å se om det muligens finnes en hemmelig dør bak en av mursteinene. Du lar fingrene dine vandre bortover langs veggen. Du fortsetter over hele rommet, men finner ikke noe spesielt."]
    skrive(ord24, 0.005)
    sult()

def bob():
    ord25 = ["\nHele denne situasjonen har fått deg til å tenke på Bob. Kanskje Bob ikke er den du tror han var heller? Hva om du i løpet av hele deres vennskap har hatt en illusjon av hvordan han egentlig er som person. Du har tatt feil av folk før, hva om du har gjort det igjen? \n\nDu har kjent Bob siden starten av ungdomsskolen. Han har alltid vært der for deg, men dere har ikke nødvendigvis vært veldig nære. Hva om Bob egentlig skjulte noe? Hvorfor har han unsluppet sjebnen som du, Mikkel og Annabelle lider nå? Hvorfor er han den eneste som er borte fra deres gjeng, og ikke på dette rommet sammen med dere? \n\nDet kan forsåvidt hende at han lider en skjebne verre enn deres? Hva om han ikke er kidnappet med dere siden han ble myrdet? Hva om han blir torturert i rommet ved siden av?"]
    skrive(ord25, 0.005)
    time.sleep(1)
    choice19 = input("\nTror du: \n A. Bob har noe med saken å gjøre \n B. Bob er sikkert uskyldig \n\nSvar: ")
    if choice19.lower() == "a" or "b" : 
        sult()

def sult():
    ord26 = ["\nMagen din gir fra seg en voldsom lyd. Det høres ut som en døende hval. Sulten slår over seg som en hetebølge."]
    skrive(ord26, 0.03)
    input()    
    ord261 = ["\n\nMikkel og Annabelle ser på deg med et forståelsesfullt blikk. De må nok ha kjent på den samme følelsen. Det har nok gått flere timer siden dere spiste, men det virker ikke som om det er noe spiselig i nærheten."]
    skrive(ord261, 0.03)
    input()    
    ord262 = ["\n\n'Noen som er keen på å spise litt støv?' spurte Mikkel. Det var litt usikkerhet på om det han sa faktisk var på tull eller om han søkte deres tillatelse på å synke så lavt. Annabelle så enda værre ut. I det svake lyset kunne du skimte at hun var utrolig blek og holdt seg om magen. Mikkel virket som om han gikk fra vettet. Tørsten og sulten hadde tatt overhånd, og beordret Mikkel til å slutte å funksjonere som et menneske. Han sto og så ut i ingenting. \n\nAnnabelle virket som om hun hadde store smerter. Hun grep om magen sin og bøyde seg framover. Hun løp bort til det ene hjørnet i rommet og støttet seg opp med begge armene. Som en bombe, eksploderte hennes middag fra gårsdagen ut på gulvet. Hun kastet opp det lille som fortsatt befant seg i magesekken hennes. \n\n'Gutta, jeg beklager. Sorry.'"]
    skrive(ord262, 0.03)
    input()   
    ord263 = ["\n\n'Du kan ikke noe for det, det går bra. Hvordan føler du deg?' svarte du rolig, men du fikk ikke noe svar. Annabelle virket veldig opptatt av noe i hennes lille oppkast-klump. Du prøvde å ignorere den velkjente, kvalmende lukten som tok over rommet, og bevegde deg mot henne. \n\nTil din overraskelse, tok hun hånden sin oppi den gjennomtyggede spaggethien og begynte å røre rundt. Du spratt tilbake. Hva var det hun holdt på med? Hun tok opp en liten gjenstand fra hennes oppkast. \nDet var en nøkkel!"]
    skrive(ord263, 0.03)
    input()
    nokler.append(1)
    print("\nANTALL NØKLER: ", sum(nokler))
    print("\nENERGI : * \n")
    if sum(nokler) < 3 : 
        ord27 = ["\nDet virker som om dere fortsatt har for få nøkler til å komme dere ut. \n\nMen du har ikke mer energi til det..."]
        skrive(ord27, 0.005)
        input()
        print("THE END")
        sys.exit()
    elif sum(nokler) == 3 : 
        ut()
        
def ut():
    ord28 = ["\nDere har klart å få tak i alle tre nøklene. Gratulerer! \n\n Dere tar alle tre nøklene i døra, og vrir om. Døra glir sakte opp. Et sterkt lys blender dere fra utsiden. Du er den første på vei ut. \n\n'Bob?'\n"]
    skrive(ord28, 0.005)
    input()
    ord29 = ["\n'nei...'\n"]
    skrive(ord29, 0.1)
    input()
    ord30 = ["\n\nFORTSETTELSE FØLGER I 'BOB IS NOT GONE ALLIKEVEL'\n"]
    skrive(ord30, 0.1)
    input()
    print("\nTHE END\n")
    sys.exit()
    
#Hvis personen heter Bob, vil spillet avsluttes siden spillet heter "Where is Bob?", og du nå har funnet Bob
#Hvis personen ikke heter Bob, vil spillet fortsette  
    
if navn.lower() == "bob":
    print("\nGratulerer! \n\nDU HAR FUNNET BOB!")
    print("\nTHE END")
    sys.exit()

else:
    vaken() 
