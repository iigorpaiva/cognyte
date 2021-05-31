## Cognyte

A aplicação foi desenvolvida em Python 3.9.1 e Pip 21.1.2.
Para que a aplicação funcione, deve-se primeiro rodar o server.py e logo em seguida rodar o client.py. 
No lado do servidor, deve ser gerado listas de 5 números randômicos variando de 1 até 50.

## Libs:

Servidor: socket, random, threading, json.
Cliente: socket, json, datetime, logging, logging.handlers

## Condições: 

- `As configurações adotadas para o cliente seguem o arquivo configuration.json;`
- `A aplicação deverá gravar em um arquivo log os dados recebidos do servidor;`
- ``

## Notas:

- `No lado do servidor, não consegui identificar a tempo o porquê que os dados estão sendo mandados um a um, o que atrapalha o recebimento em tempo real dos dados, salvando apenas um array;`
- `Devio ao tempo, não pude implementar o time para fechar sessão caso não o cliente não receba dados do servidor;`
- `A aplicação foi desenvolvida no Visual Studio Code devido ao sistema operacional do computador disponível, tentei instalar o linux em uma virtualbox mas atrapalhou a eficiência da implementação;`
- `O projeto foi desenvolvido em um tempo aproximado de 10 horas`
