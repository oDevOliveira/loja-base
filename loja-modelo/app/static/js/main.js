
document.addEventListener("DOMContentLoaded", () => {
    // Menu mobile
    const botaoMenu = document.querySelector("[data-menu-toggle]");
    const menu = document.querySelector("[data-menu]");

    if (botaoMenu && menu) {
        botaoMenu.addEventListener("click", () => {
            const aberto = menu.classList.toggle("aberto");
            botaoMenu.setAttribute("aria-expanded", aberto);
        });
    }

    // Confirmar exclusões
    document.querySelectorAll("[data-confirmar]").forEach(botao => {
        botao.addEventListener("click", evento => {
            const mensagem = botao.dataset.confirmar ||
                "Deseja realmente excluir este item?";

            if (!confirm(mensagem)) {
                evento.preventDefault();
            }
        });
    });

    // Pré-visualizar imagens
    document.querySelectorAll('input[type="file"][data-preview]').forEach(input => {
        input.addEventListener("change", () => {
            const destino = document.querySelector(input.dataset.preview);
            const arquivo = input.files[0];

            if (!destino || !arquivo) return;

            if (!arquivo.type.startsWith("image/")) {
                alert("Selecione uma imagem válida.");
                input.value = "";
                return;
            }

            if (destino.dataset.urlTemporaria) {
                URL.revokeObjectURL(destino.dataset.urlTemporaria);
            }

            const url = URL.createObjectURL(arquivo);
            destino.src = url;
            destino.dataset.urlTemporaria = url;
            destino.hidden = false;
        });
    });

    // Validar quantidade
    document.querySelectorAll("[data-quantidade]").forEach(campo => {
        campo.addEventListener("change", () => {
            const quantidade = Number(campo.value);
            const minimo = Number(campo.min || 1);
            const maximo = Number(campo.max || 99);

            if (!Number.isFinite(quantidade)) {
                campo.value = minimo;
                return;
            }

            campo.value = Math.min(maximo, Math.max(minimo, quantidade));
        });
    });

    // Evitar envio duplo de formulários
    document.querySelectorAll("form[data-envio-unico]").forEach(formulario => {
        formulario.addEventListener("submit", () => {
            if (!formulario.checkValidity()) return;

            const botao = formulario.querySelector('[type="submit"]');

            if (botao) {
                botao.disabled = true;
                botao.textContent = "Processando...";
            }
        });
    });
});


