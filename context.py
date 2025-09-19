# gotermix54/context.py
import json
from pathlib import Path

class ContextManager:
    def __init__(self):
        self.context_path = Path.cwd() / ".gotermix54" / "context.json"
        self.context = self.load()

    def load(self):
        if not self.context_path.exists():
            return {"files": [], "project_goal": "", "memory": []}
        with open(self.context_path, 'r') as f:
            return json.load(f)

    def save(self):
        self.context_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.context_path, 'w') as f:
            json.dump(self.context, f, indent=2)

    def add_file(self, filepath):
        if filepath not in self.context["files"]:
            self.context["files"].append(filepath)
            self.save()

    def set_goal(self, goal):
        self.context["project_goal"] = goal
        self.save()

    def add_memory(self, msg):
        self.context["memory"].append(msg)
        if len(self.context["memory"]) > 100:  # limit
            self.context["memory"] = self.context["memory"][-50:]
        self.save()
