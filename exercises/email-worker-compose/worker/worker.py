import redis
import json
import os
from time import sleep
from random import randint

if __name__ == '__main__':
    ## Conectar ao Redis
    redis_host = os.getenv('REDIS_HOST', 'queue')
    r = redis.Redis(host=redis_host, port=6379, db=0)

    print('Aguardando mensagens na fila...')

    while True:
        mensgem = json.loads(r.blpop('sender')[1])
        ## Simular o envio de email...
        print('Mandando a mensagem:', mensgem['assunto'])
        sleep(randint(1, 5))
        print('Mensagem', mensgem['assunto'], 'enviada')
