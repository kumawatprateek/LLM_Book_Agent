Design Document

Introduction
This document explains the design and reasoning behind the LLM-based book selection agent.

Approach
- **Language Model**: Utilized Hugging Face's GPT-3.5 equivalent for generating responses.
- **API Framework**: FastAPI was chosen for its simplicity and performance.

Workflow
1. User Request: User asks for top books.
2. Filter Top 10: Agent filters from the top 100.
3. User Selection: Agent helps select one book based on preference.
4. Text Generation: Generate personalized responses or recommendations.
5. Conclusion: Agent concludes with a thank you message.

Reasoning
- Modularity: Each task is modular for easy debugging and testing.
- Scalability: Can easily extend to more genres or detailed selection criteria.

Future Work
- Integration with a real book database.
- Enhanced user preference handling.
