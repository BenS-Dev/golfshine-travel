/**
 * Global UI:
 * - Header scroll state
 * - Mobile nav toggle
 */
(function () {
  const header = document.getElementById("siteHeader");
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.getElementById("primaryNav");
  const body = document.body;

  // Header on scroll
  if (header) {
    const onScroll = () => {
      if (window.scrollY > 24) header.classList.add("is-scrolled");
      else header.classList.remove("is-scrolled");
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // Mobile nav
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = body.classList.toggle("is-nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    nav.querySelectorAll("a").forEach((a) => {
      a.addEventListener("click", () => {
        body.classList.remove("is-nav-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Program toggle (3N / 6N switcher on Argentina destination pages)
  const programGroups = document.querySelectorAll("[data-program-group]");
  programGroups.forEach((group) => {
    const buttons = group.querySelectorAll(".program-toggle__btn");
    const panels = group.querySelectorAll(".program-panel");

    const activate = (value) => {
      buttons.forEach((b) => {
        const match = b.dataset.program === value;
        b.classList.toggle("is-active", match);
        b.setAttribute("aria-selected", match ? "true" : "false");
      });
      panels.forEach((p) => {
        p.hidden = p.dataset.program !== value;
      });
    };

    buttons.forEach((b) => {
      b.addEventListener("click", () => {
        activate(b.dataset.program);
        history.replaceState(null, "", "#program-" + b.dataset.program);
      });
    });

    const hashMatch = window.location.hash.match(/program-(\d+)/);
    if (hashMatch) activate(hashMatch[1]);
  });
})();
