"""
NOVA AI - Rule-Based AI Chatbot
Project 1: DecodeLabs Industrial Training Kit (Batch 2026)

Architecture: IPO Model (Input -> Process -> Output)
- Input Phase: User input sanitization and normalization
- Process Phase: Intent matching using rule-based logic
- Output Phase: Response generation from knowledge base

Technologies: Pure Python, No ML/DL (Logic & Control Flow)
"""

import sys
from utils import (
    InputSanitizer,
    KnowledgeBase,
    ResponseEngine,
    SessionManager
)


class NOVAIChatbot:
    """
    NOVA AI - Rule-Based Chatbot
    
    Main chatbot class implementing the complete conversation loop.
    Uses hash maps for efficient intent matching (O(1) lookup).
    """
    
    def __init__(self, intents_file: str = "intents.json"):
        """
        Initialize NOVA AI chatbot.
        
        Args:
            intents_file (str): Path to intents JSON file
        """
        print("\n" + "="*60)
        print("🤖 NOVA AI - Rule-Based AI Chatbot")
        print("   DecodeLabs Industrial Training Kit 2026")
        print("="*60 + "\n")
        
        # Initialize components
        self.kb = KnowledgeBase(intents_file)
        self.engine = ResponseEngine(self.kb)
        self.session = SessionManager()
        self.exit_commands = ['exit', 'quit', 'bye', 'goodbye', 'stop', 'end']
        
        # Check if knowledge base loaded successfully
        if not self.kb.intents:
            print("✗ Failed to initialize chatbot. No intents loaded.")
            sys.exit(1)
        
        print("✓ NOVA AI initialized successfully")
        print("✓ Type 'exit' or 'quit' to end conversation\n")
    
    def should_exit(self, user_input: str) -> bool:
        """
        Check if user wants to exit the conversation.
        
        Args:
            user_input (str): Sanitized user input
            
        Returns:
            bool: True if user wants to exit, False otherwise
        """
        # Normalize input for exit check
        normalized = user_input.lower().strip()
        
        # Check if input is in exit commands
        return normalized in self.exit_commands
    
    def display_welcome_message(self) -> None:
        """Display welcome message and instructions."""
        welcome = """
╔════════════════════════════════════════════════════════════╗
║           Welcome to NOVA AI Chatbot!                      ║
║                                                            ║
║  I'm a rule-based AI assistant powered by logic and      ║
║  decision-making. Ask me about greetings, jokes, AI,     ║
║  weather, or anything else!                              ║
║                                                            ║
║  Type 'exit' or 'quit' to end the conversation.           ║
╚════════════════════════════════════════════════════════════╝
"""
        print(welcome)
    
    def display_goodbye_message(self) -> None:
        """Display goodbye message."""
        goodbye = """
╔════════════════════════════════════════════════════════════╗
║           Thanks for chatting with NOVA AI!               ║
║                                                            ║
║  Sessions: {}  |  Conversations: {}
║                                                            ║
║  See you next time! 👋                                     ║
╚════════════════════════════════════════════════════════════╝
""".format(self.session.turn_count, len(self.session.get_conversation_history()) // 2)
        print(goodbye)
    
    def handle_user_input(self, user_input: str) -> str:
        """
        Handle complete user input workflow.
        
        Workflow:
        1. Validate input (not empty)
        2. Sanitize input
        3. Check for exit command
        4. Generate response
        5. Track in session
        
        Args:
            user_input (str): Raw user input
            
        Returns:
            str: Bot response or exit signal
        """
        # Validation: Check for empty input
        if not user_input or not user_input.strip():
            return "Please say something! 😊"
        
        # Sanitization: Clean up input
        sanitized_input = InputSanitizer.sanitize(user_input)
        
        # Track user message in session
        self.session.add_message('user', user_input)
        
        # Exit Strategy: Check if user wants to quit
        if self.should_exit(sanitized_input):
            return "EXIT_SIGNAL"
        
        # Process: Generate response through response engine
        response = self.engine.process(sanitized_input)
        
        # Track bot response in session
        self.session.add_message('bot', response)
        
        return response
    
    def run(self) -> None:
        """
        Main chatbot loop - THE HEARTBEAT.
        
        Implements infinite loop pattern:
        - Continues until user exits
        - Processes one turn per iteration
        - Maintains conversation state
        
        Architecture:
        while True:
            user_input = get_input()
            if user_input == 'exit':
                break
            response = process(user_input)
            print(response)
        """
        self.display_welcome_message()
        
        # THE INFINITE LOOP - HEARTBEAT OF THE CHATBOT
        while True:
            try:
                # INPUT PHASE: Get user input
                user_input = input("You: ").strip()
                
                # PROCESS PHASE: Handle input through workflow
                response = self.handle_user_input(user_input)
                
                # EXIT CONDITION: Check for exit signal
                if response == "EXIT_SIGNAL":
                    print("\nNOVA AI: Goodbye! Have a great day!")
                    break
                
                # OUTPUT PHASE: Display response
                print(f"\nNOVA AI: {response}\n")
                
                # Increment turn counter
                self.session.increment_turn()
            
            except KeyboardInterrupt:
                # Handle Ctrl+C gracefully
                print("\n\nNOVA AI: Interrupted. Goodbye!")
                break
            
            except EOFError:
                # Handle EOF (end of input stream)
                break
            
            except Exception as e:
                # Catch any unexpected errors
                print(f"\n✗ Error: {str(e)}")
                print("NOVA AI: I encountered an error. Please try again.\n")
        
        # Display final statistics
        self.display_goodbye_message()
    
    def run_single_turn(self, user_input: str) -> str:
        """
        Run a single conversation turn (useful for testing).
        
        Args:
            user_input (str): User input
            
        Returns:
            str: Bot response
        """
        response = self.handle_user_input(user_input)
        self.session.increment_turn()
        return response


def main():
    """Entry point for the chatbot application."""
    try:
        # Create and run chatbot
        chatbot = NOVAIChatbot(intents_file="intents.json")
        chatbot.run()
    
    except KeyboardInterrupt:
        print("\n\n✗ Chatbot interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"✗ Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
