# Tutorial #7

O presente relatório tem como objetivo descrever o processo seguido para a resolução da ficha `Tutorial #7`, disponibilizada no âmbito da disciplina de Criptografia Aplicada. As seções numeradas em baixo representam cada um dos exercícios resolvidos.

## Diffie-Hellman com OpenSSL e SageMath

**1) Produza parâmetros Diffie-Hellman com 128-bit (4096-bit modulus) security, sem recorrendo à opção *dsaparam* do OpenSSL**

É possivel recorrer ao OpenSSL para produzir os parâmetros Diffie-Hellman através do seguinte comando:

`openssl dhparam <bit_modulus_size> -out <generated_parameters_filepath> (35 min)`

Onde `<bit_modulus_size>` corresponde ao número de bits do qual o operador modulus deve processar, e `generated_parameters_filepath` o caminho e nome do ficheiro a ser gerado com a informação dos parâmetros. Para o exercicio em concreto foi então utilizado o valor **4096** para o número de bits, como demonstrando no seguinte comando:

`openssl dhparam 4096 -out 4096-dh-parameters-no-dsaparam`

Esta operação demorou cerca de **35** min a terminar.

**2) Produza parâmetros Diffie-Hellman com 128-bit (4096-bit modulus) security, recorrendo à opção *dsaparam* do OpenSSL**

Da mesma forma que no exercício 1), é possível produzir os parâmetros Diffie-Hellman recorrendo à opção `-dsaparam`, de uma forma mais eficiente. Esta opção indica ao OpenSSL para usar o algoritmo *ECDSA* (Eliptic Curve Digital Signature Algorithm) em vez do Diffie-Hellman na produzação dos parâmetros, convertendo estes para o formato Diffie-Hellman no final.

O seguinte comando foi utilizado para produzir os parâmetros, demorando cerca de **10** segundos para concluir a operação:

`openssl dhparam 4096 -dsaparam -out 4096-dh-parameters-dsaparam`

**3) Comente porque a primeira abordagem é mais demorosa, usando o Sage para confirmar a mesma**

A primeira abordagem produz os parâmetros Diffie-Hellman da forma mais "legítma", sendo um processo demorado pois é necessário gerar valores primos de 4096 bits até que a condição modulus seja satisfeita. Como referido, na segunda abordagem é utilizado o algoritmo ECDSA para gerar os parâmetros, convertendo os mesmos no formato Diffie-Hellman antes de produzir o output final. Enquanto este último produz números primos com um tamanho suficientemente grande para produzir a chave, no caso do Diffie-Hellman os números primos são produzidos onde a condição `is_prime((p - 1) / 2)` se satisfaz, sendo **p** o número primo a ser produzido.

É possível intepretar o valor primo usado para os parâmetros produzidos através da ferramenta openSSL. Usando o seguinte comando, podemos guiar o openSSL a imprimir o valor primo em hexadecimal, como também pedir a sua avaliação relativamente à segurança do número primo:

```
openssl dhparam -in <generated_parameters_filepath> -check -text
```

Executando o comando para os parâmetros produzidos com a opção `-dsaparam`, obtemos o seguinte aviso:

```
p value is not a safe prime
```

Já para os parâmetros produzidos sem a opção, é nos informado que o número primo aparenta estar *ok*.

```
DH parameters appear to be ok.
```

Importando o valor hexadecimal no Sage e convertendo o mesmo num valor inteiro, podemos comprovar que valor com a opção `-dsaparam`, não é de facto um valor primo seguro.

```
hex_4096_dh_parameters_no_dsaparam = '00:c0:7e:12:09:54:73:99:14:32:5c:d9:82:44:4b:84:bf:41:92:bf:8c:bd:c4:8a:77:74:42:5a:b1:d0:97:22:97:8d:2e:2b:7c:60:e5:7d:dc:2e:50:13:a6:ee:41:9b:01:a5:e9:d1:a0:07:27:1d:5c:40:63:ec:5d:12:0f:fb:67:7f:51:f2:2e:e6:9c:92:1a:77:8c:cb:65:70:a5:51:7b:35:41:bb:06:a4:13:f2:4a:00:72:a8:40:3e:c8:fb:3c:5a:18:e0:1e:cb:78:4e:e5:6d:75:00:1f:79:7a:0e:07:e6:68:53:2a:85:30:9a:62:dc:58:7c:74:c6:d2:68:2a:87:26:28:a7:c9:bd:c2:8c:e9:d3:0f:51:91:b1:86:96:56:05:74:43:af:80:f3:fd:f3:c2:02:8c:9c:50:41:08:96:41:1f:03:1d:e4:c7:69:5e:e5:eb:f8:b3:78:e9:62:d8:47:ae:c3:7b:3b:16:09:7c:a9:af:5b:ad:7d:a0:6f:a7:fe:46:a9:d0:ec:f2:da:7a:e0:cb:c7:16:64:da:ad:48:7d:32:41:b6:2d:a6:eb:38:bc:b2:50:47:d2:45:2e:ae:33:09:e9:dc:7d:d8:8b:75:0c:12:0f:f9:0f:87:7b:f6:43:7c:79:1f:ef:e7:78:47:18:5a:65:26:e5:c8:df:fc:9a:b5:a2:d1:cd:0b:28:a6:db:3e:3a:96:3c:17:09:e2:4e:47:0b:7e:ad:b5:3c:59:2e:8e:b7:5b:b8:cc:2c:4c:25:4f:bd:f1:6e:7a:2a:9a:9a:d3:39:e0:43:80:ce:94:be:18:90:83:54:91:40:67:7e:9e:2f:c8:36:57:dd:ce:9e:02:db:6c:d6:15:5f:05:fe:f3:45:06:54:35:00:59:b1:cb:52:86:6f:d2:01:9a:26:04:8c:53:0b:06:ea:59:73:80:31:1e:76:7e:8d:3e:ef:b6:30:02:86:56:dd:6e:52:db:5c:35:0c:bd:1d:0e:1b:26:5d:ae:16:52:83:da:f2:12:98:7f:88:a6:c5:85:bb:7f:a5:a6:b8:e3:b6:cd:70:1f:e0:24:78:31:f5:ca:37:94:d5:1d:c4:91:6d:09:43:f5:75:61:9f:3a:3b:68:b4:79:4c:5f:19:d3:57:b2:84:67:17:5f:50:0d:b0:0f:61:83:e9:e3:aa:73:c1:27:ff:a2:c1:00:98:4f:94:e2:41:99:0f:48:33:eb:58:83:cb:a4:a5:ad:5d:0b:c2:7b:23:8a:ba:49:58:c5:61:4c:63:9d:7a:d2:f7:2a:1b:3b:70:22:7a:bd:c9:92:a0:d9:58:6c:13:f4:0d:26:ba:bf:12:8f:06:04:17:6b:5b'
hex_4096_dh_parameters_with_dsaparam = '00:a5:80:69:6e:a5:8b:f3:cb:04:e4:26:fb:0a:88:93:49:d5:20:d2:f4:f2:ee:a4:a0:51:05:51:7e:c7:0d:01:ed:56:2c:fa:6c:20:19:bc:c8:c6:3d:77:a0:24:2f:b4:f2:73:ec:76:32:06:24:02:e3:da:ab:f7:42:3d:89:88:f1:5a:68:14:8d:2c:f3:95:cb:10:15:da:09:0b:7c:67:40:27:cf:4a:d2:4e:ad:8f:d2:a1:10:8d:a6:ea:69:40:ba:84:b9:24:ae:36:09:da:db:83:83:73:73:87:08:05:c2:e2:c4:95:78:7c:19:1b:98:cc:8d:e8:43:3f:40:93:51:e8:f7:6d:1f:c9:9e:2b:b7:8b:aa:4c:a0:96:11:03:a3:14:a1:76:94:57:1d:90:c2:df:b9:b5:1f:32:71:56:4a:cb:15:48:67:ba:0d:03:fa:87:36:de:21:df:b9:7a:68:28:5c:2c:ed:49:64:0e:99:ed:ed:92:af:b7:1e:84:ef:64:02:57:d0:3c:b6:ff:07:21:39:a6:25:ba:27:21:7e:a6:9b:81:6d:e1:5e:7c:56:46:04:65:3d:c8:b6:99:7d:9f:e5:ce:7d:80:f5:d3:53:93:97:cf:76:61:eb:dd:43:1f:47:84:8c:be:72:cf:ae:bb:11:30:c0:73:a9:05:98:16:11:d0:78:43:a8:cd:b1:99:2e:f0:cb:15:0f:5f:d8:a3:bd:28:20:c7:a1:54:1a:d4:30:bd:29:12:29:af:6f:46:95:56:a5:60:1e:c3:b7:94:63:a1:b4:dd:48:29:4f:36:4f:58:8d:fa:05:51:7b:23:c9:c4:2b:4d:6b:d9:2c:01:9c:9a:08:93:40:5b:21:a1:e1:e9:5e:8b:dd:46:5c:eb:8d:ad:e0:b6:94:8b:24:d9:05:bb:61:c9:9f:27:a8:5f:28:e6:6e:4f:bf:64:2c:d7:b6:97:cb:51:73:8b:b7:78:f1:ac:26:cb:38:c6:b8:32:11:c5:fb:6a:26:9f:95:b1:25:f2:ef:b2:6b:a2:47:46:71:4b:d7:ce:27:8a:08:82:b7:25:00:71:8d:2c:29:0c:03:a4:2e:63:d0:a6:4c:52:fe:25:ad:59:47:e4:d2:4d:26:c3:16:8e:d7:41:a7:56:90:78:56:62:bf:b7:ff:cd:cf:64:9d:38:21:b6:1d:1b:2f:05:80:3c:cc:45:3e:9f:20:08:99:0c:8a:ce:54:c9:87:c0:9d:8a:f8:8a:90:32:ba:43:d1:78:fe:d7:04:8f:be:34:42:ad:ed:4d:f8:68:8d:7d:e4:71:ed:20:09:30:bd:df:8c:12:a6:9d:8c:c8:05:ca:01:6b:2c:5f:85'

def hex_to_bigint(hex_string):
    hex_split = hex_string.split(":")[::-1]
    bigint = 0
    byte_value = 1
    bit8 = 256
    
    for i in hex_split:
        hex_int = int(i, 16)
        bigint += hex_int*byte_value
        byte_value *= bit8
    
    return bigint

def is_safe_prime(prime):
    return ((prime - 1) / 2).is_prime()

bigint_4096_dh_parameters_no_dsaparam = hex_to_bigint(hex_4096_dh_parameters_no_dsaparam)
bigint_4096_dh_parameters_with_dsaparam = hex_to_bigint(hex_4096_dh_parameters_with_dsaparam)

assert(is_safe_prime(bigint_4096_dh_parameters_no_dsaparam))
assert(is_safe_prime(bigint_4096_dh_parameters_with_dsaparam) == False)
```

**4) Utilize o Sage para verificar que a utilização de Diffie-Hellman funciona, utilizando os parâmetros produzidos para**

1. Produzir exponentes *x*, *y* sobre a distribuição `[0, q[`, onde *q* é a ordem do grupo produtor;

2. Calcular `X = g^x mod(p)` e `Y = g^y mod(p)`;

3. Verificar que `X^y mod(p) = Y^x mod(p)`.

Traduzindo estas expressões no Sage, obtemos os seguinte código:

```
from random import seed, randint

seed(1)

p1 = bigint_4096_dh_parameters_no_dsaparam
p2 = bigint_4096_dh_parameters_with_dsaparam
q = randint(0, bigint_4096_dh_parameters_no_dsaparam)

x = randint(0, q-1)
y = randint(0, q-1)

g = (GF(p1))(p2) # ???

X = (g^x) % p
Y = (g^y) % p

Xy = (X^y) % p
Yx = (Y^x) % p

assert(Xy == Yx)
```

**5) Seja p=1373, g=2, X=974, y=871, qual o valor Y e o valor secreto da Alice (x)?**

Tendo com base as expressões préviamente definidas, podemos concluir que:

```
Y = g^y (mod(p))
= 2^871 (mod(1373))
= 805
```

Sabendo também que `X^y (mod(p)) = Y^x (mod(p))` então:

```
X^y (mod(p)) = Y^x (mod(p))
= 974^y (mod(1373)) = 805^871 (mod(1373))
= log_974(805^871 (mod(1373))) (mod(1373)) = y // 1)
= 1.0041186286870067 = y
```

Em 1) inverte-se a condição exponencial de modo a obter a versão logarítmica:

```
2^k=c
log2(c)=k
```