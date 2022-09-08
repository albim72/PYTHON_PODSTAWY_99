#import dane
#import dane as dn
from dane import osoba
from moje_funkcje import witaj,px
#from miasto import Miasto
from stolica import Stolica,Miasto

print(osoba)
print(witaj("Tomasz"))

print(px(4,7))

ms = Miasto(34,"Toruń","kujawsko-pomorskie")
ms.print_miasto()

st = Stolica(1,"Warszawa","mazowieckie","Jan Kot")
st.print_miasto()
print(st.prezydentinfo())
