# Day 2 — Reasoning and Acting

## 1. Scenario

For this task, I selected a college course fee scenario.

The scenario contains three courses:

- CS101 — Rs. 12,000
- AI202 — Rs. 18,000
- DS303 — Rs. 15,000

The scenario contains both reasoning questions and a question requiring
external information through a tool.

The main ReAct question is:

"Which is cheaper: CS101 and AI202 with a 10% scholarship,
or all three courses with a 25% scholarship? By how much?"

The course fees are obtained using the course-fee tool and the final
amounts are calculated using the calculator tool.

---

## 2. Direct Prompting

Direct prompting sends the question directly to the language model.

The model produces an answer without using external tools and without
showing a reasoning process.

For questions where all required information is already available,
direct prompting can provide a quick answer.

However, for questions requiring information that is not available to
the model, direct prompting cannot retrieve that information using a
tool.

In my scenario, direct prompting can solve the calculation when the
course fees are included in the question. However, it cannot reliably
obtain a course fee from the course-fee tool.

---

## 3. Chain-of-Thought Prompting

Chain-of-Thought prompting asks the model to solve the question
step by step.

For example, it can calculate the total fee, calculate the scholarship,
calculate the remaining amount, and then divide the amount into
instalments.

This approach is useful for multi-step reasoning because the model is
given space to work through the problem.

However, Chain-of-Thought does not automatically provide external
information. If a required fact is missing, reasoning alone cannot
retrieve the fact from the course-fee tool.

Therefore, in my scenario, Chain-of-Thought is useful for calculations
and logical questions, but it is not sufficient when external course
fee information is required.

---

## 4. ReAct Agent

ReAct combines reasoning and tool usage.

The basic cycle is:

Thought → Action → Observation

The agent first identifies what information it needs.

It then performs an Action by calling a tool.

The result returned by the tool becomes the Observation.

The agent can then reason about the observation and perform another
action if necessary.

In my scenario, the agent can call get_course_fee for CS101, AI202
and DS303. It can then use the calculator tool to calculate the
discounted prices and compare them.

This allows the agent to use external information before producing
the final answer.

---

## 5. Comparison Table

| Basis | Direct Prompting | Chain-of-Thought | ReAct Agent |
|---|---|---|---|
| Reasoning depth | Basic/direct | Step-by-step | Step-by-step with actions |
| Tool usage | No tools | No tools | Uses tools |
| Reliability on multi-step questions | Depends on problem | Can improve multi-step reasoning | Can reason and obtain external data |
| Transparency | No visible reasoning | Steps are requested in the output | Thought, Action and Observation trace |
| Speed / cost | Usually fastest | Longer response | More tool/model calls |
| Consistency | Depends on temperature | Can vary when temperature > 0 | Depends on model and tool execution |

---

## 6. Self-Consistency Observation

For self-consistency, I used the instalment question from the
Chain-of-Thought experiment.

I ran the same question five times using a non-zero temperature.

My observed answers were:

- Run 1: [WRITE YOUR ACTUAL ANSWER]
- Run 2: [WRITE YOUR ACTUAL ANSWER]
- Run 3: [WRITE YOUR ACTUAL ANSWER]
- Run 4: [WRITE YOUR ACTUAL ANSWER]
- Run 5: [WRITE YOUR ACTUAL ANSWER]

The majority answer was:

[WRITE YOUR ACTUAL MAJORITY ANSWER]

The correct answer is Rs. 9,562.50.

When temperature is changed to 0, repeated answers become much more
similar because there is much less variation between runs.

---

## 7. Suitability Analysis

For my scenario, the three approaches demonstrate different
capabilities.

Direct prompting is useful when the question is straightforward and
all required information is already available.

Chain-of-Thought is useful when the question requires several reasoning
steps but does not require external information.

ReAct is useful when the question requires both reasoning and external
information. In my scenario, the course fees need to be obtained using
a tool before the calculations can be completed.

Therefore, the suitability of an approach depends on whether the
problem requires only a direct answer, multi-step reasoning, or both
reasoning and external information.

---

## 8. Conclusion

Direct prompting is appropriate for simple questions where a direct
answer is sufficient.

Chain-of-Thought is appropriate for multi-step reasoning problems where
the required information is already available.

ReAct is appropriate for problems that require reasoning together with
external information or tools.

The main difference is that Chain-of-Thought improves the reasoning
process but does not itself provide external information, while ReAct
combines reasoning with tool interaction through the
Thought → Action → Observation cycle.