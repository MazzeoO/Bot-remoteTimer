# Bot-remoteTimer
Um bot do telegram no qual você define um tempo em segundos e após quando o tempo acabar, o seu pc irá desligar.
*para o desenvolvimento desse projeto, IAs como ChatGpt e Gemini foram utilizadas como auxiliadores.*


## Descrição 📖
Este bot recebe uma quantidade de tempo em segundos e inicia uma contagem regressiva. Quando a contagem chega ao fim, ele executa o comando de desligamento do computador. Antes do desligamento, é iniciado um timer de 60 segundos como período de tolerância.
Este bot opera via Telegram, permitindo controle remoto do computador diretamente pelo celular.
O projeto foi desenvolvido para situações em que o usuário não pode desligar o PC localmente, como ao sair de casa ou ao estar em outro ambiente.


## Funcionamento ⚙️
Quando o código é iniciado, o bot leva alguns segundos para iniciar e, em seguida, responde no chat do Telegram com a mensagem “Bot iniciado...”, indicando que já está em funcionamento.
O usuário deve inserir o token do bot e o ID do chat no arquivo config.py, para que o sistema consiga identificar e responder corretamente ao chat desejado.

O bot possui comandos para:

definir o tempo inicial
visualizar o tempo restante
acrescentar tempo
desligar o computador
cancelar o desligamento


## Comandos 
Os comandos utilizados pelo bot:

- /start -> dá as opções iniciais
- /settime X -> Define o tempo
- /time -> para visualizar o tempo
- /acres X -> acrescenta mais tempo
- /exit -> desliga o computador em 60s
- /cancel -> cancela o /exit


## Tecnologias utilizadas 🧠

- python
- pyTelegramBotAPI (telebot)
- telegram Bot API
- Windows 10/11
  

### Bibliotecas padrões
- time
- threading
- os


### instalação

```bash
pip install pyTelegramBotAPI
```


## Como Executar
1. para executar, o usuario deverá instalar a dependência:
```bash
pip install pyTelegramBotAPI
```
2. após isso, o usuario terá que configurar o arquivo **config.py** e colocar o **TOKEN** do seu bot e o **Chat_ID** do seu chatBot.
3. Esperar até que no chat do telegram o bot envie "Bot iniciado...".


## AVISO

Este projeto executa comandos no sistema operacional Windows.
Use com cuidado para evitar desligamentos acidentais.


## Estrutura do Projeto

```md id="fix1"
- main.py
- bot.py
- commands.py
- tim.py
- system.py
- config.py
```


## Autoria
Esse projeto foi desenvolvido por **Gabriel Mazzeo**
https://github.com/MazzeoO
