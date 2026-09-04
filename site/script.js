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

  button.textContent = copyIcon;
  button.setAttribute("aria-label", "Copiar comando");
  button.setAttribute("title", "Copiar");

  button.addEventListener("click", async () => {
    const block = button.closest(".copy-block")?.querySelector("pre");
    const text = block?.innerText ?? "";

    try {
      await navigator.clipboard.writeText(text);
      button.textContent = "✓";
      button.setAttribute("title", "Copiado");
      window.setTimeout(() => {
        button.textContent = copyIcon;
        button.setAttribute("title", "Copiar");
      }, 1400);
    } catch {
      button.textContent = "!";
      button.setAttribute("title", "No se pudo copiar");
    }
  });
});
