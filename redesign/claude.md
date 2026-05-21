# CLAUDE.md — Gulfshine / Wingolf Static Website Build Rules

You are building a modern static HTML/CSS/JS redesign.

Only work inside the `redesign/` folder.

Do not delete, move, rename, or edit anything outside `redesign/`.

Old folders such as `sitepro/` and `golf 2/` are reference-only. You may inspect them and COPY useful images/content into `redesign/assets/`, but never modify originals.

## Goal

Build a luxury travel website matching the approved mockup direction:

- premium golf + travel brand
- dark green / charcoal / cream / gold palette
- cinematic hero photography
- elegant serif headings
- clean card grids
- large image panels
- luxury editorial feel
- simple static files that can be uploaded directly to `public_html`

## Required Pages

Create:

- `index.html`
- `visit-argentina.html`
- `golf.html`
- `journeys.html`
- `destinations.html`
- `about.html`
- `contact.html`

## Required Sections

Homepage:
- header/nav
- cinematic hero
- two large panels: Visit Argentina + Golf
- Explore the World section
- Featured Journeys
- Why Travel With Gulfshine
- CTA banner
- footer

Golf page:
- golf hero
- world-class golf destinations grid
- featured golf experiences
- custom golf travel CTA
- footer

Visit Argentina page:
- Argentina hero
- Argentina destinations grid
- featured Argentina itineraries
- custom Argentina trip CTA

Journeys page:
- search bar
- filters
- journey cards

Contact page:
- inquiry form layout
- contact info
- required seller of travel text

## Legal Requirement

Add this exact phrase in the footer of every page:

“Fla. Seller of Travel Ref. No. ST46553.”

Do not alter the wording.

## File Architecture

Use this structure:

```txt
redesign/
  index.html
  visit-argentina.html
  golf.html
  journeys.html
  destinations.html
  about.html
  contact.html

  css/
    base.css
    layout.css
    components.css
    pages.css
    responsive.css

  js/
    main.js
    filters.js

  assets/
    images/
      logo/
      hero/
      destinations/
      journeys/
      golf/
      argentina/
      ui/

  docs/
    IMAGE_MAP.md
    CONTENT_MAP.md