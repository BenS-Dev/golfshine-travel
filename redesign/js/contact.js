/**
 * Contact form — prefill from ?inquiry= URL param.
 * Used when a detail-page "Plan This Trip" CTA links here with the
 * destination name as a query param.
 *
 * Example: contact.html?inquiry=St+Andrews+Old+Course
 *   → message field prepended with "I'm interested in: St Andrews Old Course\n\n"
 *   → destination select updated when a matching option exists
 */
(function () {
  const params = new URLSearchParams(window.location.search);
  const inquiry = (params.get("inquiry") || "").trim();
  if (!inquiry) return;

  const message = document.getElementById("message");
  if (message) {
    const prefix = "I'm interested in: " + inquiry + "\n\n";
    message.value = prefix + message.value;
    message.focus();
    message.setSelectionRange(message.value.length, message.value.length);
  }

  const destination = document.getElementById("destination");
  if (destination) {
    const wanted = inquiry.toLowerCase();
    for (const opt of destination.options) {
      if (opt.value && wanted.includes(opt.value.toLowerCase().split(/[\s&]/)[0])) {
        destination.value = opt.value;
        break;
      }
    }
  }
})();

/**
 * Contact form submission → send.php (Resend).
 * Progressive enhancement: intercept the submit, POST via fetch, show an
 * inline status message. With JS off, the form posts normally and send.php
 * redirects back to contact.html?sent=1 / ?sent=0 (handled below).
 */
(function () {
  const form = document.getElementById("inquiry-form");
  const status = document.getElementById("form-status");
  if (!form || !status) return;

  function show(ok, message) {
    status.hidden = false;
    status.innerHTML =
      '<span class="form-status__icon" aria-hidden="true">' +
      (ok ? "✓" : "✕") +
      "</span><span class=\"form-status__text\"><strong>" +
      (ok ? "Inquiry sent" : "Not sent") +
      "</strong> — " +
      message +
      "</span>";
    status.classList.toggle("form-status--ok", ok);
    status.classList.toggle("form-status--error", !ok);
    status.scrollIntoView({ behavior: "smooth", block: "center" });
  }

  // No-JS fallback redirect result (?sent=1 / ?sent=0).
  const sent = new URLSearchParams(window.location.search).get("sent");
  if (sent === "1") {
    show(true, "Thank you — your inquiry is on its way. We answer every message personally.");
  } else if (sent === "0") {
    show(false, "Sorry — something went wrong. Please email contact@gulfshineservices.us.");
  }

  form.addEventListener("submit", async function (event) {
    event.preventDefault();
    const button = form.querySelector('button[type="submit"]');
    const original = button ? button.textContent : "";
    if (button) {
      button.disabled = true;
      button.textContent = "Sending…";
    }
    try {
      const res = await fetch(form.action, {
        method: "POST",
        body: new FormData(form),
        headers: { "X-Requested-With": "fetch", Accept: "application/json" },
      });
      const data = await res.json().catch(() => ({ ok: res.ok, message: "" }));
      show(
        data.ok,
        data.message ||
          (data.ok
            ? "Thank you — your inquiry is on its way."
            : "Something went wrong. Please email contact@gulfshineservices.us.")
      );
      if (data.ok) form.reset();
    } catch (err) {
      show(false, "Network error — please email contact@gulfshineservices.us.");
    } finally {
      if (button) {
        button.disabled = false;
        button.textContent = original;
      }
    }
  });
})();
