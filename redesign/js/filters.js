/**
 * Grid filtering + search. Used on journeys, golf, and destinations pages.
 * Wires any `.filter-chip` to its sibling `<input type="search">` and a grid
 * identified by data-grid attribute on the search input, OR falls back to
 * common IDs (#journeyGrid, #golfGrid, #atlasGrid).
 */
(function () {
  const grids = ["journeyGrid", "golfGrid", "atlasGrid"];

  grids.forEach((gridId) => {
    const grid = document.getElementById(gridId);
    if (!grid) return;

    const cards = Array.from(grid.children).filter((el) => el.matches("[data-cat], .journey-card, .tile"));
    const chips = document.querySelectorAll(".filter-chip");
    const search = document.querySelector('input[type="search"]');
    const empty = document.getElementById(gridId.replace("Grid", "Empty"));

    let activeFilter = "all";

    function apply() {
      const term = (search?.value || "").trim().toLowerCase();
      let visible = 0;
      // Word-bounded match: short region keywords like "usa" must not match
      // substrings like "ragusa". Escape the term to be regex-safe.
      const termRe = term
        ? new RegExp("\\b" + term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "i")
        : null;

      cards.forEach((card) => {
        const cats = (card.dataset.cat || "").split(/\s+/);
        // Search across data-cat + data-text + rendered text so region keywords
        // (caribbean, europe, golf, argentina, etc.) match even if they only
        // appear in the category tag.
        const text = (
          (card.dataset.cat || "") + " " +
          (card.dataset.text || "") + " " +
          card.textContent
        ).toLowerCase();

        const matchesFilter = activeFilter === "all" || cats.includes(activeFilter);
        const matchesSearch = !termRe || termRe.test(text);
        const show = matchesFilter && matchesSearch;

        card.style.display = show ? "" : "none";
        if (show) visible++;
      });

      if (empty) empty.hidden = visible > 0;
    }

    chips.forEach((chip) => {
      chip.addEventListener("click", () => {
        chips.forEach((c) => c.classList.remove("is-active"));
        chip.classList.add("is-active");
        activeFilter = chip.dataset.filter || "all";
        apply();
      });
    });

    if (search) search.addEventListener("input", apply);

    // Pre-fill search from ?search=… URL param (used by Explore-the-world tiles on the homepage).
    if (search) {
      const params = new URLSearchParams(window.location.search);
      const seed = params.get("search");
      if (seed) {
        search.value = seed;
        apply();
      }
    }
  });
})();
