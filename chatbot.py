import sqlite3

def vis_kategorier():
    print("Velg en kategori:")
    print("1. Helse")
    print("2. Utdanning")
    print("3. Offentlig_sektor")
    print("4. IT_infrastruktur")
    print("5. Sikkerhet")
    print("6. Digitalisering")
    print("7. Geodata")
    print("8. Industri")
    print("9. E_handel")
    print("10. Media")
    print("11. Finans")
    print("12. Innovasjon")
    print("13. Logistikk")

def selskaper_for_teknologi(kategori):
    tillatte_tabeller = [
        "Helse", "Utdanning", "Offentlig_sektor", "IT_infrastruktur",
        "Sikkerhet", "Digitalisering", "Geodata", "Industri",
        "E_handel", "Media", "Finans", "Innovasjon", "Logistikk"
    ]
    if kategori not in tillatte_tabeller:
        raise ValueError(f"Ugyldig kategori: {kategori}")

    conn = sqlite3.connect('selskaper.db')
    cursor = conn.cursor()
    query = f"SELECT navn FROM {kategori}"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return [row[0] for row in result]

def hovedprogram():
    kategorier = [
        "Helse",
        "Utdanning",
        "Offentlig_sektor",
        "IT_infrastruktur",
        "Sikkerhet",
        "Digitalisering",
        "Geodata",
        "Industri",
        "E_handel",
        "Media",
        "Finans",
        "Innovasjon",
        "Logistikk",
    ]

    while True:
        vis_kategorier()
        valg = input("Skriv inn nummeret på kategorien du vil velge (eller 'q' for å avslutte): ").strip()
        
        if valg.lower() == 'q':
            print("Avslutter programmet. Ha en fin dag!")
            break

        try:
            kategori = kategorier[int(valg) - 1]
        except (ValueError, IndexError):
            print("Ugyldig valg. Vennligst velg et nummer fra listen, eller 'q' for å avslutte.")
            continue

        selskaper = selskaper_for_teknologi(kategori)
        if not selskaper:
            print(f"Ingen selskaper funnet i kategorien {kategori}.")
            continue

        print(f"Selskaper i kategorien {kategori}:")
        for selskap in selskaper:
            print(f"- {selskap}")
        print()

if __name__ == "__main__":
    hovedprogram()