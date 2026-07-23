/**
 * Contact form - prefill from ?inquiry= URL param.
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
 * Contact form submission → Web3Forms (static, no server code).
 * Progressive enhancement: intercept the submit, POST via fetch, show an
 * inline status message. With JS off, the form posts normally and the
 * hidden "redirect" field brings the visitor back to contact.html?sent=1.
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
      "</strong>: " +
      message +
      "</span>";
    status.classList.toggle("form-status--ok", ok);
    status.classList.toggle("form-status--error", !ok);
    status.scrollIntoView({ behavior: "smooth", block: "center" });
  }

  // No-JS fallback redirect result (?sent=1).
  if (new URLSearchParams(window.location.search).get("sent") === "1") {
    show(true, "Thank you! Your inquiry is on its way. We answer every message personally.");
  }

  form.addEventListener("submit", async function (event) {
    event.preventDefault();
    const required = ["name", "email", "message"].map(function (id) {
      return form.querySelector("#" + id);
    });
    if (required.some(function (field) { return !field.value.trim(); })) {
      show(false, "Please fill in your name, email, and a short message.");
      return;
    }
    const button = form.querySelector('button[type="submit"]');
    const original = button ? button.textContent : "";
    if (button) {
      button.disabled = true;
      button.textContent = "Sending…";
    }
    try {
      const body = new FormData(form);
      body.delete("redirect"); // fetch path shows inline status instead
      const res = await fetch(form.action, {
        method: "POST",
        body: body,
        headers: { Accept: "application/json" },
      });
      const data = await res.json().catch(function () { return { success: res.ok }; });
      show(
        Boolean(data.success),
        data.success
          ? "Thank you! Your inquiry is on its way. We answer every message personally."
          : "Something went wrong. Please email contact@gulfshineservices.us."
      );
      if (data.success) form.reset();
    } catch (err) {
      show(false, "Network error. Please email contact@gulfshineservices.us.");
    } finally {
      if (button) {
        button.disabled = false;
        button.textContent = original;
      }
    }
  });
})();
