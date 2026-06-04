console.log("ARQUIVO JS NOVO CARREGADO");
const btn = document.getElementById("btn");
const status = document.getElementById("status");
const responseBox = document.getElementById("response");
const endCall = document.getElementById("btn-end");

let chamadaAtiva = false;

//Criando reconhecimento por voz
const ReconhecimentoFala =
    window.SpeechRecognition || 
    window.webkitSpeechRecognition;

if (!ReconhecimentoFala){

    status.innerText = 
        "Seu navegador não suporta reconhecimento por voz";
} else{


    //criando o objeto que controle o mic
    const reconhecimento = new ReconhecimentoFala()

    reconhecimento.lang = "pt-BR";
    //parar de ouvir a cada frase
    reconhecimento.continuous = false;

    //Parciais, recebendo apenas o resultado final para simplificar o fluxo
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
    


    //Iniciando a chamada
    btn.addEventListener("click", () => {
        console.log("Clique no botão iniciar");
        chamadaAtiva = true;

        btn.style.display = "none"; //esconde

        endCall.style.display = "inline-block"; //mostra 
        
        console.log(endCall);

        document.getElementById(
            "call-status"
        ).innerText = "🟢 Em chamada"

    

        status.innerText = "📞 Chamada iniciada";

        //liga mic
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

    //Evento,Transcreve o audio
    reconhecimento.onresult = async (event) => {
        console.log("1 - capturou áudio");

        //Transformou audio em rexto
        const texto =
            event.results[0][0].transcript;

        console.log("Texto", texto);

        status.innerText = 
            "✅Natanzinho Respondendo"

        //Requisição ao Backend
        const resposta = await fetch(
            "/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                //Transforma o objeto em Json
                body: JSON.stringify({
                    text: texto
                })
            }


        );

        //Recebe resposta, transforma o Json em objeto JS
        const data = 
            await resposta.json();

        const textoLimpo =
            data.response
                .replace(/\*\*/g, "")
                .replace(/\*/g, "")
                .replace(/#/g, "")
                .replace(/`/g, "");

        //Exube texto na tela
        responseBox.innerText =
            textoLimpo;

        console.log("Resposta", data.response);

        // Convertendo o texto para voz
        const fala = new SpeechSynthesisUtterance(
            textoLimpo
        );

        fala.lang = "pt-BR";

        document.getElementById(
            "call-status"
        ).innerText =
            "🟢 Natanzinho falando";

        // Executa a fala
        speechSynthesis.speak(fala)

        // Ia terminou de falar
        fala.onend = () => {

        document.getElementById(
            "call-status"
        ).innerText =
            "🟢 Em chamada";

        status.innerText =
            "🎙️ Ouvindo novamente...";

        //Já liga o mic automaticamente
        reconhecimento.start();
    };

    status.innertext = "Resposta recebida";

    };
}