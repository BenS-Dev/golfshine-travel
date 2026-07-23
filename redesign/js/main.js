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

  // Program toggle is pure CSS (radio inputs); JS only honors #program-N
  // deep links, e.g. /argentina/bariloche#program-6.
  const programHash = window.location.hash.match(/^#program-(\d+)$/);
  if (programHash) {
    const radio = document.getElementById("program-" + programHash[1]);
    if (radio && radio.classList.contains("program-radio")) radio.checked = true;
  }
})();
