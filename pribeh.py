from enum import Enum
from random import randint, choice

class EPronouns(Enum):
    PRONOUNS_HE_HIM = 1
    PRONOUNS_SHE_HER = 2
    PRONOUNS_RANDOM = 3

class EStoryContext(Enum):
    THEME_FORTNITE = 1
    THEME_WORLDOFTANKS = 2
    THEME_TF2 = 3
    THEME_CELESTE = 4
    THEME_POKEMON = 5
    THEME_TRAIN = 6
    THEME_MINECRAFT = 7
    THEME_WARHAMMER = 8

def postava_to_pronouns(postavy, postava):
    for pronouns, seznam_postav in postavy.items():
        for postava_ze_seznamu in seznam_postav:
            if postava_ze_seznamu == postava:
                return pronouns
    return None

def story_gen():
    story_context = choice(list(EStoryContext))

    hra = {
    EStoryContext.THEME_FORTNITE: {
        EPronouns.PRONOUNS_SHE_HER: {
            "start": ["dropnula v Tilted Towers.", "dropnula v Loot Laku.", "dropnula ve Wailing Woods.", "dropnula v Paradise Palms.", "dropnula v Dusty Divot.", "dropnula ve Snobby Shores."],
            "konec": ["Mezitím co těžila resources tak dostala Shotgunou od hráče co se nenápadně dostal za ní.", "Viděla droplej loot kterej se pokusila sebrat ale mezitím dostala headshot od hráče se Sniper rifelkou.", "Musela jít AFK tak ji zabil NoSkin s krumpáčem.", "Stavěla ve velké výšce ale náhle ji došly resources a spadnula z moc velké výšky.", "Pokusila se střelit z Rocket launcheru když náhle se před ni postavila zeď takže se zabila vlastní explozí.", "Dostala hned ban za to že řekla N-Slovíčko."]
        },
        EPronouns.PRONOUNS_HE_HIM: {
            "start": ["dropnul v Tilted Towers.", "dropnul v Loot Laku.", "dropnul ve Wailing Woods.", "dropnul v Paradise Palms.", "dropnul v Dusty Divot.", "dropnul ve Snobby Shores."],
            "konec": ["Mezitím co těžil resources tak dostal Shotgunou od hráče co se nenápadně dostal za něj.", "Viděl droplej loot kterej se pokusil sebrat ale mezitím dostal headshot od hráče se Sniper rifelkou.", "Musel jít AFK tak ho zabil NoSkin s krumpáčem.", "Stavěl ve velké výšce ale náhle mu došly resources a spadnul z moc velké výšky.", "Pokusil se střelit z Rocket launcheru když náhle se před něj postavila zeď takže se zabil vlastní explozí.", "Dostal hned ban za to že řekl N-Slovíčko."],
        },
    },
    EStoryContext.THEME_TF2: {
        EPronouns.PRONOUNS_SHE_HER: {
            "start": ["si vybrala za postavu Heavyho.", "si vybrala za postavu Medica.", "si vybrala za postavu Demomana.", "si vybrala za postavu Scouta.", "si vybrala za postavu Engineera.", "si vybrala za postavu Spye.", "si vybrala za postavu Snipera.", "si vybrala za postavu Pyra.", "si vybrala za postavu Soldiera."],
            "konec": ["Hned co vylezla ze spawnu dostala headshot od Snipera.", "Málem sebrala kufřík ale zabila ji Sentry nest která ten kufřík chránila.", "Snažila se zabrat Control Point ale nevšimla si že nepřátelský Demoman na něj dal Stickybomby.", "Mezitím co se snažila tlačit bombu dostala nožem do zad od nepřátelského Spye.", "Málem začala dominovat nepřátelského Hoovyho ale dostal od Scouta Fish Kill a byl ztrapňen před celým týmem."]
        },
        EPronouns.PRONOUNS_HE_HIM: {
            "start": ["si vybral za postavu Heavyho.", "si vybral za postavu Medica.", "si vybral za postavu Demomana.", "si vybral za postavu Scouta.", "si vybral za postavu Engineera.", "si vybral za postavu Spye.", "si vybral za postavu Snipera.", "si vybral za postavu Pyra.", "si vybral za postavu Soldiera."],
            "konec": ["Hned co vylezl ze spawnu dostal headshot od Snipera.", "Málem sebral kufřík ale zabila ho Sentry nest která ten kufřík chránila.", "Snažil se zabrat Control Point ale nevšimnul si že nepřátelský Demoman na něj dal Stickybomby.", "Mezitím co se snažil tlačit bombu dostal nožem do zad od nepřátelského Spye.", "Málem začal dominovat nepřátelského Hoovyho ale dostal od Scouta Fish Kill a byl ztrapňen před celým týmem."]
        },
    },
    EStoryContext.THEME_CELESTE: { 
        EPronouns.PRONOUNS_SHE_HER: {
           "start": ["začala skákat ve Forsaken City.","začala skákat v Old Site.","začala skákat v Celestial Resortu.","začala skákat v Golden Ridge.","začala skákat v Mirror Templu.","začala skákat v Reflection.","začala skákat v Summitu.","začala skákat v Core.","začala skákat ve Farewellu."],
           "konec": ["Narazila na Badeline, tak ho brutálně zavraždila.","Narazila na Badeline a měla s ním horký sex.","Ihned spadla do ostnů a zemřel.","Úspěšně tuto kapitolu dokončila, může jít dál!","Udělala velký skok, avšak jí nedošlo že nemá doplněné dashe a spadla do díry.","Udělala velký skok a přežila."]
        },
        EPronouns.PRONOUNS_HE_HIM: {
            "start": ["začal skákat ve Forsaken City.","začal skákat v Old Site.","začal skákat v Celestial Resortu.","začal skákat v Golden Ridge.","začal skákat v Mirror Templu.","začal skákat v Reflection.","začal skákat v Summitu.","začal skákat v Core.","začal skákat ve Farewellu."],
            "konec": ["Narazil na Badeline, tak ho brutálně zavraždil.","Narazil na Badeline a měl s ním horký sex.","Ihned spadl do ostnů a zemřel.","Úspěšně tuto kapitolu dokončil, může jít dál!","Udělal velký skok, avšak mu nedošlo že nemá doplněné dashe a spadl do díry.","Udělal velký skok a přežil."]
        },
    },
    EStoryContext.THEME_MINECRAFT: {
        EPronouns.PRONOUNS_SHE_HER: {
            "start": ["vytvořila nový svět.","se připojila na náhodný server.","se připojila na náhodný realm.","se připojila na holkoklučičárenský SMP."],
            "konec": ["Někdo ji napadl a zabil, a jelikož to byl hardcore, tak se už nevrátí...", "Někdo ji napadl a zabil, a tak se po respawnu pomstila!", "Po nějaké době hraní našla diamanty a teď má hodně diamantových hoes.", "Hrála tak dobře že porazila draka a teď dominuje celému světu.", "Po chvíli jí to přestalo bavit, a tak si šla prstit kundu.", "Snažila se ale nešlo jí to, třeba jí to pujde někdy příště..."]
        },
        EPronouns.PRONOUNS_HE_HIM: {
            "start": ["vytvořil nový svět.","se připojil na náhodný server.","se připojil na náhodný realm.","se připojil na holkoklučičárenský SMP."],
            "konec": ["Někdo ho napadl a zabil, a jelikož to byl hardcore, tak se už nevrátí...", "Někdo ho napadl a zabil, a tak se po respawnu pomstil!", "Po nějaké době hraní našel diamanty a teď má hodně diamantových hoes.", "Hrál tak dobře že porazil draka a teď dominuje celému světu.", "Po chvíli ho to přestalo bavit, a tak si šel honit péro.", "Snažil se ale nešlo mu to, třeba mu to pujde někdy příště..."]
        },
    },
    EStoryContext.THEME_POKEMON: { # Pokemon
      EPronouns.PRONOUNS_SHE_HER: {
          "start": ["se dostala do pokemoního zápasu.", "šla do vysoké trávy a zaútočil na ní divoký pokémon.", "jednoho dne tradovala pokémony.", "měla jednou práci v pokémoním středisku."],
          "konec": ["Když ale viděla že se před ní objevila Lopunny ztratila kontrolu nad svým tělem a udělala nekalé věci :(.", "Když ale viděla že se před ní objevila Gardervoir ztratila kontrolu nad svým tělem a udělala nekalé věci :(.", "Když ale viděla že se před ní objevil Machamp ztratila kontrolu nad svým tělem a udělala nekalé věci :(.", "Když ale viděla že se před ní objevil Vaporeon ztratila kontrolu nad svým tělem a udělala nekalé věci :(.", "Když ale viděla že se před ní objevil Leafeon tak si řekla \"Zakra to je cool pokemon!\".", "Když ale viděla že se před ní objevil Incineroar tak si řekla \"Zakra to je cool pokemon!\".", "Když ale viděla že se před ní náhle objevil Pokemoní bůh Arceus tak si řekla \"DOPRDELE BŮH EXISTUJE A JE TU ABY SOUDIL MÉ HŘÍCHY!!!!!!\".", "Když viděla že se před nim objevil Tandemaus tak si řekla \"No to je fakt boring Pokemon...\"."]
      },
      EPronouns.PRONOUNS_HE_HIM: {
          "start": ["se dostal do pokemoního zápasu.", "šel do vysoké trávy a zaútočil na něj divoký pokémon.", "jednoho dne tradoval pokémony.", "měl jednou práci v pokémoním středisku."],
          "konec": ["Když ale viděl že se před ním objevila Lopunny ztratil kontrolu nad svým tělem a udělal nekalé věci :(.", "Když ale viděl že se před ním objevila Gardervoir ztratil kontrolu nad svým tělem a udělal nekalé věci :(.", "Když ale viděl že se před ním objevil Machamp ztratil kontrolu nad svým tělem a udělal nekalé věci :(.", "Když ale viděl že se před ním objevil Vaporeon ztratil kontrolu nad svým tělem a udělal nekalé věci :(.", "Když ale viděl že se před nim objevil Leafeon tak si řekl \"Zakra to je cool pokemon!\".", "Když ale viděl že se před nim objevil Incineroar tak si řekl \"Zakra to je cool pokemon!\".", "Když ale viděl že se před nim náhle objevil Pokemoní bůh Arceus tak si řekl \"DOPRDELE BŮH EXISTUJE A JE TU ABY SOUDIL MÉ HŘÍCHY!!!!!!\".", "Když viděl že se před nim objevil Tandemaus tak si řekl \"No to je fakt boring Pokemon...\"."]
      },
    },
    EStoryContext.THEME_TRAIN: { # Vlaky
      EPronouns.PRONOUNS_SHE_HER: {
          "start": ["jednou jela vlakem IC 515 Pendolino.", "jednou jela vlakem R926 Krakonoš.", "jednou jela vlakem R756 Berounka.", "jednou jela vlakem Os 7602.", "jednou jela vlakem R604 Krušnohor."],
          "konec": ["Bohužel někdo spadl pod vlak, což vedlo ke 40-minutovému zpoždění.", "Naneštěstí správa železnic něco pojebala což vedlo ke 30-minutovému zpoždění.", "Kvůli polskému kamionu na přejezdu se vlak o 25 minut zpozdil.", "Bohužel tvoje máma zalehla trať takže musela jet náhradní autobusovou dopravou.", "Měla velké štěstí a její vlak jel na čas."]
      },
      EPronouns.PRONOUNS_HE_HIM: {
          "start": ["jednou jel vlakem IC 515 Pendolino.", "jednou jel vlakem R926 Krakonoš.", "jednou jel vlakem R756 Berounka.", "jednou jel vlakem Os 7602.", "jednou jel vlakem R604 Krušnohor."],
          "konec": ["Bohužel někdo spadl pod vlak, což vedlo ke 40-minutovému zpoždění.", "Naneštěstí správa železnic něco pojebala což vedlo ke 30-minutovému zpoždění.", "Kvůli polskému kamionu na přejezdu se vlak o 25 minut zpozdil.", "Bohužel tvoje máma zalehla trať takže musel jet náhradní autobusovou dopravou.", "Měl velké štěstí a jeho vlak jel na čas."]
      },
    },
    EStoryContext.THEME_WORLDOFTANKS: {
        EPronouns.PRONOUNS_SHE_HER: {
            "start": ["zkusila hrát wargames s Napoleonem.", "zapomněla dojít na CW v jejím klanu.", "dostala ammorack za full od E 100 s velkým dělem.", "hrála hulldowny proti Chiefovi.", "nestřílela HEATy proti 279ce.", "neprobila ránu do spodního plátu 907.", "netrefila kupoli 277 v hulldownu.", "potkala Kajzooa v 268/4.", "dostala od artyny za 700."],
            "konec": ["Dostala zápal na první dobrou, a její řepa vyletěla do oblak.", "Bloknul jí spoluhráč a tak dostala ránu navíc.", "Spoluhráč jí vypushoval před tři TDčka.", "Focusla jí nepřátelská artyna a tak měla celou hru permastun.", "Posralo jí RNG, a tak ragequitla bitvu."]
        },
        EPronouns.PRONOUNS_HE_HIM: {
            "start": ["zkusil hrát wargames s Napoleonem.", "zapomněl dojít na CW v jeho klanu.", "dostal ammorack za full od E 100 s velkým dělem.", "hrál hulldowny proti Chiefovi.", "nestřílel HEATy proti 279ce.", "neprobil ránu do spodního plátu 907.", "netrefil kupoli 277 v hulldownu.", "potkal Kajzooa v 268/4.", "dostal od artyny za 700."],
            "konec": ["Dostal zápal na první dobrou, a jeho řepa vyletěla do oblak.", "Bloknul ho spoluhráč a tak dostal ránu navíc.", "Spoluhráč ho vypushoval před tři TDčka.", "Focusla ho nepřátelská artyna a tak měl celou hru permastun.", "Posralo ho RNG, a tak ragequitnul bitvu."]
        },
    },
    EStoryContext.THEME_WARHAMMER: {
        EPronouns.PRONOUNS_SHE_HER: {
            "start": ["jednou hrála Warhammer 40K za Space Marines.", "jednou hrála Warhammer 40K za Adeptus Mechanicus.", "jednou hrála Warhammer 40K za Imperial Guard.", "jednou hrála Warhammer 40K za Adeptus Custodes.", "jednou hrála Warhammer 40K za Imperial Knights.", "jednou hrála Warhammer 40K za Imperial Knights.", "jednou hrála Warhammer 40K za Adeptus Sororitas", "jednou hrála Warhammer 40K za Orky.", "jednou hrála Warhammer 40K za Eldary.", "jednou hrála Warhammer 40K za Drukhari.", "jednou hrála Warhammer 40K za Harlequins.", "jednou hrála Warhammer 40K za Genestealer cults.", "jednou hrála Warhammer 40K za Necrony.", "jednou hrála Warhammer 40K za Tau Empire.", "jednou hrála Warhammer 40K za Tyranidy.", "jednou hrála Warhammer 40K za Leagues of Votann.", "jednou hrála Warhammer 40K za Chaos Space Marines.", "jednou hrála Warhammer 40K za Death Guard.", "jednou hrála Warhammer 40K za World Eaters.", "jednou hrála Warhammer 40K za Emperors Children.", "jednou hrála Warhammer 40K za Thousand Sons.", "jednou hrála Warhammer 40K za Chaos Demons.", "jednou hrála Warhammer 40K za Chaos Knights."],
            "konec": ["Díky své strategické mysli dala své jednotky do perfektních pozic a absolutně zničila protivníkovo armádu.", "Díky své strategické mysli se jí povedlo zabrat control pointy a vyhrála tak na více bodů.", "I přes tvrdý boj si náhle ona a její protivník uvědomili že boj skončil remízou protože se ani jeden nesoustředil na control points a side objectivy.", "Bohužel se jí nepovedlo zabrat control pointy a prohrála na body.", "Naneštěstí její protivník hrál za Space Marines takže ji dostal díky armádě která má dostupné jednotky na téměř každou situaci.", "Naneštěstí její protivník hrál za Adeptus Mechanicus a přestože měl přehnaně komplikovaná pravidla využil všechno ve svém arsenálu perfektně a zdemoloval její armádu.", "Naneštěstí její protivník hrál za Imperial Guard sice ztratil hodně vojáků ale jeho artillery její armádu zničil.", "Naneštěstí její protivník hrál za Adeptus Custodes takže i přes armádu s malým počtem jednotek ji dostal přes lepší staty.", "Naneštěstí její protivník hrál za Imperial Knights takže ji s obříma robotama nakopal prdel.", "Naneštěstí její protivník hrál za Adeptus Sororitas a s hromadou plamenometů jí uškvařil armádu.", "Naneštěstí její protivník hrál za Orky a i přesto že jeho strategie nedávala smysl tak s ní udělal úspešný charge a zničil její armádu.", "Naneštěstí její protivník hrál za Eldary a s mixem vozidel a Psychických schopností vyhrál.", "Naneštěstí její protivník hrál za Drukhary a díky jednotkám s vysokou mobilitou a damagem vyhrál.", "Naneštěstí její protivník hrál za Harlequins a díky na oko neviditelné rychlosti vyhrály bitvu.", "Naneštěstí její protivník hrál za Necrony a díky schopnosti reanimace jejich ztráty byly minimální a vyhráli.", "Naneštěstí její protivník hrál za Tyranidy a hladová masa vesmírných brouků sežrala její armádu.", "Naneštěstí její protivník hrál za Genestealer cults a rebelující kult čtyř rukého císaře díky strojům na těžení vyhrál.", "Naneštěstí její protivník hrál za Tau a za lepší dobro s velkými Mech suits rozestřílel její armádu.", "Naneštěstí její protivník hrál za Leagues of Votann a společně s vesmírnými kapitalistickými trpaslíky změnili její armádu na šrot který prodali.", "Naneštěstí její protivník hrál za Chaos Spacemarines a její armáda se stala obětinnou pro bohy Chaosu.", "Naneštěstí její protivník hrál za Death Guard a s požehnání Boha Nurgla její rány téměř nic nedělali a prohrála.", "Naneštěstí její protivník hrál za World Eaters a když se Khorne Berserkers dostali do melee tak byla brutálně zmasakrována.", "Naneštěstí její protivník hrál za Emperors Children a její armáda byla znechucena pro bohyni/boha excese a chtíče Slaneeshe.", "Naneštěstí její protivník hrál za Thousand Sons a její armáda byla proměněna v prach s pomocí Psychických schopností.", "Naneštěstí její protivník hrál za Chaos Demons a armáda Démonů všech čtyř bohů chaosu její armádu poslala přímo do pekla.", "Naneštěstí její protivník hrál za Chaos Knights zmasakroval její armádu s obřímy roboty ve jménu Chaosu."]
        },
        EPronouns.PRONOUNS_HE_HIM: {
            "start": ["jednou hrál Warhammer 40K za Space Marines.", "jednou hrál Warhammer 40K za Adeptus Mechanicus.", "jednou hrál Warhammer 40K za Imperial Guard.", "jednou hrál Warhammer 40K za Adeptus Custodes.", "jednou hrál Warhammer 40K za Imperial Knights.", "jednou hrál Warhammer 40K za Imperial Knights.", "jednou hrál Warhammer 40K za Adeptus Sororitas", "jednou hrál Warhammer 40K za Orky.", "jednou hrál Warhammer 40K za Eldary.", "jednou hrál Warhammer 40K za Drukhari.", "jednou hrál Warhammer 40K za Harlequins.", "jednou hrál Warhammer 40K za Genestealer cults.", "jednou hrál Warhammer 40K za Necrony.", "jednou hrál Warhammer 40K za Tau Empire.", "jednou hrál Warhammer 40K za Tyranidy.", "jednou hrál Warhammer 40K za Leagues of Votann.", "jednou hrál Warhammer 40K za Chaos Space Marines.", "jednou hrál Warhammer 40K za Death Guard.", "jednou hrál Warhammer 40K za World Eaters.", "jednou hrál Warhammer 40K za Emperors Children.", "jednou hrál Warhammer 40K za Thousand Sons.", "jednou hrál Warhammer 40K za Chaos Demons.", "jednou hrál Warhammer 40K za Chaos Knights."],
            "konec": ["Díky své strategické mysli dal své jednotky do perfektních pozic a absolutně zničil protivníkovo armádu.", "Díky své strategické mysli se mu povedlo zabrat control pointy a vyhrál tak na více bodů.", "I přes tvrdý boj si náhle on a její protivník uvědomili že boj skončil remízou protože se ani jeden nesoustředil na control points a side objectivy.", "Bohužel se mu nepovedlo zabrat control pointy a prohrála na body." "Naneštěstí jeho protivník hrál za Space Marines takže ho dostal díky armádě která má dostupné jednotky na téměř každou situaci.", "Naneštěstí jeho protivník hrál za Adeptus Mechanicus a přestože měl přehnaně komplikovaná pravidla využil všechno ve svém arsenálu perfektně a zdemoloval jeho armádu.", "Naneštěstí jeho protivník který hrál za Imperial Guard sice ztratil hodně vojáků ale artillery jeho armádu zničil.", "Naneštěstí jeho protivník hrál za Adeptus Custodes takže i přes armádu s malým počtem jednotek ho dostal přes lepší staty.", "Naneštěstí jeho protivník který hrál za Imperial Knights takže mu s obříma robotama nakopal prdel.", "Naneštěstí jeho protivník hrál za Adeptus Sororitas a s hromadou plamenometů mu uškvařil armádu.", "Naneštěstí jeho protivník hrál za Orky a i přesto že jeho strategie nedávala smysl tak s ní udělal úspešný charge a zničil mu armádu.", "Naneštěstí jeho protivník hrál za Eldary a s mixem vozidel a Psychických schopností vyhrál.", "Naneštěstí jeho protivník hrál za Drukhary a díky jednotkám s vysokou mobilitou a damagem vyhrál.", "Naneštěstí jeho protivník hrál za Harlequins a díky na oko neviditelné rychlosti vyhrál bitvu.", "Naneštěstí jeho protivník hrál za Necrony a díky schopnosti reanimace jejich ztráty byly minimální a vyhráli.", "Naneštěstí jeho protivník hrál za Tyranidy a hladová masa vesmírných brouků sežrala jeho armádu.", "Naneštěstí jeho protivník hrál za Genestealer cults a rebelující kult čtyř rukého císaře se stroji na těžení vyhrál.", "Naneštěstí jeho protivník hrál za Tau a za lepší dobro s velkými Mech suits rozestřílely jeho armádu.", "Naneštěstí jeho protivník hrál za Leagues of Votann a společně s vesmírnými kapitalistickými trpaslíky změnil jeho armádu na šrot který prodali.", "Naneštěstí jeho protivník hrál za Chaos Spacemarines a jeho armáda se stala obětinnou pro bohy Chaosu.", "Naneštěstí jeho protivník hrál za Death Guard a s požehnání Boha Nurgla jeho rány téměř nic nedělali a prohrál.", "Naneštěstí jeho protivník hrál za World Eaters a když se Khorne Berserkers dostali do melee tak byl brutálně zmasakrován.", "Naneštěstí jeho protivník hrál za Emperors Children a jeho armáda byla znechucena pro bohyni/boha excese a chtíče Slaneeshe.", "Naneštěstí jeho protivník hrál za Thousand Sons a jeho armáda byla proměněna v prach s pomocí Psychických schopností.", "Naneštěstí jeho protivník hrál za Chaos Demons a armáda Démonů všech čtyř bohů chaosu jeho armádu poslala přímo do pekla.", "Naneštěstí jeho protivník který hrál za Chaos Knights zmasakroval jeho armádu s obřímy roboty ve jménu Chaosu."],
        },
    },
    }

    postavy = {
        EPronouns.PRONOUNS_SHE_HER: ["Pavlí", "Lena", "Adélka", "Fena", "Markétka"],
        EPronouns.PRONOUNS_HE_HIM: ["Šéf", "Archie", "Péťa", "Džimmy", "Fanoušek", "Skyyf", "Ol*a", "Pavlí"],
        EPronouns.PRONOUNS_RANDOM: ["Kiki", "R926 Krakonoš(ka)", "Kapitán(ka)"]
    }

    # náhodně vybereme z náhodného výběru joooo
    # tohle je peak programování tak na to nešmatlej
    postava = choice(choice(list(postavy.values())))
    pronouns = postava_to_pronouns(postavy, postava)

    while pronouns == EPronouns.PRONOUNS_RANDOM:
        pronouns = choice(list(EPronouns))

    start = choice(hra[story_context][pronouns]["start"])
    end = choice(hra[story_context][pronouns]["konec"])

    return (postava + " " + start + " " + end)
