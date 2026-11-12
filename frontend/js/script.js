function cadastrar() {
  var nome = document.getElementById("nome").value;
  var cidade = document.getElementById("cidade").value;
  var estado = document.getElementById("estado").value;
  var cultivo = document.getElementById("cultivo").value;

  if (nome == "" || cidade == "" || estado == "" || cultivo == "") {
    alert("Por favor, preencha todos os campos!");
  } else {
    alert(
      "Cadastro realizado com sucesso!\n\n" +
        "Agricultor: " +
        nome +
        "\nCidade: " +
        cidade +
        "\nEstado: " +
        estado +
        "\nCultivo: " +
        cultivo,
    );
  }
}