from utils.cli import CLI
if __name__ == '__main__':
    owner=input("enter your own wallet")
    app = CLI(owner)
    app.run()