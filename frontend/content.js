function addGenerateButton() {
  const toolbar = document.querySelector(".btC");
  if (!toolbar) return;

  if (document.getElementById("generate-boilerplate-btn")) return;

  const button = document.createElement("button");
  button.id = "generate-boilerplate-btn";
  button.textContent = "Generate Boilerplate";
  button.style.backgroundColor = "#e1e2eb";
  button.style.color = "#007bff";
  button.style.border = "1px solid rgb(69, 167, 209)";
  button.style.padding = "10px 20px";
  button.style.marginLeft = "10px";
  button.style.cursor = "pointer";
  button.style.borderRadius = "10px";
  button.style.fontSize = "14px";
  button.style.fontWeight = "bold";

  button.style.hover = "background-color: #0056b3";

  button.addEventListener("click", handleGenerateBoilerplate);

  toolbar.appendChild(button);
}

// Function to handle the "Generate Boilerplate" button click
function handleGenerateBoilerplate() {
  const subjectInput = document.querySelector('input[name="subjectbox"]');
  const bodyInput = document.querySelector('div[aria-label="Message Body"]');

  if (!subjectInput || !bodyInput) {
    alert("Could not locate the email subject or body fields.");
    return;
  }

  const subject = subjectInput.value.trim();
  if (!subject) {
    alert("Please enter a subject before generating the boilerplate.");
    return;
  }

  // Call the backend API via the background script
  chrome.runtime.sendMessage(
    { action: "fetchBoilerplate", subject },
    (response) => {
      if (response && response.email) {
        bodyInput.innerHTML = response.email;
      } else {
        alert(
          response.error || "Failed to generate boilerplate. Try again later."
        );
      }
    }
  );
}

// Add the button once the DOM is ready
window.addEventListener("load", () => {
  const obsever = new MutationObserver(addGenerateButton);
  obsever.observe(document.body, { childList: true, subtree: true });
});
