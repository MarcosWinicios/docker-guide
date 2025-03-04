# Dockerfile

Um Dockerfile é um arquivo de configuração que contém instruções para construir uma imagem Docker. 
O Dockerfile é usado para automatizar o processo de construção de imagens Docker.

### FROM 

A instrução `FROM` é a primeira instrução em um Dockerfile. Ela define a imagem base que será usada para construir a nova imagem. 
A instrução `FROM` é obrigatória em um Dockerfile.

```Dockerfile
FROM <image>:<tag>
```
**Nota:** A tag é opcional. Se não for especificada, o Docker usará a tag `latest` por padrão. Em ambientes de produção, é recomendável especificar a tag para garantir a reprodutibilidade e a consistência.

### RUN

A instrução `RUN` é usada para executar comandos durante a construção da imagem. 
Ela executa os comandos especificados no shell do contêiner e cria uma nova camada na imagem. 
A instrução `RUN` é usada para instalar pacotes, configurar o ambiente, baixar arquivos, etc.

```Dockerfile
RUN <command>
```

### CMD

A instrução `CMD` é usada para especificar o comando padrão que será executado quando o contêiner for iniciado.

```Dockerfile
CMD ["executable", "param1", "param2"]
```

### ENTRYPOINT

A instrução `ENTRYPOINT` é usada para especificar o comando que será executado quando o contêiner for iniciado.

```Dockerfile
ENTRYPOINT ["executable", "param1", "param2"]
```

**Nota:** A diferença entre `CMD` e `ENTRYPOINT` é que `CMD` é substituído quando um comando é passado ao contêiner, enquanto `ENTRYPOINT` é mantido e o comando é passado como argumento para o `ENTRYPOINT`.

### ADD

A instrução `ADD` é usada para copiar arquivos e diretórios do host para o contêiner.

```Dockerfile
ADD <source> <destination>
```

### COPY

A instrução `COPY` é usada para copiar arquivos e diretórios do host para o contêiner.

```Dockerfile
COPY <source> <destination>
```

**Nota**: A diferença entre `ADD` e `COPY` é que `ADD` permite a cópia de arquivos remotos e a descompactação de arquivos tar automaticamente, enquanto `COPY` é mais simples e só copia arquivos locais.

### WORKDIR

A instrução `WORKDIR` define o diretório de trabalho para os comandos `RUN`, `CMD`, `ENTRYPOINT`, `COPY` e `ADD` que seguem a instrução.

```Dockerfile
WORKDIR /path/to/directory
```

### LABEL

A instrução `LABEL` é usada para adicionar metadados à imagem.

```Dockerfile
LABEL key="value"
```

### ARG

A instrução `ARG` é usada para definir variáveis de ambiente que podem ser usadas durante a construção da imagem.

```Dockerfile
ARG <variable>
```

### ENV

A instrução `ENV` é usada para definir variáveis de ambiente no contêiner.

```Dockerfile
ENV key="value"
```

**Nota**: A diferença entre `ARG` e `ENV` é que `ARG` é usado durante a construção da imagem, enquanto `ENV` é usado durante a execução do contêiner.
É possível combinar `ARG` e `ENV` para definir variáveis de ambiente que podem ser substituídas durante a construção da imagem.

Exemplo:

```Dockerfile
ARG user
ENV USER=${user}
```

