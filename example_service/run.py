import argparse
import sys
import os
import signal
from .app import create


def _quit(signal, frame):
    print('Shutting down!')
    sys.exit(0)


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Service Example')
    parser.add_argument('--config-file', help='Config file',
                        type=str, default=None)
    args = parser.parse_args(args=args)

    if args.config_file is not None:
        os.environ.set('FLASK_SETTINGS', args.config_file)

    app = create()

    host = app.config.get('host', '0.0.0.0')
    host = os.environ.get('HOST', host)

    port = app.config.get('port', 5000)
    port = os.environ.get('PORT', port)

    debug = app.config.get('DEBUG', False)

    signal.signal(signal.SIGINT, _quit)
    signal.signal(signal.SIGTERM, _quit)

    app.run(debug=debug, host=host, port=port)


if __name__ == "__main__":
    main()
