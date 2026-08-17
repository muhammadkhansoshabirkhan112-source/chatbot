# 🤖 NOVA AI - Rule-Based AI Chatbot

**Project 1 | DecodeLabs Industrial Training Kit (Batch 2026)**

A production-grade rule-based AI chatbot built with pure Python, demonstrating fundamental concepts in control flow, logic, and decision-making. This project forms the foundation for understanding how AI systems process information and generate responses.

---

## 🎯 Project Overview

### Goal
Create a simple rule-based chatbot that responds to predefined user inputs using if-else logic and runs in a continuous loop.

### Key Features
✅ **Intelligent Intent Matching** - Dictionary-based hash maps for O(1) efficient lookup  
✅ **Input Sanitization** - Handles case normalization and whitespace cleanup  
✅ **Fallback Handling** - Graceful responses for unknown inputs  
✅ **Session Management** - Tracks conversation history  
✅ **Modular Architecture** - Clean separation of concerns  
✅ **Error Handling** - Robust exception management  
✅ **Production Ready** - Professional code standards  

### Technology Stack
- **Language:** Python 3.7+
- **Architecture:** IPO Model (Input → Process → Output)
- **Data Structure:** Hash Maps (Dictionaries) for O(1) lookup
- **Paradigm:** Rule-based Logic (No ML/DL - yet!)

---

## 📊 Architecture

### IPO (Input-Process-Output) Model

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  INPUT → SANITIZE → MATCH → RESPOND → OUTPUT      │
│                                                     │
│  Phase 1: Raw user input                           │
│  Phase 2: Normalize and clean input                │
│  Phase 3: Match against known patterns             │
│  Phase 4: Generate response from knowledge base    │
│  Phase 5: Send response to user                    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Component Structure

```
chatbot.py (Main Chatbot Class)
    ├── utils.py
    │   ├── InputSanitizer (Cleaning & Normalization)
    │   ├── KnowledgeBase (Intent Storage & Lookup)
    │   ├── ResponseEngine (IPO Processing)
    │   └── SessionManager (Conversation History)
    │
    └── intents.json (Knowledge Base File)
        ├── 10+ Intents
        ├── 50+ Patterns
        └── 100+ Responses
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- No external dependencies (pure Python)

### Installation

1. **Clone or download the project:**
```bash
cd NOVA-AI-Chatbot
```

2. **Verify files are present:**
```bash
ls -la
# Should show: chatbot.py, utils.py, intents.json, requirements.txt, README.md
```

3. **Run the chatbot:**
```bash
python chatbot.py
```

### Usage Example

```
========================================================
🤖 NOVA AI - Rule-Based AI Chatbot
   DecodeLabs Industrial Training Kit 2026
========================================================

✓ NOVA AI initialized successfully
✓ Type 'exit' or 'quit' to end conversation

╔════════════════════════════════════════════════════╗
║           Welcome to NOVA AI Chatbot!              ║
║                                                    ║
║  I'm a rule-based AI assistant powered by logic.  ║
║  Type 'exit' or 'quit' to end the conversation.   ║
╚════════════════════════════════════════════════════╝

You: Hello!

NOVA AI: Hi there! How can I help you today?

You: Tell me a joke

NOVA AI: Why do programmers prefer dark mode? Because light attracts bugs!

You: exit

NOVA AI: Goodbye! Have a great day!
```

---

## 📚 Knowledge Base

The chatbot has 10 primary intents covering:

| Intent | Purpose | Example Patterns |
|--------|---------|------------------|
| **greeting** | Respond to greetings | hello, hi, hey, good morning |
| **farewell** | Say goodbye | bye, goodbye, see you, farewell |
| **about_bot** | Information about the chatbot | who are you, what is your name |
| **weather** | Handle weather queries | how is the weather, weather forecast |
| **help** | Provide assistance | help, can you help, assist me |
| **joke** | Tell jokes | tell me a joke, make me laugh |
| **name** | Respond to name-related queries | what is your name, call me |
| **ai_concept** | Explain AI | what is AI, explain artificial intelligence |
| **decodelabs** | Information about DecodeLabs | who created you, decodelabs |
| **time** | Handle time queries | what time is it, current time |

**Total Coverage:**
- 10 Intents
- 50+ Patterns
- 100+ Response Variations
- Fallback Responses for Unknown Input

### Adding New Intents

Edit `intents.json`:
```json
{
  "tag": "your_intent",
  "patterns": [
    "pattern1",
    "pattern2",
    "pattern3"
  ],
  "responses": [
    "Response 1",
    "Response 2",
    "Response 3"
  ]
}
```

---

## 💻 Code Structure

### chatbot.py
Main chatbot class implementing:
- Infinite loop pattern
- Input validation
- Exit strategy
- Session tracking
- Error handling

```python
class NOVAIChatbot:
    def run(self):
        """Main chatbot loop - THE HEARTBEAT"""
        while True:
            user_input = input("You: ")
            response = self.handle_user_input(user_input)
            if response == "EXIT_SIGNAL":
                break
            print(f"NOVA AI: {response}")
```

### utils.py
Utility classes:

#### InputSanitizer
- Lowercase conversion
- Whitespace removal
- Extra space cleanup

#### KnowledgeBase
- JSON loading
- Pattern indexing
- O(1) intent lookup via hash map

#### ResponseEngine
- IPO model implementation
- Intent matching
- Random response selection

#### SessionManager
- Conversation history
- Turn tracking
- Message logging

### intents.json
Knowledge base containing:
- Intent definitions
- Pattern examples
- Response templates

---

## 🔑 Key Algorithms

### Pattern Matching Strategy
```python
def get_intent(self, user_input):
    # Strategy 1: Exact match (O(1))
    if user_input in pattern_map:
        return pattern_map[user_input]
    
    # Strategy 2: Substring match (O(n))
    for pattern, intent in pattern_map.items():
        if pattern in user_input:
            return intent
    
    return None  # No match found
```

### Efficiency Analysis
- **Pattern Lookup:** O(1) via hash map
- **Intent Resolution:** O(1) average case
- **Response Selection:** O(1) random choice
- **Overall Complexity:** O(1) per turn

---

## 🎓 Learning Outcomes

By building this project, you'll understand:

1. **Control Flow** - If-else logic and loops
2. **Data Structures** - Hash maps and dictionaries
3. **Architecture Patterns** - IPO model
4. **Logic Design** - Decision-making systems
5. **Error Handling** - Graceful exception management
6. **Software Design** - Modular, maintainable code
7. **State Management** - Session tracking
8. **User Interface** - Interactive command-line applications

---

## 🧪 Testing

### Test the chatbot interactively:
```bash
python chatbot.py
```

### Test single turns:
```python
from chatbot import NOVAIChatbot

bot = NOVAIChatbot()
response = bot.run_single_turn("hello")
print(response)  # Output: Hi there! How can I help you today?
```

### Expected Test Cases

| Input | Expected Output |
|-------|-----------------|
| "hello" | Greeting response |
| "tell me a joke" | Joke response |
| "exit" | Chatbot exits |
| "who are you" | About bot response |
| "random xyz" | Fallback response |

---

## 📈 Future Enhancements

**Phase 2 - Machine Learning Integration:**
- NLP with NLTK/spaCy
- Intent classification using ML models
- Named entity recognition
- Sentiment analysis

**Phase 3 - Advanced Features:**
- Context awareness
- Multi-turn conversations
- Personality modeling
- Integration with APIs

---

## 🛠️ Troubleshooting

### FileNotFoundError: intents.json
**Solution:** Ensure `intents.json` is in the same directory as `chatbot.py`

### No module named 'utils'
**Solution:** Ensure `utils.py` is in the same directory

### ModuleNotFoundError for json
**Solution:** json is built-in; ensure Python 3.7+ is installed

---

## 📝 Code Standards

This project follows:
- **PEP 8** - Python style guide
- **Type Hints** - For clarity
- **Docstrings** - For documentation
- **Comments** - For complex logic
- **Error Handling** - Try-except blocks

---

## 🏆 DecodeLabs Certification

**Project Requirements:** ✅ All Met
- [x] Rule-based logic implementation
- [x] Handle greetings and exits
- [x] If-else decision making
- [x] Continuous loop
- [x] Professional code quality
- [x] Complete documentation

---

## 📞 Support & Contact

**DecodeLabs:**
- 📧 decodelabs.tech@gmail.com
- 📱 +91 89330 06408
- 🌐 www.decodelabs.tech
- 📍 Greater Lucknow, India

**Created:** Batch 2026  
**Version:** 1.0.0  
**Last Updated:** 2026

---

## 📜 License

This project is created as part of DecodeLabs Industrial Training Kit.

---

## 💡 Tips for Success

1. **Understand the IPO Model** - Input → Process → Output
2. **Study the intent structure** - See how rules work
3. **Experiment with new intents** - Add your own patterns
4. **Improve responses** - Make them more personalized
5. **Track the session** - Understand conversation flow
6. **Extend functionality** - Add context awareness

---

**Happy Learning! Build Something Amazing! 🚀**
