(() => {
  let altIdCounter = 0;

  const toggleAltText = (button) => {
    const targetId = button.getAttribute("aria-controls");
    const target = targetId ? document.getElementById(targetId) : null;
    if (!target) {
      return;
    }
    const isExpanded = button.getAttribute("aria-expanded") === "true";
    button.setAttribute("aria-expanded", (!isExpanded).toString());
    if (isExpanded) {
      target.setAttribute("hidden", "");
    } else {
      target.removeAttribute("hidden");
    }
  };

  const createAltControls = (img, altText) => {
    altIdCounter += 1;
    const controls = document.createElement("div");
    controls.className = "alt-controls";

    const button = document.createElement("button");
    button.type = "button";
    button.className = "alt-toggle";
    button.textContent = "ALT";
    button.setAttribute("aria-expanded", "false");

    const altId = `alt-text-${altIdCounter}`;
    button.setAttribute("aria-controls", altId);

    const text = document.createElement("p");
    text.id = altId;
    text.className = "alt-text";
    text.hidden = true;
    text.textContent = altText;

    controls.append(button, text);
    img.insertAdjacentElement("afterend", controls);
    img.dataset.altToggle = "true";
  };

  const attachAltToggles = (root = document) => {
    const scope = root instanceof Element ? root : document;
    const images = scope.querySelectorAll("main img[alt]");
    images.forEach((img) => {
      const altText = img.getAttribute("alt");
      if (!altText || altText.trim() === "") {
        return;
      }
      if (img.dataset.altToggle === "true") {
        return;
      }
      const next = img.nextElementSibling;
      if (next && next.classList.contains("alt-controls")) {
        img.dataset.altToggle = "true";
        return;
      }
      createAltControls(img, altText);
    });
  };

  document.addEventListener("click", (event) => {
    const button = event.target.closest(".alt-toggle");
    if (!button) {
      return;
    }
    toggleAltText(button);
  });

  const init = () => {
    attachAltToggles(document);
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  window.attachAltToggles = attachAltToggles;
})();
