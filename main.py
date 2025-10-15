def main():
    print("Hello from obfuxtreme!")


if __name__ == "__main__":
    import multiprocessing

    p = multiprocessing.Process(target=main)
    p.start()
    p.join()
    p = multiprocessing.Process(target=main)
    p.start()
    p.join()
    print("Process finished.")
