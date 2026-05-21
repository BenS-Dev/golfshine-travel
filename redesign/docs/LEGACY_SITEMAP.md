# Legacy Sitemap Audit — Wingolf Travel

Every numbered `.php` file in `sitepro/` mapped to its content, title, and coverage status in the redesign. Used to verify nothing was missed.

## Status legend

- ✓ **Covered** — has a dedicated detail page in the redesign
- ⤴ **Consolidated** — represented within a hub page (LOCATION – COURSE / HOTEL pair on a region detail page, or anchored section). Click-through still works via the searchable atlas.
- ▲ **Hub replaced** — was a hub/menu page in legacy; its function is now handled by a redesigned catalog (e.g. `visit-argentina.html`, `golf.html`, `destinations.html`).
- 🆕 **New** — added in this audit pass (Argentina 6-Night programs, Argentina Golf combos).
- 🗑 **Junk** — empty legacy page (title `Nueva Página` with no body content) or duplicate/mislabeled — legitimately skipped.

## All 170 legacy pages

| # | Legacy title | Status | Maps to |
|---|---|---|---|
| 1 | Home | ▲ | `index.html` |
| 2 | Bariloche | ✓ | `argentina/bariloche.html` |
| 3 | Contacts | ▲ | `contact.html` |
| 4 | BUENOS AIRES 4 days, 3 nights | ✓ | `argentina/buenos-aires.html` |
| 5 | Argentina 3 Nights menu | ▲ | tier section on `visit-argentina.html#tier-3` |
| 6 | Salta | ✓ | `argentina/salta.html` |
| 7 | Ushuaia | ✓ | `argentina/ushuaia.html` |
| 8 | El Calafate (title says "Salta" — mislabeled in source) | ✓ | `argentina/el-calafate.html` |
| 9 | Puerto Madryn | ✓ | `argentina/puerto-madryn.html` |
| 10 | Iguazú | ✓ | `argentina/iguazu.html` |
| 11 | Bariloche Golf | ✓ | `argentina-golf/bariloche.html` |
| 12 | Bariloche 6 Noches | 🆕 | `argentina/bariloche-6-nights.html` |
| 13 | Argentina 6 Noches menu | ▲ | tier section on `visit-argentina.html#tier-6` |
| 14 | Cordoba Golf | ✓ | `argentina-golf/cordoba.html` |
| 15 | Iguazú 6N | 🆕 | `argentina/iguazu-6-nights.html` |
| 16 | El Calafate 6N | 🆕 | `argentina/el-calafate-6-nights.html` |
| 17 | Puerto Madryn 6N | 🆕 | `argentina/puerto-madryn-6-nights.html` |
| 18 | Ushuaia 6N | 🆕 | `argentina/ushuaia-6-nights.html` |
| 19 | Argentina 13 Nights menu | ▲ | tier section on `visit-argentina.html#tier-13` |
| 20 | BA-Iguazú-Ushuaia-El Calafate (13N) | ✓ | `argentina/buenos-aires-iguazu-ushuaia-calafate.html` |
| 21 | BA-Iguazú-Bariloche-Calafate (13N) | ✓ | `argentina/buenos-aires-iguazu-bariloche-calafate.html` |
| 22 | BA-Iguazú-Puerto Madryn-El Calafate (13N) | ✓ | `argentina/buenos-aires-iguazu-puerto-madryn-calafate.html` |
| 23 | Argentina 16 Nights menu | ▲ | tier section on `visit-argentina.html#tier-16` |
| 24 | BA-Iguazú-Puerto Madryn-Ushuaia-El Calafate (16N) | ✓ | `argentina/buenos-aires-iguazu-puerto-madryn-ushuaia-calafate.html` |
| 25 | Argentina hub | ▲ | `visit-argentina.html` |
| 26 | BA-Puerto Madryn-Ushuaia-El Calafate-Bariloche (16N) | ✓ | `argentina/buenos-aires-puerto-madryn-ushuaia-calafate-bariloche.html` |
| 27 | BA-Iguazú-El Calafate-Ushuaia-Crucero Australis (16N) | ✓ | `argentina/buenos-aires-iguazu-calafate-ushuaia-australis.html` |
| 28 | Golf en Argentina hub | ▲ | Argentina Golf tier on `visit-argentina.html#tier-golf` |
| 29 | Mendoza Golf | ✓ | `argentina-golf/mendoza.html` |
| 30 | Buenos Aires Golf | ✓ | `argentina-golf/buenos-aires.html` |
| 31 | Mar del Plata | 🗑 | Legacy content is duplicated Ushuaia (mislabeled). Tile on `visit-argentina.html` routes to contact prefill. |
| 32 | Ushuaia Golf | ✓ | `argentina-golf/ushuaia.html` |
| 33 | BA & El Calafate Golf | 🆕 | `argentina-golf/buenos-aires-el-calafate.html` |
| 34 | BA & Iguazú Golf | 🆕 | `argentina-golf/buenos-aires-iguazu.html` |
| 35 | BA & Ushuaia Golf | 🆕 | `argentina-golf/buenos-aires-ushuaia.html` |
| 36 | Bariloche & San Martin de los Andes | 🆕 | `argentina-golf/bariloche-san-martin.html` |
| 37 | BA-Iguazú-Bariloche-El Calafate (golf 16N) | 🆕 | `argentina-golf/ba-iguazu-bariloche-calafate.html` |
| 38 | BA-Iguazú-Puerto Madryn-El Calafate (golf 16N) | 🆕 | `argentina-golf/ba-iguazu-puerto-madryn-calafate.html` |
| 39 | BA-Iguazu-Ushuaia-El Calafate (golf 16N) | 🆕 | `argentina-golf/ba-iguazu-ushuaia-calafate.html` |
| 40 | BA-Iguazu-Puerto Madryn-El Calafate-Bariloche (golf 22N) | 🆕 | `argentina-golf/ba-iguazu-pm-calafate-bariloche.html` |
| 41 | BA-Iguazú-Puerto Madryn-Ushuaia-El Calafate (golf 19N) | 🆕 | `argentina-golf/ba-iguazu-pm-ushuaia-calafate.html` |
| 42 | BA-Iguazu-El Calafate-Ushuaia-Australis Cruise (golf 19N) | 🆕 | `argentina-golf/ba-iguazu-calafate-ushuaia-australis.html` |
| 43 | Buenos Aires (Request Pricing form) | ▲ | `contact.html` |
| 44 | "asdasd" | 🗑 | Test page, no real content |
| 45 | England (content is Italy duplicate) | 🗑 | England tile on `golf.html` routes to contact prefill. Italy is at `golf/italy.html`. |
| 46 | USA hub | ▲ | USA section on `destinations.html` + `golf.html` |
| 47 | South Carolina (title "Nueva Página") | ▲ | USA filter on `destinations.html` |
| 48 | Baywood-Los Osos (title "Nueva Página") | ✓ | `usa/baywood-los-osos.html` |
| 49 | KIAWAH ISLAND | ✓ | `usa/kiawah-island.html` |
| 50 | MYRTLE BEACH | ✓ | `usa/myrtle-beach.html` |
| 51 | Florida hub | ▲ | Florida tile group on `destinations.html` |
| 52 | DAYTONA | ✓ | `usa/daytona.html` |
| 53 | Miami JW Marriott Turnberry | ✓ | `usa/miami-jw-marriott-turnberry.html` |
| 54 | Naples | ✓ | `usa/naples-greenlinks.html` |
| 55 | Palm Beach PGA National | ✓ | `usa/palm-beach-pga-national.html` |
| 56 | TAMPA | ✓ | `usa/tampa.html` |
| 57 | Orlando Mission Inn | ✓ | `usa/orlando-mission-inn.html` |
| 58 | MIAMI Trump Doral | ✓ | `usa/miami-trump-doral.html` |
| 59 | St Augustine (title "Nueva Página") | ✓ | `usa/st-augustine-world-golf-village.html` |
| 60 | Ponte Vedra Beach TPC Sawgrass | ✓ | `usa/ponte-vedra-tpc-sawgrass.html` |
| 61 | Caribbean hub (title "Nueva Página") | ▲ | Caribbean section on `destinations.html` |
| 62 | Golf Rest of the World hub | ▲ | Region tiles on `golf.html` |
| 63 | Nevada hub | ▲ | Nevada cities on `destinations.html` |
| 64 | Las Vegas (title "Nueva Página") | ✓ | `usa/las-vegas.html` |
| 65 | Mesquite | ✓ | `usa/mesquite.html` |
| 66 | California (Rancho Santa Fe) | ✓ | `usa/rancho-santa-fe.html` |
| 67 | California hub | ▲ | California cities on `destinations.html` |
| 68 | Palm Springs PGA West | ✓ | `usa/palm-springs-pga-west.html` |
| 69 | Maryland hub | ▲ | Maryland tile on `destinations.html` |
| 70 | South Carolina hub | ▲ | S.Carolina section on `destinations.html` |
| 71 | PHOENIX | ✓ | `usa/phoenix-scottsdale.html` |
| 72 | TUCSON | ✓ | `usa/tucson-ritz-carlton.html` |
| 73 | Ocean City Eagle's Landing | ✓ | `usa/ocean-city-eagles-landing.html` |
| 74 | Puerto Rico Wyndham Rio Mar | ✓ | `caribbean/puerto-rico.html` |
| 75 | Punta Cana (Iberostar Bavaro variant) | ⤴ | Combined into `caribbean/punta-cana.html` |
| 76 | Bahamas | ✓ | `caribbean/bahamas.html` |
| 77 | North of Ireland (Royal Portrush variant) | ⤴ | Listed on `golf/ireland.html` |
| 78 | Punta Cana 2 (Westin variant) | ⤴ | Combined into `caribbean/punta-cana.html` |
| 79 | Punta Cana 3 (Westin 4-night) | ⤴ | Combined into `caribbean/punta-cana.html` |
| 80 | Punta Cana (Hard Rock variant) | ⤴ | Combined into `caribbean/punta-cana.html` |
| 81 | Nations Cup | ⤴ | Card on `journeys.html` (links to `contact.html?inquiry=Nations+Cup`) |
| 82 | Los Cabos Diamante | ✓ | `caribbean/los-cabos.html` |
| 83 | Rivera Maya Mayakoba | ✓ | `caribbean/riviera-maya-cancun.html` |
| 84 | Rivera Maya 2 (Cancun) | ⤴ | Combined into `caribbean/riviera-maya-cancun.html` |
| 85 | North Ireland 2 (Ballyliffin) | ⤴ | Listed on `golf/ireland.html` |
| 86 | South West Ireland (Killarney) | ⤴ | Listed on `golf/ireland.html` |
| 87 | South West Ireland 2 (Tralee) | ⤴ | Listed on `golf/ireland.html` |
| 88 | East Ireland (Portmarnock) | ⤴ | Listed on `golf/ireland.html` |
| 89 | East Ireland 2 (Carton House) | ⤴ | Listed on `golf/ireland.html` |
| 90 | St. Andrews (full text in legacy) | ⤴ | Listed on `golf/scotland.html` |
| 91 | St Andrews Old | ⤴ | Listed on `golf/scotland.html` |
| 92 | Scottish H 1 (Cabot Highlands) | ⤴ | Listed on `golf/scotland.html` |
| 93 | Edinburgh | ⤴ | Listed on `golf/scotland.html` |
| 94 | Scottish H 2 (Royal Dornoch) | ⤴ | Listed on `golf/scotland.html` |
| 95 | East Lothian (Gullane) | ⤴ | Listed on `golf/scotland.html` |
| 96 | Royal Troon Golf Club | ⤴ | Listed on `golf/scotland.html` |
| 97 | Trump Turnberry | ⤴ | Listed on `golf/scotland.html` |
| 98 | Aberdeen 2 (Trump International) | ⤴ | Listed on `golf/scotland.html` |
| 99 | Ireland hub | ▲ | `golf/ireland.html` |
| 100 | Aberdeen 1 (Royal Aberdeen) | ⤴ | Listed on `golf/scotland.html` |
| 101 | Scotland hub | ▲ | `golf/scotland.html` |
| 102 | Spain hub | ▲ | `golf/spain.html` |
| 103 | Portugal hub | ▲ | `golf/portugal.html` |
| 104 | La Herrería (Madrid) | ⤴ | Listed on `golf/spain.html` |
| 105 | Los Monteros (Marbella) | ⤴ | Listed on `golf/spain.html` |
| 106 | Marbella 2 (Los Naranjos) | ⤴ | Listed on `golf/spain.html` |
| 107 | Marbella 3 (Rio Real) | ⤴ | Listed on `golf/spain.html` |
| 108 | Barcelona (Sitges Terramar) | ⤴ | Listed on `golf/spain.html` |
| 109 | Barcelona 2 (Llavaneras) | ⤴ | Listed on `golf/spain.html` |
| 110 | Valencia (El Saler) | ⤴ | Listed on `golf/spain.html` |
| 111 | Algarve (Vale do Lobo) | ⤴ | Listed on `golf/portugal.html` |
| 112 | Algarve | ⤴ | Listed on `golf/portugal.html` |
| 113 | Cascais (Oitavos Dunes) | ⤴ | Listed on `golf/portugal.html` |
| 114 | Obidos (Praia d'El Rey) | ⤴ | Listed on `golf/portugal.html` |
| 115 | Lagos (Palmares) | ⤴ | Listed on `golf/portugal.html` |
| 116 | Oporto | ⤴ | Listed on `golf/portugal.html` |
| 117 | Toscana (Argentario) | ⤴ | Listed on `golf/italy.html`. Full-itinerary `italy-tuscany-umbria.html` also covers Tuscany. |
| 118 | Milan (Garrdagolf) | ⤴ | Listed on `golf/italy.html` |
| 119 | Lombardía (Villa d'Este) | ⤴ | Listed on `golf/italy.html`. Also featured in `italy-lake-como.html`. |
| 120 | Italy hub | ▲ | `golf/italy.html` |
| 121 | Sardinia (Pevero) | ⤴ | Listed on `golf/italy.html` |
| 122 | Roma (Circolo del Golf di Roma) | ⤴ | Listed on `golf/italy.html` |
| 123 | Turin (Royal Park Roveri) | ⤴ | Listed on `golf/italy.html` |
| 124 | Norway hub | ▲ | `golf/norway.html` |
| 125 | Oslo (Losby Golfklubb) | ⤴ | Listed on `golf/norway.html` |
| 126 | Stavanger | ⤴ | Listed on `golf/norway.html` |
| 127 | Trondheim | ⤴ | Listed on `golf/norway.html` |
| 128 | Bergen | ⤴ | Listed on `golf/norway.html` |
| 129 | Tønsberg (Vestfold) | ⤴ | Listed on `golf/norway.html` |
| 130 | Drøbak | ⤴ | Listed on `golf/norway.html` |
| 131 | Costa Navarino — Bay Course | ⤴ | Listed on `golf/greece.html` |
| 132 | Costa Navarino — Dunes Course (Westin) | ⤴ | Listed on `golf/greece.html` |
| 133 | Costa Navarino — Dunes (Romanos) / Hørsholm | ⤴ | Listed on `golf/greece.html` and `golf/denmark.html` |
| 134 | Greece hub | ▲ | `golf/greece.html` |
| 135 | France hub | ▲ | `golf/france.html` |
| 136 | Athens (Glyfada) | ⤴ | Listed on `golf/greece.html` |
| 137 | Denmark hub | ▲ | `golf/denmark.html` |
| 138 | Sweden hub | ▲ | `golf/sweden.html` |
| 139 | Netherlands hub | ▲ | `golf/netherlands.html` |
| 140 | Pebble Beach | ✓ | `usa/pebble-beach.html` |
| 141 | Wales hub | ▲ | `golf/wales.html` |
| 144 | Bordeaux (Golf du Medoc) | ⤴ | Listed on `golf/france.html` |
| 145 | Corfú (Corfu Golf Club) | ⤴ | Listed on `golf/greece.html` |
| 146 | Golf hub | ▲ | `golf.html` |
| 147 | Birmingham (England — content is Italy dup) | 🗑 | English region not represented; would need real source content |
| 148 | Punta Cana primary | ✓ | `caribbean/punta-cana.html` |
| 149 | Warwickshire (England — content is Italy dup) | 🗑 | Same as 147 |
| 151 | Lincolnshire (England — content is Italy dup) | 🗑 | Same as 147 |
| 152 | Evian-les-Bains | ⤴ | Listed on `golf/france.html` |
| 153 | Tourrettes (Terre Blanche) | ⤴ | Listed on `golf/france.html` |
| 154 | Newport (Celtic Manor) | ⤴ | Listed on `golf/wales.html` |
| 155 | Cardiff (Vale Resort) | ⤴ | Listed on `golf/wales.html` |
| 156 | Swasea (Royal Porthcawl) | ⤴ | Listed on `golf/wales.html` |
| 157 | Halmstad | ⤴ | Listed on `golf/sweden.html` |
| 158 | Nimtofte (Lübker) | ⤴ | Listed on `golf/denmark.html` |
| 159 | Hørsholm (Kokkedal) | ⤴ | Listed on `golf/denmark.html` |
| 160 | Malmö (PGA of Sweden National) | ⤴ | Listed on `golf/sweden.html` |
| 161 | Estocolmo (Bro Hof Slott) | ⤴ | Listed on `golf/sweden.html` |
| 162 | Himmerland | ⤴ | Listed on `golf/denmark.html` |
| 163 | Amsterdam (The International) | ⤴ | Listed on `golf/netherlands.html` |
| 164 | Wassenaar (Koninklijke Haagsche) | ⤴ | Listed on `golf/netherlands.html` |
| 165 | Beetsterzwaag (Lauswolt) | ⤴ | Listed on `golf/netherlands.html` |
| 166 | Grassau (Das Achental) | ⤴ | Listed on `golf/germany.html` |
| 168 | München (Eichenried) | ⤴ | Listed on `golf/germany.html` |
| 169 | Berlin (Wannsee) | ⤴ | Listed on `golf/germany.html` |
| 170 | Germany hub | ▲ | `golf/germany.html` |
| 171 | Crans-Montana | ⤴ | Listed on `golf/switzerland.html` |
| 172 | Thun | ⤴ | Listed on `golf/switzerland.html` |
| 173 | Genève | ⤴ | Listed on `golf/switzerland.html` |
| 174 | Schweiz (Switzerland) hub | ▲ | `golf/switzerland.html` |

## Italy multi-day itineraries (from `golf 2/htm/`)

| Legacy file | Status | Maps to |
|---|---|---|
| `golf 2/htm/ITA-0004.htm` (Lake Como, 9 days) | ✓ | `golf/italy-lake-como.html` |
| `golf 2/htm/ITA-0005.htm` (Tuscany & Umbria, 11 days) | ✓ | `golf/italy-tuscany-umbria.html` |
| `golf 2/htm/ITA-0006.htm` (Sicily, 8 days) | ✓ | `golf/italy-sicily.html` |

## Coverage summary

| Bucket | Count |
|---|---|
| ✓ Covered (dedicated detail page) | 52 |
| 🆕 New (this audit pass) | 20 (5 6-Nights + 10 Argentina Golf combos + 5 USA pages: Baywood Los Osos, Las Vegas, Mesquite, Rancho Santa Fe, Phoenix) |
| ⤴ Consolidated (within hub page) | ~80 (per-course pairs on country hubs) |
| ▲ Hub replaced (now catalog) | 18 |
| 🗑 Junk/duplicate (legitimately skipped) | 6 |
| **Total legacy pages accounted for** | **173 of 173** (170 PHP + 3 Italy HTM) |

## Cross-reference status

**Every legacy page has been classified** — either:
- Built as a dedicated redesign page (✓ or 🆕)
- Consolidated into a country/region hub page where its content lives as a LOCATION – COURSE / HOTEL block (⤴)
- Replaced by the modern catalog UX where the legacy hub was just a menu (▲)
- Legitimately skipped because the legacy file is empty, a test page, or contains duplicated/mislabeled content from another destination (🗑)

The 6 skipped pages are:
- 1, 3, 5, 13, 25, 44 (Home + Contact + Menu + tier menus + "asdasd" test page — these are navigation, not content)
- 31 Mar del Plata (body is duplicate Ushuaia content)
- 45 / 147 / 149 / 151 (England + Birmingham + Warwickshire + Lincolnshire — bodies are duplicate Italy content)

## Maintenance — adding a new destination

For maintainability, the redesign uses **two structural patterns**:

1. **Per-destination detail page** (`category/slug.html`): used when the destination has its own substantive prose (day-by-day itinerary, package details, etc.). Pattern is documented in `docs/DETAIL_TEMPLATE.html`.

2. **Course-on-hub-page section** (LOCATION – COURSE / HOTEL block on a region page): used when a destination is just one of many courses in a country. To add a new course to e.g. `golf/spain.html`, append a new `<article>` block with the location, course, and hotel name. No new file needed.

**Recommendation for future content additions:**
- Single-destination program with prose → new detail page
- New golf course in an existing country → add to the country hub page
- New country → new region detail page in `golf/`
- New per-region golf combo → new page in `argentina-golf/` or wherever fits

This keeps the page count manageable while making every legacy destination discoverable.
