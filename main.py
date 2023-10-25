from pywebio.input import input as pw_input
from pywebio.output import put_success

favorite_food = pw_input('Введіть улюблену страву >>>').lower()
smile = '\U0001F958'
summa = f"О, я теж люблю {favorite_food} {smile}"
put_success(summa)
