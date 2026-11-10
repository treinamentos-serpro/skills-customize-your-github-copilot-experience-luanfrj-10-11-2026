# 📘 Atividade: Testes Avançados com Java

## 🎯 Objetivo

Pratique testes automatizados avançados em Java usando JUnit 5 e Mockito. Você vai testar regras de domínio com diferentes entradas, isolar dependências em testes unitários e verificar o fluxo completo de empréstimo com implementações em memória.

## 📝 Tarefas

### 🛠️ Testar Regras com Parâmetros

#### Descrição
Configure um projeto Maven com Java 17 ou superior e JUnit Jupiter. Implemente `LoanPolicy.isValidPeriod(int days)`, que aceita períodos de empréstimo entre 1 e 30 dias, inclusive, e teste a regra com testes parametrizados.

#### Requisitos
O programa concluído deve:

- Usar `@ParameterizedTest` com `@ValueSource` ou `@CsvSource`
- Verificar períodos válidos e inválidos, incluindo os limites 1 e 30 e valores fora deles
- Manter os testes independentes entre si e executáveis com `mvn test`

### 🛠️ Isolar o Serviço com Mockito

#### Descrição
Crie `LoanService`, dependente de `BookRepository` e `NotificationSender`, e escreva testes unitários para o método `borrow(long bookId, String studentId)`. O método deve lançar `BookNotFoundException` quando o livro não existir e `BookUnavailableException` quando já estiver emprestado. No sucesso, deve marcar o livro como indisponível, salvá-lo e enviar uma notificação ao aluno.

#### Requisitos
O programa concluído deve:

- Usar JUnit Jupiter e `mockito-junit-jupiter` para criar mocks das dependências
- Configurar os retornos do repositório para os cenários de sucesso, livro inexistente e livro indisponível
- Verificar as exceções esperadas e que o repositório salva o livro apenas no sucesso
- Verificar que a notificação é enviada uma vez no sucesso e não é enviada quando ocorre uma exceção

### 🛠️ Verificar a Integração em Memória

#### Descrição
Teste o fluxo de `LoanService` com implementações em memória de `BookRepository` e `NotificationSender`, sem mocks, banco de dados ou serviços externos.

#### Requisitos
O programa concluído deve:

- Preparar dados isolados para cada teste, sem depender da ordem de execução
- Confirmar que um empréstimo bem-sucedido atualiza o estado do livro e registra a notificação
- Confirmar que uma tentativa inválida deixa os dados inalterados
- Executar a suíte completa com `mvn test`
