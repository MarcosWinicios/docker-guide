# Estratégias de uso

## **Reutilização de containers**
Uma das principais vantagens do Docker é a reutilização de containers. Em vez de criar um novo container para cada execução da aplicação, é possível reutilizar o mesmo container várias vezes. Isso reduz o tempo de inicialização e o consumo de recursos.

Para reutilizar um container, basta utilizar o comando [**start**](docker-commands.md#start) em vez de [**run**](docker-commands.md#run).:

## **Acessar o terninal do container**
Para acessar o terminal de um container em execução, basta utilizar o comando [**exec**](docker-commands.md#exec) com a opção `-it`. Isso permite interagir com o container como se fosse um terminal local.

Syntax: `docker container exec -it <container-id> bash`

```bash
  docker container exec -it 1234567890 bash
```

## **Parar todos os containers**

Para parar todos os containers em execução, basta utilizar o comando [**stop**](docker-commands.md#stop) com a opção `-t 0`.

```bash
  docker container stop $(docker container ls -q)
```

## **Remover todos os containers**

Para remover todos os containers, basta utilizar o comando [**rm**](docker-commands.md#rm) com a opção `-f`.

```bash
  docker container rm -f $(docker container ls -aq)
```

## **Listar containers de uma imagem**

```bash
  docker container ls -a --filter ancestor=<nome-da-imagem>
```

## **Executar comandos ao iniciar o container**

É possível executar comandos ao iniciar o container com o comando **run**. Isso é útil para configurar o ambiente do container antes de iniciar a aplicação.

Syntax: `docker container run <imagem> <comando>`

```bash
  docker container run nginx ls
```

Para executar um shell interativo, basta passar o comando `bash`.

```bash
  docker container run -it nginx bash
```

É possível combinar o `bash` com o `-c` para executar comandos diretamente no shell do container sem abrir um shell interativo.

Exemplo, printando uma variável de ambiente do container:

```bash
  docker container run nginx bash -c 'echo $PATH'
```

## **Integrações entre a máquina host e o container**

### **Portas**: 
É possível mapear portas da máquina host para o container, permitindo que a aplicação seja acessível externamente.

Syntax: `-p <porta-host>:<porta-container>`

```bash
  docker container run -p 8080:80 nginx
```

### **Volumes**: 
Volumes permitem compartilhar arquivos entre a máquina host e o container. Isso é útil para persistir dados ou compartilhar arquivos de configuração.

Syntax: `-v <caminho-diretorio-host>:<caminho-diretorio-container>`

```bash
  docker container run -v $(pwd)/path/to/host:/path/to/container nginx
```