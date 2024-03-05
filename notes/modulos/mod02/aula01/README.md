# Aula 01

Atenção, essas anotação foram testadas no Linux Mint 21.3 (victoria), para verificar a versão do seu ambiente Linux, execute o comando:

## 1. Instalação

#### 1.1 Verificar seu Sistema Operacional

    lsb_release -a

#### 1.2 Instalações
Para realizar os procedimentos de teste é necessário realizar a instalação do Python 3:

    sudo apt install python3 python3-pip -y

#### 1.2 Validar instalação

    python3 --version

## 2. Exemplos

#### 2.1 Hash SHA-256
Testar exemplo

    python3 main1.py

#### 2.2 Hash KECCAK-256
Instalar o módulo keccaky

    pip3 install keccaky

Caso esteja tudo certo execute o comando

    python3 main2.py

#### 2.3 Chaves Públicas
Instalar o módulo eth-account

    pip3 install eth-account

Caso esteja tudo certo execute o comando

    python3 main3.py

#### 2.4 Merkle Tree
Instalar o módulo [merkly](https://github.com/olivmath/merkly).

    pip install merkly

Caso esteja tudo certo execute o comando

    python3 main4.py

Outro exemplo do merkle tree

    python3 main5.py

#### 2.5 Mineração PoW

        python3 main6.py

#### 2.6 Mineração PoW

        python3 main7.py
