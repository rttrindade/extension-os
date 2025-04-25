function pegaForm() {
    event.preventDefault()

    /*Pega os dados do form*/
    let data = document.getElementById("data").value
    let condominio = document.getElementById("condominio").value
    let inicio = document.getElementById("inicio").value
    let fim = document.getElementById("fim").value
    let servico = document.getElementById("servico").value
    let tecnico = document.getElementById("tecnico").value
    var parou = document.getElementsByName('parou')
    let modelo = document.getElementById("modelo").value
    var parouConfirma = ''

    /*Valida se o condominio ficou parado*/
    if (parou[0].checked) {
        parouConfirma = true
    }
    else{
        parouConfirma = false
    }

    /*transforma os dados em json*/
    body = {
        "data": data,
        "condominio": condominio,
        "inicio": inicio,
        "fim": fim,
        "servico": servico,
        "tecnico": tecnico,
        "parou": parouConfirma,
        "modelo": modelo
    }

    console.log(body)

}