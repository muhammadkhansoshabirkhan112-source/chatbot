"""
NOVA AI - Utility Functions
Helper functions for input sanitization, intent matching, and response generation.
"""

import json
import random
from typing import Dict, List, Tuple, Optional


class InputSanitizer:
    """
    Handles input sanitization and normalization.
    Converts user input to lowercase and removes extra whitespace.
    """
    
    @staticmethod
    def sanitize(user_input: str) -> str:
        """
        Sanitize user input by:
        1. Converting to lowercase
        2. Removing leading/trailing whitespace
        3. Removing extra spaces between words
        
        Args:
            user_input (str): Raw user input
            
        Returns:
            str: Sanitized input
        """
        # Remove leading/trailing whitespace
        cleaned = user_input.strip()
        
        # Convert to lowercase for case-insensitive matching
        cleaned = cleaned.lower()
        
        # Remove extra spaces between words
        cleaned = ' '.join(cleaned.split())
        
        return cleaned


class KnowledgeBase:
    """
    Manages the chatbot's knowledge base of intents and responses.
    Uses efficient dictionary-based lookup for O(1) access.
    """
    
    def __init__(self, intents_file: str = "intents.json"):
        """
        Initialize knowledge base from JSON file.
        
        Args:
            intents_file (str): Path to intents.json file
        """
        self.intents = {}
        self.pattern_to_intent = {}  # Hash map for O(1) pattern lookup
        self.load_intents(intents_file)
    
    def load_intents(self, intents_file: str) -> bool:
        """
        Load intents from JSON file.
        
        Args:
            intents_file (str): Path to intents.json
            
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        try:
            with open(intents_file, 'r') as f:
                data = json.load(f)
            
            # Build knowledge base and pattern lookup map
            for intent in data.get('intents', []):
                tag = intent.get('tag')
                patterns = intent.get('patterns', [])
                responses = intent.get('responses', [])
                
                self.intents[tag] = {
                    'patterns': patterns,
                    'responses': responses
                }
                
                # Map each pattern to its intent tag for fast lookup
                for pattern in patterns:
                    self.pattern_to_intent[pattern] = tag
            
            print(f"✓ Knowledge base loaded: {len(self.intents)} intents")
            return True
        
        except FileNotFoundError:
            print(f"✗ Error: {intents_file} not found!")
            return False
        except json.JSONDecodeError:
            print("✗ Error: Invalid JSON format in intents file!")
            return False
        except Exception as e:
            print(f"✗ Error loading intents: {str(e)}")
            return False
    
    def get_intent(self, user_input: str) -> Optional[str]:
        """
        Match user input to an intent using pattern matching.
        
        Matching Strategy:
        1. Try exact phrase match (fastest)
        2. Try substring match (contains any pattern)
        3. Return None if no match found
        
        Args:
            user_input (str): Sanitized user input
            
        Returns:
            Optional[str]: Intent tag or None if not found
        """
        # Strategy 1: Exact match in hash map (O(1))
        if user_input in self.pattern_to_intent:
            return self.pattern_to_intent[user_input]
        
        # Strategy 2: Substring matching (user input contains a pattern)
        for pattern, intent_tag in self.pattern_to_intent.items():
            if pattern in user_input:
                return intent_tag
        
        return None
    
    def get_response(self, intent_tag: str) -> Optional[str]:
        """
        Get a random response for the given intent.
        
        Args:
            intent_tag (str): The intent tag
            
        Returns:
            Optional[str]: Random response or None if intent not found
        """
        if intent_tag not in self.intents:
            return None
        
        responses = self.intents[intent_tag].get('responses', [])
        if not responses:
            return None
        
        return random.choice(responses)


class ResponseEngine:
    """
    Core engine for generating chatbot responses.
    Implements the IPO (Input -> Process -> Output) model.
    """
    
    def __init__(self, knowledge_base: KnowledgeBase):
        """
        Initialize response engine with knowledge base.
        
        Args:
            knowledge_base (KnowledgeBase): The chatbot's knowledge base
        """
        self.kb = knowledge_base
        self.sanitizer = InputSanitizer()
    
    def process(self, user_input: str, default_response: str = "I do not understand. Could you rephrase that?") -> str:
        """
        Process user input and generate response.
        
        Flow:
        1. INPUT: Sanitize raw user input
        2. PROCESS: Match to intent and get response
        3. OUTPUT: Return response (or default if no match)
        
        Args:
            user_input (str): Raw user input
            default_response (str): Fallback response
            
        Returns:
            str: Generated response
        """
        # PHASE 1: INPUT & SANITIZATION
        sanitized_input = self.sanitizer.sanitize(user_input)
        
        # PHASE 2: PROCESS (Intent Matching)
        intent_tag = self.kb.get_intent(sanitized_input)
        
        # PHASE 3: OUTPUT (Response Generation)
        if intent_tag:
            response = self.kb.get_response(intent_tag)
            if response:
                return response
        
        # FALLBACK: Return default response if no match
        return default_response


class SessionManager:
    """
    Manages chatbot session tracking and conversation flow.
    """
    
    def __init__(self):
        """Initialize session manager."""
        self.messages = []
        self.turn_count = 0
    
    def add_message(self, role: str, content: str) -> None:
        """
        Add a message to conversation history.
        
        Args:
            role (str): 'user' or 'bot'
            content (str): Message content
        """
        self.messages.append({
            'role': role,
            'content': content,
            'turn': self.turn_count
        })
    
    def increment_turn(self) -> None:
        """Increment conversation turn counter."""
        self.turn_count += 1
    
    def get_conversation_history(self) -> List[Dict]:
        """
        Get full conversation history.
        
        Returns:
            List[Dict]: List of messages
        """
        return self.messages
    
    def get_last_user_message(self) -> Optional[str]:
        """
        Get the last user message.
        
        Returns:
            Optional[str]: Last user message or None
        """
        for msg in reversed(self.messages):
            if msg['role'] == 'user':
                return msg['content']
        return None
    
    def reset(self) -> None:
        """Reset session (clear history and turn count)."""
        self.messages = []
        self.turn_count = 0


# Export classes
__all__ = [
    'InputSanitizer',
    'KnowledgeBase',
    'ResponseEngine',
    'SessionManager'
]
