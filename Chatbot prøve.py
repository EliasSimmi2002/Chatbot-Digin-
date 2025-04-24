def vis_kategorier():
    print("Velg en kategori:")
    print("1. Digital utvikling og programvare:")
    print("2. IT-infrastruktur og teknologi:")
    print("3. Digital transformasjon og rådgivning:")

def selskaper_for_teknologi(kategori):
    selskaper = {
        "Digital utvikling og programvare": ["Anzyz Technologies", "Advantek", "Appsens"],
        "IT-infrastruktur og teknologi": ["Atea", "Altidata", "Bitpro"],
        "Digital transformasjon og rådgivning": ["Abacus", "Avinto", "Alette Lie Consultancy"]
    }
    return selskaper.get(kategori, [])

def hovedprogram():
    while True:
        vis_kategorier()
        valg = input("Skriv inn nummeret på kategorien du vil velge (eller 'q' for å avslutte): ").strip()
        
        if valg.lower() == 'q':
            print("Avslutter programmet. Ha en fin dag!")
            break

        if valg == "1":
            kategori = "Digital utvikling og programvare"
        elif valg == "2":
            kategori = "IT-infrastruktur og teknologi"
        elif valg == "3":
            kategori = "Digital transformasjon og rådgivning"
        else:
            print("Ugyldig valg. Vennligst velg et nummer mellom 1 og 3, eller 'q' for å avslutte.")
            continue

        selskaper = selskaper_for_teknologi(kategori)
        print(f"Selskaper i kategorien {kategori}:")
        for selskap in selskaper:
            print(f"- {selskap}")
        print()  

if __name__ == "__main__":
    hovedprogram()