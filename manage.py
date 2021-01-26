from app import create_app
from flask_script import Manager, Server

app = create_app()

if __name__ == '__main__':
    print(app.url_map)

    manager = Manager(app)
    manager.add_command('runserver', Server(host='127.0.0.1', port=9000))
    manager.run()
