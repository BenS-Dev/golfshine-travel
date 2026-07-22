<?php
/**
 * Contact form handler - sends inquiries via the Resend API.
 *
 * The static contact form POSTs here. Works with or without JavaScript:
 *   - AJAX (fetch) requests get a JSON response.
 *   - Plain form posts get redirected back to contact.html?sent=1 / ?sent=0.
 *
 * Configuration lives in config.php (copy from config.sample.php). The Resend
 * API key never lives in client code or in git.
 */

declare(strict_types=1);

$wantsJson = (
    (isset($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) === 'fetch')
    || (isset($_SERVER['HTTP_ACCEPT']) && strpos($_SERVER['HTTP_ACCEPT'], 'application/json') !== false)
);

function respond(bool $ok, string $message, bool $wantsJson): void
{
    if ($wantsJson) {
        header('Content-Type: application/json');
        http_response_code($ok ? 200 : 400);
        echo json_encode(['ok' => $ok, 'message' => $message]);
    } else {
        header('Location: contact.html?sent=' . ($ok ? '1' : '0'));
    }
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    respond(false, 'Method not allowed.', $wantsJson);
}

// Spam honeypot - bots fill hidden fields; humans never see them.
if (!empty($_POST['company'] ?? '')) {
    // Pretend success so bots don't learn anything.
    respond(true, 'Thank you! We will be in touch shortly.', $wantsJson);
}

$config = @include __DIR__ . '/config.php';
if (!is_array($config) || empty($config['resend_api_key']) || $config['resend_api_key'] === 'RESEND_API_KEY_GOES_HERE') {
    respond(false, 'The form is not configured yet. Please email contact@gulfshineservices.us.', $wantsJson);
}

$name    = trim((string)($_POST['name'] ?? ''));
$email   = trim((string)($_POST['email'] ?? ''));
$message = trim((string)($_POST['message'] ?? ''));

if ($name === '' || $email === '' || $message === '') {
    respond(false, 'Please fill in your name, email, and a short message.', $wantsJson);
}
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    respond(false, 'Please enter a valid email address.', $wantsJson);
}

// Collect the optional fields for the inquiry body.
$fields = [
    'Name'                  => $name,
    'Email'                 => $email,
    'Phone'                 => trim((string)($_POST['phone'] ?? '')),
    'Destination interest'  => trim((string)($_POST['destination'] ?? '')),
    'Trip type'             => trim((string)($_POST['trip-type'] ?? '')),
    'Rough dates'           => trim((string)($_POST['dates'] ?? '')),
];

$rows = '';
$text = '';
foreach ($fields as $label => $value) {
    if ($value === '') {
        continue;
    }
    $safe = htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
    $rows .= "<tr><td style=\"padding:4px 12px 4px 0;font-weight:600\">{$label}</td><td style=\"padding:4px 0\">{$safe}</td></tr>";
    $text .= "{$label}: {$value}\n";
}
$msgHtml = nl2br(htmlspecialchars($message, ENT_QUOTES, 'UTF-8'));
$text   .= "\nMessage:\n{$message}\n";

$html = "<h2 style=\"font-family:Georgia,serif\">New trip inquiry</h2>"
      . "<table style=\"font-family:Arial,sans-serif;font-size:14px;border-collapse:collapse\">{$rows}</table>"
      . "<p style=\"font-family:Arial,sans-serif;font-size:14px\"><strong>Message</strong><br>{$msgHtml}</p>";

$payload = [
    'from'     => $config['from'],
    'to'       => [$config['to']],
    'reply_to' => $email,
    'subject'  => 'New trip inquiry from ' . $name,
    'html'     => $html,
    'text'     => $text,
];

$ch = curl_init('https://api.resend.com/emails');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_POSTFIELDS     => json_encode($payload),
    CURLOPT_HTTPHEADER     => [
        'Authorization: Bearer ' . $config['resend_api_key'],
        'Content-Type: application/json',
    ],
    CURLOPT_TIMEOUT        => 20,
]);
$response = curl_exec($ch);
$status   = (int)curl_getinfo($ch, CURLINFO_HTTP_CODE);
$curlErr  = curl_error($ch);
unset($ch); // handle freed automatically on PHP 8+

if ($curlErr !== '' || $status < 200 || $status >= 300) {
    error_log('Resend send failed (' . $status . '): ' . ($curlErr ?: $response));
    respond(false, 'Sorry, something went wrong sending your message. Please email contact@gulfshineservices.us.', $wantsJson);
}

respond(true, 'Thank you! Your inquiry is on its way. We answer every message personally.', $wantsJson);
