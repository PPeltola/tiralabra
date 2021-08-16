13.8.

Tällä viikolla en ehtinyt tekemään projektia kuin yhtenä päivänä, mutta sain implementoitua backpropagationin! Toki implementaatio ei varmasti ole täydellinen, mutta se toimii: sain mahdllisimman yksinkertaisella kymmenen neuronin ja vain yhden kerroksen kokeilulla osumaprosentiksi 87.87! Tässä mallissakin on vielä paljon puutteita, se ei mm. muuta neuronien biasta (vakiotermi), enkä kouluttanut sitä kuin yhden koulutusdatan iteraation verran. Tein myös toiminnallisuuden jolla eri neuronien painot pystyy visualisoimaan, sillä ajattelin että yhden kerroksen kymmenen neuronin mallissa eri neuroninen painot varmaankin myötäilisivät niiden vastuulla olevan numeron ääriviivoja. Visualisointi ei siis oikein edes toimi muille kuin input-kerrokselle, sillä vain siinä jokainen paino vastaa suoraan yhtä pikseliä.

Ensi viikolla kokeilen useamman kerroksen malleja, mutta uskon että törmään niissä suorituskykyhaasteisiin ja matriisien implentoinnin tarpeeseen.

Tässä ovat eri numeroita tunnistavien neuronien painot kuvaamastani karvalakkimallista visualisoituna, tummempi pikseli tarkoittaa negatiivista painoa kyseiselle pikselille ja vaalea positiivista painoa:

### Nolla
<img src="kuvat/vk4/w0.png" align="left" height="140" width="140" >


### Yksi
<img src="kuvat/vk4/w1.png" align="left" height="140" width="140" >


### Kaksi
<img src="kuvat/vk4/w2.png" align="left" height="140" width="140" >


### Kolme
<img src="kuvat/vk4/w3.png" align="left" height="140" width="140" >


### Neljä
<img src="kuvat/vk4/w4.png" align="left" height="140" width="140" >


### Viisi
<img src="kuvat/vk4/w5.png" align="left" height="140" width="140" >


### Kuusi
<img src="kuvat/vk4/w6.png" align="left" height="140" width="140" >


### Seitsemän
<img src="kuvat/vk4/w7.png" align="left" height="140" width="140" >


### Kahdeksan
<img src="kuvat/vk4/w8.png" align="left" height="140" width="140" >


### Yhdeksän
<img src="kuvat/vk4/w9.png" align="left" height="140" width="140" >


Tällä viikolla käytin aikaa projektiin n. 6 tuntia
