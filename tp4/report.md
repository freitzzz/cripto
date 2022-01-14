# Tutorial #4

O presente relatório tem como objetivo descrever o processo seguido para a resolução da ficha `Tutorial #4`, disponibilizada no âmbito da disciplina de Criptografia Aplicada. As seções numeradas em baixo representam cada um dos exercícios resolvidos.

## 1) Stream Cipher RC4

A Alice e Bob concordaram em comunicar através de um canal de comunição cifrado com um esquema baseado no stream cipher RC4. Contudo, estes não querem produzir uma chave secreta a cada transmissão, reutilizando a mesma ao longo das várias sessões de comunicação. Para tal, estes concordaram em usar uma chave *k*, de 128 bits, e para cifrar uma mensagem *m*, o seguinte procedimento:

1. Escolher um valor aleatório *v*, de 80-bit;
2. Produzir a cifra da mensagem `c = RC4(v.k) XOR m`, sendo a concatenação de duas strings;
3. Enviar a bit string `(v.c)` sobre o canal de comunicação.

**a) Supondo que a Alice envia a mensagem *m* cifrada ao Bob, seguinde o procedimento descrito, como pode este recuperar a mensagem original através de k e (v.c)?**

O inverso de uma operação XOR é dado com o XOR do resultado, ou seja:

```
a XOR b = c
c XOR b = a
a XOR c = b
```

Neste modo, como `c = RC4(v.k) XOR m`, então podemos concluir que `m = RC4(v.k) XOR c`.
Tendo (c.v) e sabendo que *v* tem o perído de 80 bits, então para obter *c* é necessário eliminar os últimos 80 bits presentes em (c.v).

Obtendo *c*, aplica-se este sobre a operação XOR a RC4(v.k) e obtem-se *m*.

**b) Se um atacante observar vários valores da bit string produzida (v1.c1, v2.c2, ...), como pode este determinar que a mesma key-stream (output de RC4), foi usada para cifrar duas mensagem diferentes?**

Como é usado sempre a mesma chave como input de RC4, então isso significa que para além de *v* e *m*, não existe nenhum atributo que diferencia as bit-strings produzidas. O output de RC4(v.k) é igual quando usado o mesmo valor aleatório *v*, pois a chave é igual para todas as sessões de comunicação. Com isto e seguindo o mesmo processo descrito anteriormente, é possível obter o valor de (v1, v2, ...) ao eliminar os primeiro 80 bits em (v.c), para se obter *c*. Uma vez sabendo *c*, determina-se o seu período, de forma a que seja possível eliminar este de (c.v), resultando no valor de *v*.

Sabendo este valor, o atacante apenas tem que observar uma repetição do mesmo de forma a comprovar que a mesma keystream foi usada para cifrar duas mensagems diferentes.

**c) Apróximadamente, quantas mensagems terão que ser transmitidas, até que a mesma keystream seja usada duas vezes?**

Uma vez que a keystream depende apenas do valor de *v*, que tem o período de 80-bit, então isso significa que, apróximadamente após `2^80/2 = 2^40` mensagens, irá ocorrer uma colisão.

**d) Escreva um programa Python, que dado um valor *n*, calcula o valor menor presente num conjunto de valores produzidos aleatóriamente, de forma uniforme, tanto que hajam mais números aleatórios repetidos, do que não repetidos**

```
```

**e) Quantas mensagems deve a Alice usar a mesma chave *k*, até produzir uma nova?**

Uma vez reutilizando a mesma chave, torna-se muito mais facil obter o valor produzido por RC4(k.v), estando as colisões neste dependentes de *v*. A melhor solução seria a Alice produzir uma nova chave *k* a cada mensagem enviada. Contudo, como tanto a Alice e Bob querem evitar o envio repetido de novas chaves, podem ser enviadas tantas mensagens até que haja uma possível colisão (2^40).