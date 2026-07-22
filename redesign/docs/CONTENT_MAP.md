# Content Map

A flat list of every page, every section, and where to edit text/imagery. Sections are listed in render order top → bottom.

## index.html - Homepage
| Section | What it does | Edit in |
| --- | --- | --- |
| Header / Nav | Brand mark, primary navigation, "Plan Your Trip" CTA | `index.html` `<header>`, styled by `components.css` `.site-header` |
| Hero | Cinematic full-bleed intro with title, sub, two CTAs | `<section class="hero">` |
| Feature Panels (2-up) | Visit Argentina + Golf - the brand's two main paths | `<section class="feature-panels">` |
| Explore the World | 6-tile world atlas grid | `<section class="section section--cream">` |
| Featured Journeys | 3 hand-picked journey cards | `<section class="section section--cream-warm">` |
| Why Travel With Gulfshine | 4 feature blocks on dark green | `<section class="section section--dark">` |
| CTA Banner | "Let's design your next journey" | `<section class="cta-banner">` |
| Footer | 4-column footer + Seller of Travel legal | `<footer class="site-footer">` |

## visit-argentina.html - Visit Argentina
| Section | What it does |
| --- | --- |
| Hero (inner) | "Argentina, at her own pace" |
| Argentina Destinations Grid | All 8 regions: Buenos Aires, Iguazú, Bariloche, El Calafate, Ushuaia, Mendoza, Puerto Madryn, Salta |
| Editorial - Buenos Aires Desk | A note about the local team |
| Featured Itineraries | 3 Argentina journey cards |
| Custom Argentina Trip CTA | Bespoke design CTA |
| Footer | Standard |

## golf.html - Golf Travel
| Section | What it does |
| --- | --- |
| Hero (inner) | "The world's great courses, played well" |
| World-Class Golf Destinations | 10 country/region tiles |
| Featured Golf Experiences | 3 signature itineraries |
| Editorial - Wingolf Approach | Why golf travel feels different |
| Custom Golf Travel CTA | Bespoke design CTA |
| Footer | Standard |

## destinations.html - World Atlas
| Section | What it does |
| --- | --- |
| Page header | "The Atlas" |
| South America (01) | Editorial → links to Argentina |
| Caribbean (02) | Editorial + 3-tile sub-grid |
| Europe (03) | Editorial + 3-tile sub-grid |
| USA (04) | Editorial |
| Rest of the World (05) | Editorial |
| CTA Banner | Standard |
| Footer | Standard |

## journeys.html - Featured Journeys
| Section | What it does |
| --- | --- |
| Page header | "Journeys, hand-built." |
| Search + filter bar | `<input id="journeySearch">` + 6 filter chips (All, Argentina, Golf, Caribbean, Europe, USA) |
| Journey grid | 12 cards. Each card has `data-cat` (filter category) and `data-text` (extra search keywords) |
| Empty state | Hidden by default - shown by `filters.js` when no cards match |
| CTA Banner | Standard |
| Footer | Standard |

**To add a journey card:** copy any `<article class="journey-card">` block, swap image, title, description, duration. Tag with one or more space-separated categories in `data-cat`. Add searchable keywords in `data-text`.

## about.html - About Gulfshine
| Section | What it does |
| --- | --- |
| Page header | "A small house, three decades in." |
| Story editorial | Brand origin + how the company grew |
| Values list | 5 numbered principles (i-v) |
| CTA Banner | Standard |
| Footer | Standard |

## contact.html - Plan Your Trip
| Section | What it does |
| --- | --- |
| Page header | "Tell us the rough idea." |
| Inquiry form | Name, email, phone, destination, trip type, dates, message |
| Contact meta sidebar | Email, phone, offices, response promise, Seller of Travel license |
| Footer | Standard |

**Form note:** the form currently posts to `#`. When wiring to a real handler (Formspree, Netlify Forms, custom endpoint), update the `action` attribute on the `<form>` only - field names already match common handlers.

## Legal - Seller of Travel

Every page footer renders:

> Fla. Seller of Travel Ref. No. ST46553.

It also appears in the contact page sidebar under **License**. Do not alter the wording.

## Content preservation

Per `RULE.MD`, all major regions and itineraries from the old site are represented:

- Argentina: Buenos Aires, Iguazú, Bariloche, El Calafate, Ushuaia, Mendoza, Puerto Madryn, Salta
- Golf: Scotland, Ireland, Portugal, Spain, Italy, Greece, Netherlands, Argentina, Caribbean, USA
- World: Caribbean / Bahamas, Europe / Mediterranean, USA, Rest of the World

If a section is added, mirror its row here.
