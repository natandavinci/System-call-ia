const btn = document.getElementById("btn");
const status = document.getElementById("status");
const responseBox = document.getElementById("response");

const ReconhecimentoFala =
    window.SpeechRecognition || 
    window.webkitSpeechRecognition;

if (!ReconhecimentoFala){

    status.innerText = 
        "Seu navegador não suporta reconhecimento por voz";
} else{

    const reconhecimento = new ReconhecimentoFala()

    reconhecimento.lang = "pt-BR";

    reconhecimento.continuous = false;

    reconhecimento.interimResults = false;

    btn.addEventListener("click", () => {

        status.innerText = "🎙️ Ouvindo...";

        reconhecimento.start();
    });

    reconhecimento.onresult = (event) => {

        const texto =
            event.results[0][0].transcript;

        status.innerText = 
            "✅Texto capturado"

        responseBox.innerText = texto
    };

    reconhecimento.onerror = (event) => {

        status.innerText = 
            "Erro: " + event.error;
    };

    reconhecimento.onend = () => {

        console.log("Reconhecimento encerrado");
    };





}