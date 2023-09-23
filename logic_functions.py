from typing import List
from myclass import Task

def create_task(title, details, priority, story_points):
    new_task = Task(title, details, priority, story_points)
    return new_task

def get_task(task_list: List[Task], task_name):
    for task in task_list:
        if task.title == task_name:
            return task
        return None

def delete_task(task_list: List[Task], task_name):
    find_task = get_task(task_list, task_name) 
    task_list.remove(find_task)

def update_task(task_list: List[Task], task_name, new_details=None, new_priority=None, new_story_points=None):
    find_task = get_task(task_list, task_name)
    if new_details is not None:
        find_task.details = new_details
    if new_priority is not None:
        find_task.priority = new_priority
    if new_story_points is not None:
        find_task.new_story_points = new_story_points
        return True
    return False



   
    


    
            
                






    
