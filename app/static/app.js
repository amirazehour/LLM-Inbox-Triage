const message = document.querySelector("#message");
const button = document.querySelector("#triage");
const result = document.querySelector("#result");

button.addEventListener("click", async () => {
  if (!message.value.trim()) {
    message.focus();
    return;
  }

  button.disabled = true;
  result.textContent = "Loading…";

  try {
    const response = await fetch("/api/triage", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: message.value }),
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || "Triage failed.");
    result.textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    result.textContent = JSON.stringify({ error: error.message }, null, 2);
  } finally {
    button.disabled = false;
  }
});
