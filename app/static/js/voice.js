const btn = document.getElementById("btn");
const status = document.getElementById("status");
const responseBox = document.getElementById("response");
const endCall = document.getElementById("btn-end");

let chamadaAtiva = false;

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

    reconhecimento.onend = () => {
        console.log("Reconhecimento encerrado");
    };
    

    btn.addEventListener("click", () => {

        chamadaAtiva = true;

        document.getElementById(
            "call-status"
        ).innerText = "🟢 Em chamada"

    

        status.innerText = "📞 Chamada iniciada";

        reconhecimento.start();
    });

    endCall.addEventListener("click", () => {
        chamadaAtiva = false;

        reconhecimento.stop();

        speechSynthesis.cancel();

        document.getElementById(
            "call-status"
        ).innerText =
            "⚪ Encerrada";

        status.innerText = "📴 Chamada encerrada"
    })

    reconhecimento.onresult = async (event) => {
        console.log("1 - capturou áudio");
        const texto =
            event.results[0][0].transcript;

        console.log("Texto", texto);
        status.innerText = 
            "✅Enviando para IA"

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


        const data = 
            await resposta.json();

        responseBox.innerText =
            data.response;

        console.log("Resposta", data.response);

        const fala = new SpeechSynthesisUtterance(
            data.response
        );

        fala.lang = "pt-BR";

        document.getElementById(
            "call-status"
        ).innerText =
            "🟢 IA falando";

        speechSynthesis.speak(fala)

        fala.onend = () => {

        document.getElementById(
            "call-status"
        ).innerText =
            "🟢 Em chamada";

        status.innerText =
            "🎙️ Ouvindo novamente...";

        reconhecimento.start();
    };

    status.innertext = "Resposta recebida";

    };
}