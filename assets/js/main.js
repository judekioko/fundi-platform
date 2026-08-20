const WHATSAPP_NUMBER = "254113781366";

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
