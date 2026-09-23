# Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 3.1 Explanation of Each Approach

### Scenario

For this project, I selected a personal student assignment management
scenario. The purpose is to help a student identify pending assignments
and determine which assignment should be worked on first.

The private information is stored in a file named `student_data.json`.
The file contains assignment subjects, task descriptions, deadlines,
priorities, and completion statuses.

The main user request used for the comparison is:

> "What should I work on first from my pending assignments?"

The same problem is implemented using three different approaches:
a plain chatbot, a rule-based workflow, and an AI agent.

---

### 1. Plain Chatbot

A plain chatbot mainly uses an LLM to understand a user's question and
generate a natural-language response. It does not use external tools or
predefined program rules in this implementation.

For this scenario, the plain chatbot does not directly access the private
`student_data.json` file. Therefore, it does not know the actual pending
assignments, deadlines, or priorities stored in the file.

When the user asks a question, the chatbot receives the user's message
and generates a response. The basic process is:

**User request → LLM → Response**

The main limitation in this scenario is private-data access. Since the
chatbot cannot read the private assignment file, it cannot accurately
identify the student's actual pending assignments or determine which one
has the nearest deadline.

A plain chatbot is therefore useful for general conversation and advice,
but the implementation used in this project does not provide direct
access to the student's private assignment data.

---

### 2. Rule-Based Workflow

The rule-based workflow does not use an LLM. Instead, it follows
predefined programming steps and conditions.

In this scenario, the workflow reads the private `student_data.json` file.
It checks the status of every assignment and selects assignments whose
status is `Pending`. It then sorts the pending assignments according to
their deadlines and displays the results.

The process is:

**Read private data → Apply predefined rules → Check status → Sort by deadline → Display result**

The workflow can access the private data because the Python program
explicitly reads the JSON file.

The main advantage of this approach is that its behavior is predictable
when the predefined rules are correct. However, it has limited flexibility.
If the user asks a different type of question that was not considered when
the rules were written, the program may require additional rules or code.

For example, the current workflow is designed to identify and display
pending assignments. It does not dynamically decide what tools are
required based on a new natural-language request.

---

### 3. AI Agent

An AI agent is designed around the concept:

**Agent = LLM + Tools + Loop**

Unlike a plain chatbot, an agent can use tools to obtain information.
Unlike a fixed workflow, an agent can use the results of previous actions
to determine what action should be performed next.

For this scenario, the agent uses tools to access the private assignment
data, identify pending assignments, and check deadlines and priorities.

The agent follows a multi-step process:

**User request → Understand the task → Select a tool → Use the tool → Observe the result → Decide the next action → Use another tool → Final answer**

In the implementation, the agent first reads the private student data.
It then identifies pending assignments. After that, it checks deadlines
and priorities and determines which assignment should be worked on first.

The loop can be represented as:

**Request → Tool → Observe → Decide → Tool → Observe → Final Answer**

This demonstrates the important idea of an agent performing multiple
actions rather than simply producing a single response.

The agent can access private data through its tools. Its main limitation
is that the quality of the result depends on the correctness of the tools,
the data, and the agent's decisions. More complex agent systems can also
require additional safeguards and validation.

---

## 3.2 Comparison Table

| Basis for comparison | Plain chatbot | Rule-based workflow | AI agent |
|---|---|---|---|
| Flexibility | Can understand natural-language questions, but cannot access the private file in this implementation. | Limited because the behavior is defined by fixed rules. | More flexible because it can decide which actions and tools are needed. |
| Decision-making | Generates a response using an LLM. | Follows predefined programming conditions. | Uses the request and observed tool results to decide the next action. |
| Tool usage | No tools are used in this implementation. | Uses predefined program operations. | Uses tools to read private data and process task information. |
| Private-data access | No direct access to `student_data.json` in this implementation. | Yes, the workflow directly reads the JSON file. | Yes, the agent uses a tool to access the JSON file. |
| Multi-step task handling | Limited because it mainly generates a response. | Can perform multiple steps if they are explicitly programmed. | Can perform multiple steps through its tool-use loop. |
| Automation | Limited for this scenario. | High for tasks with known rules. | High for dynamic multi-step tasks. |
| Reliability | Depends on the generated response and the information provided to it. | Predictable when the predefined rules and data are correct. | Depends on the agent's decisions, tools, and quality of the underlying data. |

---

## 3.3 Suitability Analysis

For this student assignment scenario, an AI agent is suitable when the
system needs to handle a request that involves multiple steps, private
data, tools, and decisions based on the results of previous actions.

The plain chatbot can understand the user's natural-language question,
but in this implementation it cannot directly access the private
assignment file. Therefore, it cannot determine the actual pending
assignments from the stored data.

The rule-based workflow can access the private data and reliably identify
pending assignments. It is predictable because its behavior is controlled
by predefined conditions. However, its flexibility is limited because
new types of requests may require new rules to be programmed.

The AI agent can combine tool usage, private-data access, multiple steps,
observation of results, and decision-making. It can therefore handle a
more dynamic version of the assignment-assistance task.

For a simple task such as displaying all pending assignments, a
rule-based workflow can be sufficient. For a request that requires
multiple actions and decisions, the agent approach provides a more
flexible architecture.

---

## 3.4 Conclusion

The three approaches are useful for different types of problems.

A **plain chatbot** is appropriate when the main requirement is natural
conversation, answering general questions, explaining concepts, or
generating text without requiring access to external tools or private
data.

A **rule-based workflow** is appropriate when the task is predictable
and the required steps and conditions are known in advance. It is useful
when consistent and repeatable behavior is important. Examples include
checking predefined conditions, validating input, or processing data
according to fixed business rules.

An **AI agent** is appropriate when a task requires multiple steps,
access to tools or private data, observation of results, and decisions
about what action should be taken next. The agent can combine an LLM
with tools and a loop to work toward completing the user's request.

Therefore, the choice between a chatbot, rule-based workflow, and AI
agent depends on the requirements of the problem. Simple conversational
tasks can use a chatbot, predictable tasks can use rule-based workflows,
and more dynamic multi-step tasks can use an agent architecture.