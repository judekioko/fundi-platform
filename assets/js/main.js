// TODO: replace with the real Fundi WhatsApp Business number, international format, no leading +
// e.g. Kenya number 0712 345 678 -> "254712345678"
const WHATSAPP_NUMBER = "254700000000";

const form = document.getElementById("request-form");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  if (!form.reportValidity()) return;

  const data = Object.fromEntries(new FormData(form).entries());

  const message = [
    "New Fundi request:",
    `Category: ${data.category}`,
    `Problem: ${data.description}`,
    `Location: ${data.location}`,
    `Urgency: ${data.urgency}`,
    `Name: ${data.name}`,
    `Phone: ${data.phone}`,
  ].join("\n");

  const url = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
  window.open(url, "_blank", "noopener");
});
