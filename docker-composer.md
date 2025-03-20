# Docker compose

Docker compose é uma ferramenta para definir e executar aplicativos Docker multi-container. Com o Docker Composer, você usa um arquivo YAML para configurar seus serviços. Em seguida, com um único comando, você cria e inicia todos os serviços a partir de sua configuração.

# Conceitos
- **version**: Versão do docker-compose.yml. Define quais funcionalidades estão disponíveis. Deve ser a primeira linha do arquivo.

- **Services**: São os containers que compõem a aplicação. Cada serviço é uma imagem Docker que será executada.
    - **container_name**: Nome do container. Equivalente ao comando `docker run --name`.
    - **image**: Imagem Docker que será utilizada para criar o container do serviço. Equivalente ao comando `docker run`.
    - **Volumes**: Mapeia um diretório do host para um diretório do container. Equivalente ao comando `docker run -v`.
    - **ports**: Mapeia uma porta do host para uma porta do container. Equivalente ao comando `docker run -p`.
    - **environment**: Define variáveis de ambiente. Equivalente ao comando `docker run -e`.
    - **depends_on**: Define dependências entre serviços. O serviço dependente só será iniciado após o serviço de que depende.
    - **networks**: Define a rede que o container fará parte. Equivalente ao comando `docker network connect`.
    - **restart**: Define a política de reinicialização do container. Valores possíveis: 
      - `no`: nunca
      - `always`: sempre
      - `on-failure`: apenas em caso de falha
      - `unless-stopped`: a menos que seja parado manualmente
    - **command**: Comando que será executado ao iniciar o container. Equivalente ao comando `docker run`.

# Comandos

- **`docker compose up`**: Cria e inicia os containers. Deve ser executado na pasta onde está o arquivo docker-compose.yml.
- **`docker compose down`**: Para e remove os containers.
- **`docker compose ps`**: Lista os containers.
- **`docker compose logs`**: Exibe os logs dos containers.
- **`docker compose exec`**: Executa um comando dentro de um container.