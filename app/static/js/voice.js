console.log("ARQUIVO JS NOVO CARREGADO");
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
        console.log("Clique no botão iniciar");
        chamadaAtiva = true;

        btn.style.display = "none";

        endCall.style.display = "inline-block";
        
        console.log(endCall);

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

        btn.style.display = "inline-block";
        endCall.style.display = "none";

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

        const textoLimpo =
            data.response
                .replace(/\*\*/g, "")
                .replace(/\*/g, "")
                .replace(/#/g, "")
                .replace(/`/g, "");

        responseBox.innerText =
            textoLimpo;

        console.log("Resposta", data.response);

        const fala = new SpeechSynthesisUtterance(
            textoLimpo
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