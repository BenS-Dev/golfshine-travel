# Sitemap — Legacy → Redesign

Map of every legacy `sitepro/N.php` to its redesigned URL. Use this to verify nothing was missed and to extend the site later.

## Top-level catalog pages

| Redesign URL | Replaces | Notes |
| --- | --- | --- |
| `/index.html` | `sitepro/1.php` | Homepage |
| `/visit-argentina.html` | `sitepro/25.php` + tier menus | 4 time-tiers (3/6/13/16 Nights) + Argentina Golf tier |
| `/golf.html` | `sitepro/146.php` | All regions searchable + Italy itineraries |
| `/destinations.html` | Atlas of all destinations | Search bar + filter chips, ~40 tiles |
| `/journeys.html` | Featured Argentina + Golf programs | Tier itineraries + Italy tours |
| `/contact.html` | `sitepro/3.php` (Contact) + `43.php` (Request Pricing) | Inquiry form with `?inquiry=` prefill |
| `/404.html` | n/a | Design-system-matched 404 page (noindex) |

## Argentina destinations — `/argentina/` (13 files)

| File | Legacy source |
| --- | --- |
| `buenos-aires.html` | `sitepro/4.php` |
| `bariloche.html` | `sitepro/2.php` |
| `el-calafate.html` | `sitepro/8.php` |
| `iguazu.html` | `sitepro/10.php` |
| `puerto-madryn.html` | `sitepro/9.php` |
| `salta.html` | `sitepro/6.php` |
| `ushuaia.html` | `sitepro/7.php` |
| `buenos-aires-iguazu-ushuaia-calafate.html` | `sitepro/20.php` (13N combo) |
| `buenos-aires-iguazu-bariloche-calafate.html` | `sitepro/21.php` (13N combo) |
| `buenos-aires-iguazu-puerto-madryn-calafate.html` | `sitepro/22.php` (13N combo) |
| `buenos-aires-iguazu-puerto-madryn-ushuaia-calafate.html` | `sitepro/24.php` (16N combo) |
| `buenos-aires-puerto-madryn-ushuaia-calafate-bariloche.html` | `sitepro/26.php` (16N combo) |
| `buenos-aires-iguazu-calafate-ushuaia-australis.html` | `sitepro/27.php` (16N + cruise) |

## Argentina Golf — `/argentina-golf/` (5 files)

| File | Legacy source |
| --- | --- |
| `buenos-aires.html` | `sitepro/30.php` |
| `bariloche.html` | `sitepro/11.php` |
| `cordoba.html` | `sitepro/14.php` |
| `mendoza.html` | `sitepro/29.php` (with real prices u$s 251 single / 178 double) |
| `ushuaia.html` | `sitepro/32.php` |

## Golf regions + Italy itineraries — `/golf/` (17 files)

**Regions** (LOCATION – COURSE / HOTEL format from each legacy hub):
| File | Source |
| --- | --- |
| `scotland.html` | `sitepro/101.php` |
| `ireland.html` | `sitepro/99.php` |
| `wales.html` | `sitepro/141.php` |
| `spain.html` | `sitepro/102.php` |
| `portugal.html` | `sitepro/103.php` |
| `france.html` | `sitepro/135.php` |
| `italy.html` | `sitepro/120.php` |
| `netherlands.html` | `sitepro/139.php` |
| `germany.html` | `sitepro/170.php` |
| `switzerland.html` | `sitepro/174.php` |
| `greece.html` | `sitepro/134.php` |
| `sweden.html` | `sitepro/138.php` |
| `denmark.html` | `sitepro/137.php` |
| `norway.html` | `sitepro/124.php` |

**Italy multi-day itineraries** (day-by-day verbatim copy):
| File | Source |
| --- | --- |
| `italy-lake-como.html` | `golf 2/htm/ITA-0004.htm` (9 days) |
| `italy-tuscany-umbria.html` | `golf 2/htm/ITA-0005.htm` (11 days) |
| `italy-sicily.html` | `golf 2/htm/ITA-0006.htm` (8 days) |

## Caribbean — `/caribbean/` (5 files)

| File | Source |
| --- | --- |
| `punta-cana.html` | `sitepro/148.php` + variants `75/78/79/80.php` (4 packages combined) |
| `riviera-maya-cancun.html` | `sitepro/83.php` + `84.php` (Mayakoba) |
| `puerto-rico.html` | `sitepro/74.php` (Wyndham Grand Rio Mar) |
| `bahamas.html` | `sitepro/76.php` (Reef Course / Grand Lucayan) |
| `los-cabos.html` | `sitepro/82.php` (Diamante) |

## USA — `/usa/` (15 files)

| File | Source |
| --- | --- |
| `miami-jw-marriott-turnberry.html` | `sitepro/53.php` |
| `miami-trump-doral.html` | `sitepro/58.php` |
| `palm-beach-pga-national.html` | `sitepro/55.php` |
| `ponte-vedra-tpc-sawgrass.html` | `sitepro/60.php` |
| `st-augustine-world-golf-village.html` | `sitepro/59.php` |
| `orlando-mission-inn.html` | `sitepro/57.php` |
| `daytona.html` | `sitepro/52.php` |
| `tampa.html` | `sitepro/56.php` |
| `naples-greenlinks.html` | `sitepro/54.php` |
| `palm-springs-pga-west.html` | `sitepro/68.php` |
| `pebble-beach.html` | `sitepro/140.php` |
| `myrtle-beach.html` | `sitepro/50.php` |
| `kiawah-island.html` | `sitepro/49.php` |
| `tucson-ritz-carlton.html` | `sitepro/72.php` |
| `ocean-city-eagles-landing.html` | `sitepro/73.php` |

## Contact info — single source of truth

Used identically on every page footer and detail-page CTA strip:

- **Email:** `contact@gulfshineservices.us`
- **Phone:** `(561)985-3886`
- **Legal phrase:** `Fla. Seller of Travel Ref. No. ST46553.`

Source: `sitepro/90.php` (St. Andrews footer) and `golf 2/cabezal.php`.

## Pages NOT migrated as standalone

| Legacy file(s) | Reason |
| --- | --- |
| `sitepro/about.html` (planned) | No legacy source content. Deleted from build. |
| `sitepro/news.php`, `blog.php` | Empty placeholder pages on legacy. Not migrated. |
| `sitepro/5.php`, `13.php`, `19.php`, `23.php` | Tier menu hub pages — image-only navigation. Their function is now served by the time-tier sections on `visit-argentina.html`. |
| `sitepro/31.php` (Mar del Plata) | Legacy file content is duplicated Ushuaia content (mislabeled). Tile routes to contact prefill. |
| `sitepro/45.php` (England) | Legacy file content is duplicated Italy content (mislabeled). The England tile on `golf.html` and `destinations.html` routes to contact prefill. |
| `sitepro/77/85/86/87/88/89.php` (Ireland variants), `sitepro/90/91.php` (St Andrews variants), `sitepro/93/95/96/97/98/100.php` (Scotland variants), `sitepro/104-156.php` (per-course detail pages) | These are sub-pages of the country hubs already represented. The hub-page detail pages list every LOCATION – COURSE / HOTEL pair. |
| `golf 2/*` PHP iframe wrappers | They wrap external `ltvtech.com` CFM endpoints with no extractable local content. The only real prose lived in `htm/ITA-000{4,5,6}.htm`, all of which are migrated. |
| `sitepro/81.php` (Nations Cup) | Surfaced as a card on `journeys.html`. No separate detail page. |

## File counts

- **Top-level catalog:** 7 (index, visit-argentina, golf, destinations, journeys, contact, 404)
- **Argentina:** 13 (7 destinations + 6 combo itineraries)
- **Argentina Golf:** 5 (BA, Bariloche, Cordoba, Mendoza, Ushuaia)
- **Golf:** 17 (14 region pages + 3 Italy itineraries)
- **Caribbean:** 5
- **USA:** 15
- **Total HTML pages:** **63**
- **`sitemap.xml` URLs:** 62 (all except 404.html)
