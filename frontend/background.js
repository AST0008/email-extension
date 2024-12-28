async function fetchBoilerplate(subject) {
  try {
    const response = await fetch(
      "https://web-production-1cc2.up.railway.app/generate",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ subject }),
      }
    );

    const data = await response.json();
    if (data.email) {
      return { email: data.email };
    } else {
      return { error: data.error || "Unknown error" };
    }
  } catch (err) {
    return { error: err.message };
  }
}

// Listen for messages from the content script

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "fetchBoilerplate") {
    fetchBoilerplate(message.subject).then(sendResponse);
    return true; // Indicates async response
  }
});
