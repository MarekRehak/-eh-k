class Zamestnanec:
    def __init__(self, jmeno, plat):
        # Místo přímého zápisu do _jmeno a _plat použijeme rovnou naše settery.
        # Díky tomu se pravidla zkontrolují hned při vytváření zaměstnance.
        self.jmeno = jmeno  
        self.plat = plat    

    # --- ZAPOUZDŘENÍ JMÉNA ---

    @property
    def jmeno(self):
        """Vrátí jméno zaměstnance."""
        return self._jmeno

    @jmeno.setter
    def jmeno(self, nove_jmeno):
        """Nastaví nové jméno, ale zkontroluje, že není prázdné a jde o text."""
        if not isinstance(nove_jmeno, str) or nove_jmeno.strip() == "":
            raise ValueError("Chyba: Jméno nesmí být prázdné a musí to být text!")
        
        # Uložíme očištěné jméno (bez mezer na začátku a na konci) do protected atributu
        self._jmeno = nove_jmeno.strip()

    # --- ZAPOUZDŘENÍ PLATU ---

    @property
    def plat(self):
        """Vrátí aktuální plat zaměstnance."""
        return self._plat

    @plat.setter
    def plat(self, nova_hodnota):
        """Změní plat, ale pohlídá, aby neklesl pod minimum."""
        if nova_hodnota < 30000:
            raise ValueError(f"Chyba: Plat nesmí klesnout pod 30 000 Kč! (Zadáno: {nova_hodnota})")
        
        self._plat = nova_hodnota


# --- Jak to vypadá v praxi ---

# Vytvoříme zaměstnance (zde projdou obě kontroly z __init__)
pepa = Zamestnanec("Josef Novák", 40000)
print(f"Zaměstnanec: {pepa.jmeno}, Plat: {pepa.plat} Kč")

# Můžeme jméno normálně změnit, pokud je platné
pepa.jmeno = "Josef Novák starší"
print(f"Nové jméno: {pepa.jmeno}")

# POKUS O CHYBU VE JMÉNĚ:
# Pokud se někdo pokusí jméno vymazat, setter ho zastaví.
try:
    pepa.jmeno = "   "  # Jen prázdné mezery
except ValueError as chyba:
    print(chyba)

# POKUS O CHYBU PŘI VYTVÁŘENÍ:
# Tady to spadne hned na začátku, protože už v __init__ se volá kontrola platu.
try:
    karel = Zamestnanec("Karel", 15000)
except ValueError as chyba:
    print(f"Nepodařilo se vytvořit Karla: {chyba}")
