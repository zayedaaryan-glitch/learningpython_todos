def get_jobs(filepath='pending_jobs.txt'):
    """ Reads filepath and returns a list of
    pending job items.
    """
    with open(filepath , "r") as file_local:
        pending_jobs_local = file_local.readlines()
    return pending_jobs_local


def write_jobs(pending_jobs_local, filepath='pending_jobs.txt', ):
    """ Writes pending job items to a text file.
    """
    with open(filepath , "w") as file_local:
        file_local.writelines(pending_jobs_local)

if __name__ == "__main__":
    print("hello world")
    print(get_jobs())
