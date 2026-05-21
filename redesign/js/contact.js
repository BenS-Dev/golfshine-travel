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
