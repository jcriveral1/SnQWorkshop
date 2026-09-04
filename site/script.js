const buttons = document.querySelectorAll("[data-copy]");
const copyIcon = "⧉";

buttons.forEach((button) => {
  const block = button.previousElementSibling;

  if (block?.tagName === "PRE") {
    const wrapper = document.createElement("div");
    wrapper.className = "copy-block";
    block.parentNode.insertBefore(wrapper, block);
    wrapper.append(block, button);
  }

  const copyLabel = button.dataset.copyLabel || "Copiar comando";

  button.textContent = copyIcon;
  button.setAttribute("aria-label", copyLabel);
  button.setAttribute("title", copyLabel);

  button.addEventListener("click", async () => {
    try {
      const block = button.closest(".copy-block")?.querySelector("pre");
      const sourceUrl = button.dataset.copyUrl;
      const text = sourceUrl
        ? await fetch(sourceUrl).then((response) => {
            if (!response.ok) {
              throw new Error(`No se pudo leer ${sourceUrl}`);
            }
            return response.text();
          })
        : block?.innerText ?? "";

      await navigator.clipboard.writeText(text);
      button.textContent = "✓";
      button.setAttribute("title", "Copiado");
      window.setTimeout(() => {
        button.textContent = copyIcon;
        button.setAttribute("title", copyLabel);
      }, 1400);
    } catch {
      button.textContent = "!";
      button.setAttribute("title", "No se pudo copiar");
    }
  });
});
