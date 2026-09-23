# Agentic AI: Foundations and Open-Source Practice

## Day 1 Task: From Prompt to Action

## 1. Scenario

For this task, I selected a simple student marks percentage scenario.

The system receives questions related to general AI knowledge, general factual information, and numerical calculations.

I used the following questions:

1. What is an LLM in simple words?
2. What is the capital of France?
3. A student scored 45 marks out of 50. What is the percentage?

The first two questions can be answered directly by an LLM. The third question involves a numerical calculation, so I created one external tool called `calculate_percentage`.

The purpose of this project is to compare a plain LLM with an LLM that has access to one external tool.

---

# 2. What is a Large Language Model?

A Large Language Model, or LLM, is an artificial intelligence model trained using a large amount of text. It learns patterns in language and can generate human-like responses to user questions.

In my scenario, the LLM can answer a question such as "What is an LLM in simple words?" using its learned knowledge.

It can also answer a common factual question such as "What is the capital of France?"

However, a plain LLM does not automatically have access to external programs, databases, calculators, files, or live information.

For example, my percentage question is:

"A student scored 45 marks out of 50. What is the percentage?"

A language model may be able to calculate this itself, but in my experiment the plain LLM was not given any external calculation tool.

The tool-enabled version was given a specific percentage calculator. This allowed the calculation to be performed by an external Python function.

---

# 3. What is an Agent?

An AI agent is a system where an LLM can understand a task and interact with external tools when they are needed.

A normal LLM response mainly consists of generating an answer to the user's prompt.

An agentic system can perform additional actions. It can decide that a tool is useful, call the tool with appropriate parameters, receive the result, and then use that result to generate the final answer.

In my project, the plain LLM directly answers the percentage question.

The tool-enabled system has access to the `calculate_percentage` function. When the model determines that the calculation tool is relevant, it makes a tool call.

The tool calculates the percentage and returns the result to the model.

The model then uses the returned result to generate the final answer.

---

# 4. What is a Tool?

A tool is an external function or capability that an LLM can use to perform a particular operation.

In my project, the tool is:

`calculate_percentage(value, total)`

The function receives two values:

- `value` - the marks obtained by the student
- `total` - the total marks

It calculates the percentage and returns the result.

The tool definition contains information about the tool name, description, and parameters.

For example, the tool description tells the model that the function calculates a percentage.

The parameters tell the model that it needs a `value` and a `total`.

The model needs this description because it cannot automatically know what every function in a program does. The tool schema tells the model what capability is available and what information must be provided to use it.

---

# 5. What is a Tool Call?

A tool call is a request from the LLM to execute a particular external tool with specific parameters.

For my scenario, the user asks:

"A student scored 45 marks out of 50. What is the percentage?"

The model can request the following tool operation:

`calculate_percentage(value=45, total=50)`

The Python program receives the request and executes the function.

The function calculates:

`(45 / 50) × 100`

The result is:

`Percentage = 90.00%`

The result is then returned to the LLM.

The LLM uses this result to produce the final answer.

---

# 6. Step-by-Step Tool Call Flow

The tool call in my project follows these steps.

### Step 1: User asks a question

The user asks:

"A student scored 45 marks out of 50. What is the percentage?"

### Step 2: The question is sent to the LLM

The LLM receives the question and also has access to the description of the `calculate_percentage` tool.

### Step 3: The LLM decides whether a tool is relevant

The question requires a percentage calculation, so the calculator tool is relevant.

### Step 4: The LLM makes a tool call

The model requests:

`calculate_percentage(value=45, total=50)`

### Step 5: The Python program executes the tool

The Python function calculates:

`(45 / 50) × 100`

### Step 6: The tool returns the result

The tool returns:

`Percentage = 90.00%`

### Step 7: The result is sent back to the LLM

The LLM receives the tool result.

### Step 8: The LLM produces the final answer

The model generates a final response such as:

"The student's percentage is 90%."

The complete flow is:

**User → LLM → Tool Call → Tool → Tool Result → LLM → Final Answer**

---

# 7. Why Should a Tool Return Its Result as Text?

A tool should return useful information to the model even when the operation fails.

For example, if the total marks were zero, the calculation would not be valid.

Instead of stopping the complete program, the tool can return:

`ERROR: Total cannot be zero.`

The model can then understand the error and explain it to the user.

Returning an error as text keeps the interaction running and allows the LLM to decide how to respond.

This is useful in agentic systems because tools may fail for different reasons, and the model can receive the failure information and react appropriately.

---

# 8. Comparison Table

| Basis | Plain LLM Prompt | LLM With One Tool |
|---|---|---|
| Source of the answer | The model's learned knowledge and generated response | The model's knowledge plus the result returned by the external tool |
| Can it fetch or compute information outside its own memory? | No external tool is available | It can use the provided percentage calculation tool |
| Reliability on factual or numeric questions | The model can often answer correctly, but there is no external tool verification | The specific calculation can be performed by the external tool |
| Transparency | The generated answer does not show an external operation | The tool call, arguments, and tool result can be displayed |
| Speed / cost | No additional tool execution is required | An additional tool call is required |

---

# 9. Observation

I tested three questions using my scenario.

## Question 1

**Question:**

"What is an LLM in simple words?"

### Plain LLM

The plain LLM answered the question directly using its learned knowledge.

### Tool-enabled LLM

The tool-enabled system did not need the percentage calculator because the calculator was not relevant to the question.

### Observation

This shows that a tool is not required for every question.

---

## Question 2

**Question:**

"What is the capital of France?"

### Plain LLM

The plain LLM answered:

"Paris."

### Tool-enabled LLM

The percentage calculator was not required because the question did not involve a percentage calculation.

### Observation

This demonstrates that an agent can answer directly when the available tool is not relevant.

---

## Question 3

**Question:**

"A student scored 45 marks out of 50. What is the percentage?"

### Plain LLM

The plain LLM generated an answer directly.

### Tool-enabled LLM

The tool-enabled version called:

`calculate_percentage(value=45, total=50)`

The tool returned:

`Percentage = 90.00%`

The model then used this result to generate the final answer.

### Observation

This demonstrates the main purpose of tool calling. The LLM can delegate a specific operation to an external function and then use the returned result.

---

# 10. Suitability of the Plain LLM

A plain LLM is suitable when the task mainly requires language understanding, explanation, summarisation, or general knowledge.

For example, the questions about what an LLM is and the capital of France did not require my percentage calculator.

However, tools become useful when the task requires an external operation or information from an external source.

Examples include:

- Calculations
- Database lookups
- Reading files
- Searching external information
- Accessing APIs
- Performing specialised operations

In my scenario, the percentage calculator demonstrates how an external tool can provide an additional capability to the LLM.

---

# 11. Conclusion

This experiment demonstrated the difference between a plain LLM and an LLM with access to a tool.

A plain LLM can answer many questions directly using its learned knowledge. However, it does not automatically have access to external programs or systems.

An agentic system can extend an LLM by providing tools.

The model can identify when a tool is relevant, request the tool with appropriate parameters, receive the result, and use that result in its final response.

My project uses only one simple percentage calculator, but the same concept can be extended to many other tools such as databases, search systems, file readers, weather APIs, and business applications.

Therefore, a plain LLM can be sufficient for many language-based questions, while an external tool becomes useful when a task requires an operation or information that should come from an external source.