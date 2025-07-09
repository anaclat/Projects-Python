# `__init__` em Python

O método `__init__` é o **construtor de uma classe**.  
Ele é chamado automaticamente quando um novo objeto é criado.

## Para que serve?

- Inicializar os atributos do objeto, ou seja, **definir os dados** da instância no momento em que ela é criada.

---

# `self` em Python

`self` é uma **referência ao próprio objeto da classe**.

Sempre que você cria um objeto e chama um método, o Python passa automaticamente o objeto atual como o primeiro argumento.  
Por convenção, esse argumento se chama `self`.

## Para que serve?

- Acessar **atributos e métodos** do próprio objeto;
- Diferenciar **variáveis locais** de **atributos do objeto** (instância).