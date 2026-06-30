<?php
/**
 * Copy this file to `config.php` on the server and fill in your real values.
 * `config.php` is gitignored and blocked from being served (see .htaccess).
 *
 *   cp config.sample.php config.php
 *
 * Prerequisite: verify gulfshineservices.us as a sending domain in Resend
 * (add the DKIM/SPF DNS records it gives you in cPanel) BEFORE sends will work.
 */
return [
    // From the Resend dashboard → API Keys. Keep this secret.
    'resend_api_key' => 'RESEND_API_KEY_GOES_HERE',

    // Must be an address on your Resend-verified domain.
    'from'           => 'Gulfshine Travel <noreply@gulfshineservices.us>',

    // Where inquiries are delivered.
    'to'             => 'contact@gulfshineservices.us',
];
