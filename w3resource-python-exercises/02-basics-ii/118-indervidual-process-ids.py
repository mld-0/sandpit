import os
import multiprocessing

def print_process_info(title):
    module_name = __name__
    parent_process_id = os.getppid()
    process_id = os.getpid()
    print(f"title=({title}), module_name=({module_name}), parent_process_id=({parent_process_id}), process_id=({process_id})")

def hello_world(title):
    print(f"Hello World: ({title})")
    print_process_info(title)

if __name__ == '__main__':
    print_process_info('main')
    p = multiprocessing.Process(target=hello_world, args=('hello process',))
    p.start()
    p.join()

