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

    //teste
    reconhecimento.onstart = () => {
    console.log("Microfone iniciado");
    };

    reconhecimento.onspeechstart = () => {
        console.log("Usuário começou a falar");
    };

    reconhecimento.onspeechend = () => {
        console.log("Usuário terminou de falar");
    };

    reconhecimento.onerror = (event) => {
        console.log("ERRO COMPLETO:", event);
        console.log("Código:", event.error);

        status.innerText =
            "Erro: " + event.error;
    };

    reconhecimento.lang = "pt-BR";

    reconhecimento.continuous = false;

    reconhecimento.interimResults = false;

    btn.addEventListener("click", () => {

        status.innerText = "🎙️ Ouvindo...";

        reconhecimento.start();
    });

    reconhecimento.onresult = async (event) => {
        console.log("1 - capturou áudio")
        const texto =
            event.results[0][0].transcript;

        console.log("2 - capturou áudio")
        status.innerText = 
            "✅Texto capturado e enviando para o servidor"

        const resposta = await fetch(
            "/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    text: texto
                })
            }


        );

        console.log("3 - capturou áudio")

        const data = 
            await resposta.json();

        console.log("4 - Json recebido")

        responseBox.innerText =
            data.response;

        console.log("5 - Texto exibido");

        const fala = new SpeechSynthesisUtterance(
            data.response
        );

        fala.lang = "pt-BR";

        console.log("6 - Objeto de fala criado");

        speechSynthesis.speak(fala)

        console.log("7 - falando");

        status.innerText = 
            "Resposta recebida";



    };

    reconhecimento.onerror = (event) => {

        status.innerText = 
            "Erro: " + event.error;
    };

    reconhecimento.onend = () => {

        console.log("Reconhecimento encerrado");
    };





}