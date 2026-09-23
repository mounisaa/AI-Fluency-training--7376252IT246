# Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

My private-data scenario is a Student Assignment Assistant.

The private data is stored in a JSON file named `student_data.json`.
It contains assignment names, subjects, deadlines, priorities, and completion
statuses.

The user asks:

"What should I work on first from my pending assignments?"

The same problem is solved using a plain chatbot, a rule-based workflow,
and an AI agent.

---

## 2. Plain Chatbot

The plain chatbot mainly uses an LLM to understand the user's message and
generate a response. It does not use tools or a predefined workflow.

In my implementation, the chatbot does not access the private
`student_data.json` file. Therefore, it cannot directly know which
assignments are pending or which assignment has the nearest deadline.

The processing is mainly:

User request → LLM → Response.

The main limitation is that the chatbot cannot automatically retrieve
the private assignment information. It can give general advice, but it
cannot make a decision based on the actual private data.

---

## 3. Rule-Based Workflow

The rule-based workflow uses predefined programming rules instead of an LLM.

In my implementation, the workflow reads the private JSON file and checks
the status of each assignment. If the status is "Pending", the assignment
is selected. The pending assignments are then sorted according to their
deadline.

The workflow therefore has direct access to the private data.

The processing is:

Read data → Apply predefined rules → Sort tasks → Display result.

The advantage is that the workflow is predictable and repeatable. However,
it is less flexible because the conditions have to be explicitly programmed.
If the user asks a completely different type of question, additional rules
may need to be written.

---

## 4. AI Agent

The AI agent combines an LLM-style decision-making component with tools and
an iterative loop.

In my implementation, the agent has tools for reading private data,
finding pending assignments, and checking deadlines and priorities.

The agent receives the user's request and determines that it needs
information from the private assignment file. It uses the data-reading tool,
observes the result, then uses another tool to identify pending assignments.
It then checks deadlines and priorities before producing the final answer.

The basic agent architecture is:

LLM + Tools + Loop.

The loop allows the agent to observe the result of one action and continue
with another action until the task is completed.

The agent is therefore more suitable for multi-step tasks where different
tools may need to be used.

---

## 5. Comparison Table

| Basis | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | High for conversation, but limited access to private data | Low to medium because rules are predefined | High because it can decide which tools/actions are needed |
| Decision-making | Generates a response using the LLM | Uses fixed conditions | Uses reasoning and tool results to decide next actions |
| Tool usage | No tools | Uses predefined program operations | Selects and uses available tools |
| Private-data access | No direct access in this implementation | Yes | Yes |
| Multi-step task handling | Limited | Possible if explicitly programmed | Strong because actions can be performed iteratively |
| Automation | Low | High for predefined tasks | High for dynamic multi-step tasks |
| Reliability | Depends on generated response | High and predictable for known rules | Depends on agent decisions and tools |

---

## 6. Suitability Analysis

For my scenario, the AI agent is suitable when the user expects the system
to perform multiple steps using private data and then decide what action
should be taken.

The plain chatbot is useful for general conversation, but it cannot directly
retrieve my private assignment information in this implementation.

The rule-based workflow can access the private data and reliably identify
pending assignments. However, its behavior depends on predefined rules.

The AI agent can combine private-data access, multiple tools, observations,
and decision-making. Therefore, it can handle a more flexible version of
the assignment-assistance problem.

For a simple fixed task such as listing all pending assignments, a
rule-based workflow may be sufficient. For a dynamic request that requires
multiple steps and tool selection, the agent architecture is more suitable.

---

## 7. Conclusion

A plain chatbot is appropriate when the main requirement is natural-language
conversation, explanation, question answering, or generating text without
requiring external tools.

A rule-based workflow is appropriate when the task is predictable and the
required steps and conditions are known in advance. It is useful when
consistent and deterministic behavior is important.

An AI agent is appropriate when a task requires multiple steps, access to
tools or private data, observation of results, and decisions about what
action to take next. The agent can combine an LLM with tools and a loop to
continue working toward the requested result.

Therefore, the three approaches are useful for different types of problems.
The appropriate approach depends on the complexity, flexibility, data
access, and automation requirements of the task.