"""Text Editor Action Tracker
Demonstrates Stacks (LIFO), Queues (FIFO), and Tuples.
"""

from collections import deque
from typing import Deque, List, Tuple

# Tuple type representing an action record: (action_type, payload)
Action = Tuple[str, str]


class TextEditorTracker:
    def __init__(self):
        # Stack for Undo history (LIFO)
        self.undo_stack: List[Action] = []
        # Stack for Redo history (LIFO)
        self.redo_stack: List[Action] = []
        # Queue for background print/export tasks (FIFO)
        self.print_queue: Deque[str] = deque()

    def perform_action(self, action_type: str, content: str) -> None:
        """Executes a new action, pushes it to the undo stack, and clears redo history."""
        action: Action = (action_type, content)
        self.undo_stack.append(action)
        self.redo_stack.clear()  # A new action invalidates previous redo history
        print(f"[+] Action performed: {action_type} '{content}'")

    def undo(self) -> None:
        """Undoes the last action (pops from undo stack, pushes to redo stack)."""
        if not self.undo_stack:
            print("[-] Nothing to undo.")
            return

        action = self.undo_stack.pop()
        self.redo_stack.append(action)
        print(f"[Undo] Reverted: {action[0]} '{action[1]}'")

    def redo(self) -> None:
        """Redoes the last undone action (pops from redo stack, pushes to undo stack)."""
        if not self.redo_stack:
            print("[-] Nothing to redo.")
            return

        action = self.redo_stack.pop()
        self.undo_stack.append(action)
        print(f"[Redo] Re-applied: {action[0]} '{action[1]}'")

    def queue_print_job(self, document_name: str) -> None:
        """Enqueues a document for background printing (FIFO)."""
        self.print_queue.append(document_name)
        print(f"[Queue] Added '{document_name}' to print queue.")

    def process_next_print_job(self) -> None:
        """Dequeues and processes the oldest print job (FIFO)."""
        if not self.print_queue:
            print("[-] Print queue is empty.")
            return

        job = self.print_queue.popleft()
        print(f"[Print] Processed print job: '{job}'")


def main():
    editor = TextEditorTracker()

    print("--- 1. Performing Actions (Stack Push) ---")
    editor.perform_action("WRITE", "Hello World")
    editor.perform_action("WRITE", " This is Python.")
    editor.perform_action("DELETE", "Python.")

    print("\n--- 2. Demonstrating Undo (Stack Pop -> Redo Push) ---")
    editor.undo()
    editor.undo()

    print("\n--- 3. Demonstrating Redo (Redo Pop -> Undo Push) ---")
    editor.redo()

    print("\n--- 4. Demonstrating Background Queue (FIFO) ---")
    editor.queue_print_job("Doc1_Draft.txt")
    editor.queue_print_job("Doc2_Final.pdf")

    print("\n--- 5. Processing Queue Jobs (FIFO Pop Left) ---")
    editor.process_next_print_job()
    editor.process_next_print_job()


if __name__ == "__main__":
    main()
