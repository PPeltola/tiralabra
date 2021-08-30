30.8.

Tällä viikolla kokeilin rakentaa monikerroksista verkkoa, ja kohtasin siinä jonkin verran haasteita. Suorituskyky vaikutti ensin olevan suurin este, mutta pienen optimoinnin ja pypy-tulkin avulla pystyn käyttämään nykyistä vain vektoreita hyödyntävää implementaatiota melko hyvin. Varsinkin pypy-tulkki vaikutti asiaan, sillä se n. kymmenkertaisti verkon kouluttamisen nopeuden.

Sain mielestäni backpropagationin toimimaan oikein monen kerroken verkossa, mutta tällä hetkellä verkko ei tunnu kouluttuvan aivan halutulla tavalla. Verkko ei kouluttuessa vain kasva tarkkuudessa, vaan tarkkuus saattaa heitellä myös alaspäin. Parhammillaan verkko on yltänyt n. 70% tarkkuuteen, mutta tarkkuuden eteneminen koulutussyklien myötä vaikuttaa jokseenkin satunnaiselta. Uskon että saan ongelman ratkaistua ns. batchingillä, eli muuttamalla koulutuksen kuvakohtisesta syklistä joukon kuvia kerralla ajavaksi. Myös dynaaminen oppimisnopeuden säätö (aluksi suurempi, myöhemmillä sykleillä pienenevä) on käsittääkseni mahdollinen apu tähän, ajattelin kokeilla sitäkin.

Tarkoituksenani oli tällä viikolla siistiä koodia, dokumentoida projektia sekä testata niitä osia joit on mielekästä testata. En kuitenkaan ehtinyt niin pitkälle, joten joudun tekemään nuo nyt viimeisellä viikolla.

Tällä viikolla käytin aikaa projektiin n. 9 tuntia.
