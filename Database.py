import sqlite3

def opprett_database():
    conn = sqlite3.connect('selskaper.db')
    cursor = conn.cursor()
    
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
    
    for kategori in kategorier:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS "{kategori}" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            navn TEXT NOT NULL
        )
        """)

    selskaper = {
        "Helse": [
            "Aiveo", "Appsens", "I4Helse", "Sørlandet sykehus", "Varde Tech", "DiagraphIT", "Unilabs", "Invivo", "Alma", "Helse Nord"
        ],
        "Utdanning": [
            "Noroff", "Norsk Interaktiv", "Vivid-Edtech", "Moava", "OKOS Agder", "Universitetet i Agder"
        ],
        "Offentlig_sektor": [
            "Agder Fylkeskommune", "Arendal kommune", "Kristiansand kommune", "Lillesand kommune", "Sikri", "Statens Kartverk", "Norkart", "Norske Film", "Sandnes kommune"
        ],
        "IT_infrastruktur": [
             "Atea", "Altidata", "Bulk Infrastructure", "Nordlo", "Iteam", "Phonero", "P-Lindberg", "Aksess IT", "Fujitsu", "Avinor", "Telenor", "Smartme", "Telenor Group", "Hjorth Digital", "Telenor Business", "Mellomdalen", "Exelcom", "Gigant", "Aqeri"
        ],
        "Sikkerhet": [
            "Telenor Cyberdefence", "Defendable", "ForSec", "Netsecurity", "ZignSec", "F-secure", "Securitas"
        ],
        "Digitalisering": [
            "Bouvet", "Crayon", "Dfind Consulting", "Egde Consulting", "Experis",
            "Sopra Steria", "Tietoevry", "Webstep", "Xledger", "Visma", "Tibber",
            "Digital Norway", "Knowit", "Metier OEC", "Eventum", "KPMG", "Accenture",
            "Deloitte", "PwC", "Evry", "Invenia", "Sopra Banking Software",
            "Infranode", "TietoEvry", "Kongsberg Digital", "Bekk", "Kantega",
            "Crayon", "Accenture Norge", "Tietoevry", "Ingage", "Kantar", "Wipro",
            "Microsoft", "Atos", "Optimeering", "Stravito"
        ],
        "Geodata": [
            "StormGeo", "Steerpath", "Hexagon", "Klimator", "Norkart"
        ],
        "Industri": [
            "Vår Energi", "Rambøll", "Veidekke", "Kongsberg Gruppen", "Odfjell Drilling", 
            "Lerøy", "Mesta", "Nederman", "Alfa Laval"
        ],
        "E_handel": [
            "Zalando", "Elkjøp", "H&M", "Arvato", "Mesterbakeren"
        ],
        "Media": [
            "Schibsted", "Edda Media", "Avalanche Studios", "Clear Channel", "Norsk Rikskringkasting"
        ],
        "Finans": [
            "Nordea", "DNB", "IF", "Lindorff", "Swedbank"
        ],
        "Innovasjon": [
            "The Factory", "Drivhus", "Technoport", "Enova", "Briskr", "Løvenskiold Handel", "Solon Eiendom"
        ],
        "Logistikk": [
            "Lerøy Seafood Group", "Kongsberg Gruppen", "Mesta"
        ]
    }

    for kategori, selskap_liste in selskaper.items():
        for selskap in selskap_liste:
            cursor.execute(f'INSERT INTO "{kategori}" (navn) VALUES (?)', (selskap,))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    opprett_database()
    print("Databasen og tabellene er opprettet!")