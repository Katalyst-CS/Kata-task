from datetime import datetime
class TaskEntity:
    id: str
    title: str
    description: str
    created_date: datetime
    start_date = datetime
    end_date = datetime
    project_id = str
    metadata = {}
    watchers = []

    def set_metadata(self, metadata: dict):
        self.metadata = metadata
    
    def add_meta(self, key: str, value):
        self.metadata[key] = value

    def set_watchers(self, watchers):
        self.watchers = watchers
    
    def add_watcher(self, watcher):
        self.watchers.append(watcher)