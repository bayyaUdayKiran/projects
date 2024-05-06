import random
from time import sleep

if __name__ == "__main__":
    swaras = ["Shadjam[Sa]", "Rishabham[Re]", "Gandharam[Ga]", "Madhyamam[Ma]", "Panchamam[Pa]", "Dhaivatam[Da]", "Nishadam[Ni]", "Shadjam[Sa*`]"]
    max = len(swaras) - 1
    while(True):
        print(swaras[random.randint(0, max)])
        sleep(7)

   
    