# Comandos docker

## **Mudança de syntax do docker**
A partir da versão 1.13, o Docker passou a utilizar uma nova syntax para os comandos. 
A syntax antiga ainda é válida, mas é recomendado o uso da nova syntax.

Exemplo de mudança de syntax:
- **Antiga**: `docker run -it <docker-image>`
- **Nova**: `docker container run -it <docker-image>`

Agora, os comandos são divididos em categorias:
- `docker container`: Comandos relacionados a containers.
- `docker image`: Comandos relacionados a imagens.
- `docker network`: Comandos relacionados a redes.
- `docker volume`: Comandos relacionados a volumes.

Então, o comando `docker run` passa a ser `docker container run`.

Ou seja, a nova syntax é:
```bash
  docker <categoria> <comando> <opções> <argumentos-referente-a-categoria>
```



## **Comandos**

### **ls**

Lista os recursos em execução.

```bash
  docker container ls
```

`docker container ls` é um alias para `docker container ps`.

``docker image ls``: Lista as imagens disponíveis.

``docker network ls``: Lista as redes disponíveis.

``docker volume ls``: Lista os volumes disponíveis.

Pode ser combinado com as opções `-a`, `-q`, `-s`, `--no-trunc`, `--latest`. Ver em [Opções comuns](#opções).

### **run**

```bash
  docker container run <docker-image>
```

O comando ``docker container run`` concatena os seguintes comandos:
1. [`docker image pull`](#pull)
2. [`docker container create`](#create)
3. [`docker container start`](#start)
4. [`docker container exec`](#exec)

Pode ser combinado com as opções `-i`, `-t`, `-it`, `-rm`, `-p`, `-d`, `--name`. Ver em [Opções comuns](#opções).


### **pull**

Baixa uma imagem do registry para a máquina local.

```bash
  docker image pull <docker-image>:<version>
```

### **push**

Envia uma imagem para o registry.

```bash
  docker image push <docker-image>:<version>
```

### **tag**
Cria uma tag para uma imagem. As tags são utilizadas para identificar versões de uma imagem.
São como um ponteiro para uma imagem.

```bash
  docker image tag <docker-image>:<version> <docker-image-tag>:<nova-versao>
```

### **create**
Cria um container a partir de uma imagem.
```bash
  docker container create <docker-image>
```


### **start**
Inicializa um container.
```bash
  docker container start <container-id>
```
Pode ser combinado com as opções `-a`, `-i`, `-d`. Ver em [Opções comuns](#opções).

### **stop**
Para um container em execução.
```bash
  docker container stop <container-id>
```

### **restart**
Reinicia um container.
```bash
  docker container restart <container-id>
```

### **rm**
Remove um container.
```bash
  docker container rm <container-id>
```

### **exec**
Executa um comando em um container em execução.
```bash
  docker container exec <container-id> <comando>
```

### **logs**
Exibe os logs de um container.
```bash
  docker container logs <container-id>
```

### **inspect**
Exibe informações detalhadas sobre um container.
```bash
  docker container inspect <container-id>
```

## **Opções comuns**

- `-h` | `--help`: Exibe a ajuda do comando.
```bash
  docker --help
```

- `-p` | `--port`: Mapeia uma porta.
```bash 
    -p <porta-host>:<porta-container>
```

- `-v` | `--volume`: Mapeia um volume.
```bash
  -v <caminho-diretorio-host>:<caminho-diretorio-container>
```

- `-i` | `--interactive`: Modo interativo.
```bash
  docker container run -i <container-id>
```

- `-t` | `--tty`: Acesso ao terminal.
```bash
  docker container run -t <container-id>
```

- `-it`: Modo interativo e terminal. Usa-se junto com o comando `run`.
```bash
  docker container run -it <container-id>
```

- `-ai`: Modo interativo e acesso ao terminal. Usa-se junto com o comando `start`.
```bash
  docker container run -ai <container-id>
```

- `-f` | `--force`: Força a execução do comando.
```bash
  docker container rm -f <container-id>
```

- `-q` | `--quiet`: Exibe apenas o ID do recurso.
```bash
  docker container ls -q
```

- `-l` | `--latest`: Exibe o último recurso criado.
```bash
  docker container ls -l
```

- `-n` | `--no-trunc`: Exibe o nome completo do recurso.
```bash
  docker container ls -n
```

- `-s` | `--size`: Exibe o tamanho do recurso.
```bash
  docker container ls -s
```

- `-a` | `--all`: Exibe todos os recursos.
```bash
  docker container ls -a
```

- `-q` | `--quiet`: Exibe apenas o ID do recurso.
```bash
  docker container ls -q
```

- `-d` | `--detach`: Modo detached. Executa o container em segundo plano.
```bash
  docker container run -d <container-id>
```

- `--name`: Atribui um nome ao container.
```bash
  docker container run --name <nome> <container-id>
```