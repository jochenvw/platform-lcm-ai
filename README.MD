# Platform Life Cycle Management(LCM) AI

Platform Lifecycle Management (LCM) is a critical process for managing cloud-native platforms, ensuring they are scalable, reliable, and efficient. The velocity at which hyperscalers providers like Azure, AWS, and Google Cloud introduce new services, features, and deprecate existing ones at an unprecedented pace. This velocity often surpasses the capacity of platform engineering teams to effectively manage and integrate these changes, posing significant challenges in cloud platform lifecycle management. Here we explore how AI can be integrated to automate and optimize LCM, addressing the challenges faced by organizations in managing their cloud infrastructure.

## The Commonplace Approach: A Recipe for Inefficiency
The conventional method of managing cloud platform lifecycle typically involves three steps:

![Miztiik - Platform Engineering with AI](images/miztiik_architecture_platform_lcm_ai_001.png)

1. **Identify Changes**: Monitor various sources to detect updates, deprecations, security advisories, and other modifications.

1. **Assess**: Evaluate the relevance and impact of these changes on the platform by applying a set of *guidelines* or *rules*. For instance, they might ask, "*Is TLS 1.1 deprecated?"*<sup>[1],[2]</sup> or "*Are there new security vulnerabilities?*"

1. **Implement**: Apply insights to the platform environment, often resulting in notifications to teams responsible.

![Miztiik - Platform Engineering with AI](images/miztiik_architecture_platform_lcm_ai_002.png)


To automate this effectively, we should translate the *guidelines* or *rules* into hard coded logic framework that matches curated data sources using string manipulation. While straightforward, this approach presents several significant limitations:  

- **Limited Adaptability**: Static rules quickly become obsolete due to rapid technological advancements and fail to capture complex platform interdependencies. Success hinges on the team's deep technical knowledge. Without it, critical updates risk being missed or misunderstood. 
- **Lack of Actionable Specificity**: The process relies on broad guidance without clear, actionable steps, placing a heavy burden on individual expertise and leading to inconsistent execution.  
- **Reactive Approach**: Teams often address issues only after they occur, increasing the likelihood of service disruptions rather than proactively mitigating risks.  


## Platform LCM AI

To perform lifecycle management (LCM) that evolves and adapts, transform static rule-based logic into an adaptive reasoning engine. The advancements in AI, particularly large language models (LLMs), to summarize and identify relationships in text allows us to combine our _Sources_ and _Rules_ to effectively create a _reasoning engine_. Now teams can update the behaviour of the _reasoning engine_ using natural language instead of code. This allows teams to update rules dynamically with reduced cognitive overhead.

![Miztiik - Platform Engineering with AI](images/miztiik_architecture_platform_lcm_ai_003.png)

Incorporating environmental or workload metadata into these systems facilitates the transition from generic guidance to actionable, prescriptive recommendations tailored to specific workloads. This targeted approach empowers teams to execute tasks consistently and proactively, minimizing reliance on individual expertise and reducing the risk of service disruptions.

![Miztiik - Platform Engineering with AI](images/miztiik_architecture_platform_lcm_ai_004.png)

Embracing AI-driven solutions in platform LCM enhances operational efficiency and also positions organizations to better navigate the complexities of modern cloud environments. By leveraging the advanced reasoning capabilities of LLMs, businesses can achieve a more resilient and responsive infrastructure, ensuring sustained success in an ever-changing digital landscape.


## Limitations and Mitigations

Schillace<sup>[6]</sup> & Ethan Mollick<sup>[7]</sup> are of the opinion *"The models get better over time".*  However, current generation of AI models are not perfect and have limitations. Here are some of the limitations and potential mitigation strategies:

- Data Quality (Bias, Incompleteness, Noise)
- Hallucination

One potential mitigation strategy is to implement a human-in-the-loop system that allows human operators to review and correct the AI's decisions. This approach ensures that the AI system remains aligned with the organization's goals and values while leveraging the efficiency and scalability of AI-driven solutions.


## Conclusion

By transforming static rule-based systems into adaptive reasoning engines, organizations can better navigate the increasing complexity of cloud environments while reducing operational overhead. The successful adoption of AI-driven LCM depends not just on the technology itself, but on how well it's integrated into existing workflows and systems.


## What's Next: Technical Deep Dive
In Part 2 of this series, we'll explore the technical implementation details of Platform LCM AI, including:

- Modular Pipeline Architecture
- Enhancement Phase
  - Advanced reasoning capabilities  - GraphRAG perhaps?
  - Extended tool integration
- Optimization Phase
  - Self-improving capabilities with Confidence scoring, Validation gates, and Feedback loops
  - Advanced automation

Constructing the AI reasoning engine using Azure OpenAI
Building resilient data pipelines for cloud provider updates
Implementing confidence scoring and validation gates
Creating feedback loops for continuous improvement
Developing integration patterns with existing DevOps tools

Stay tuned as we transform these concepts into practical, implementable solutions for modern cloud environments.


### 📚 References

1. [Azure TLS Deprecation][1]
1. [AWS TLS Deprecation][2]
1. [Overlooked Challenge of Efficiently Decommissioning Resources][3]
1. [Unleash AI in Platform Engineering][4]
1. [Gartner - How to Govern a Hybrid Multicloud Environment][5]
1. [Schillace Laws][6]
1. [Ethan Mollick - Assume this is the worst AI you will ever use][7]
1. [Ethan Mollick - One useful thing][8]
1. [Microsoft GraphRAG][9]



[1]: https://learn.microsoft.com/en-us/lifecycle/announcements/tls-support-ending-10-31-2024
[2]: https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/
[3]: https://blog.omnistrate.com/posts/49
[4]: https://thenewstack.io/integrating-ai-to-make-platform-engineering-intelligent/
[5]: https://www.gartner.com/en/documents/5446963
[6]: https://devblogs.microsoft.com/semantic-kernel/early-lessons-from-gpt-4-the-schillace-laws/#the-schillace-laws-in-practice:~:text=can%20do%20it%3B-,the%20model%20will%20get%20better%2C%20but%20the%20code%20won%E2%80%99t.,-Trade%20leverage%20for
[7]: https://www.gsb.stanford.edu/insights/co-intelligence-ai-masterclass-ethan-mollick#:~:text=instructions%20at%20all.%E2%80%9D-,Assume%20this%20is%20the%20worst%20AI%20you%20will%20ever%20use,-.%E2%80%9CWe%E2%80%99re%20early
[8]: https://www.oneusefulthing.org/p/what-people-ask-me-most-also-some?r=o98ff&utm_campaign=post&utm_medium=email&triedRedirect=true#:~:text=all%20three%20scenarios.-,The%20only%20thing%20I%20know%20for%20sure%20is%20that%20the%20AI%20you%20are%20using%20today%20is%20the%20worst%20AI%20you%20are%20ever%20going%20to%20use,-%2C%20since%20we%20are
[9]:https://microsoft.github.io/graphrag/