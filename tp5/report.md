# Tutorial #5

O presente relatório tem como objetivo descrever o processo seguido para a resolução da ficha `Tutorial #5`, disponibilizada no âmbito da disciplina de Criptografia Aplicada. As seções numeradas em baixo representam cada um dos exercícios resolvidos.

## Diffie-Hellman com OpenSSL e SageMath

**1) Implement the universal hash function of poly1305 in Sage**



**3) Complexidade Computacional usando a Notação Big O**

No presente exercício é pedido que um conjunto de comparações usando a notação Big O sejam confirmadas. Estas são:

```
1) 2n = O(n) // V
2) n^2 = O(n) // F
3) n^2 = O(nlog(n)) // F
4) nlog(n) = O(n^2) // V
5) 3^n = O(2^n) // F
6) O(2^(n^2)) = 2^O(n^2) // F
```

A afirmação 1) é verdadeira, pois a notação Big O especifica que funções com crescimento semelhante (n - linear), mas com constantes diferentes (2), tem a mesma complexidade dada pelo crescimento da função (n). No mesmo sentido, a afirmação 2), 3) são falsas, pois o crescimento de uma função exponêncial (n^2) é diferente do crescimento de uma função linear (n) e logarítmica (nlog(n)).

A afirmação 4) é verdadeira, pois apesar do crescimento de `n^2` ser maior que `nlog(n)`, como ambas não estão expressas com a notação Big O, esta afirmação não pode ser confirmada. Como nlog(n) "instruções cabem" dentro da função `n^2`, podemos considerar esta afirmação como verdadeira.

A afirmação 5) é falsa, pois tal como referido na 4), `3^n` cresce mais rápido do que `2^n`. Para finalizar, a afirmação 6) também é falsa pois `2^O(n^2)` tem um crescimento superior.